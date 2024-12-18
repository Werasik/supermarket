from django.shortcuts import render, redirect
from django.http import JsonResponse
import paypalrestsdk
from django.conf import settings

# Налаштування PayPal SDK
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # "sandbox" або "live"
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

def create_payment(request):
    """
    Створює платіж через PayPal та перенаправляє користувача на сторінку підтвердження.
    """
    try:
        if request.method == "POST":
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "redirect_urls": {
                    "return_url": request.build_absolute_uri('/payments/payment_success/'),
                    "cancel_url": request.build_absolute_uri('/payments/payment_cancel/')
                },
                "transactions": [{
                    "amount": {
                        "total": "10.00",
                        "currency": "USD"
                    },
                    "description": "Payment for online supermarket goods"
                }]
            })

            # Створення платежу
            if payment.create():
                for link in payment.links:
                    if link.rel == "approval_url":
                        request.session['payment_id'] = payment.id  # Зберігаємо payment_id
                        return redirect(link.href)
            else:
                return JsonResponse({"error": payment.error}, status=400)
        else:
            return render(request, "create_payment.html")
    except Exception:
        return JsonResponse({"error": "An unexpected error occurred."}, status=500)


def payment_success(request):
    """
    Обробляє підтвердження оплати після повернення користувача з PayPal.
    """
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")

    if not payment_id or not payer_id:
        return render(request, "payment_error.html", {"error": "Invalid payment details."})

    try:
        payment = paypalrestsdk.Payment.find(payment_id)

        # Виконання платежу
        if payment.state == "created" and payment.execute({"payer_id": payer_id}):
            return render(request, "payment_success.html", {"message": "Payment successful!"})
        else:
            return render(request, "payment_error.html", {"error": payment.error})
    except paypalrestsdk.ResourceNotFound:
        return render(request, "payment_error.html", {"error": "Payment not found. Invalid payment ID."})
    except Exception:
        return render(request, "payment_error.html", {"error": "An error occurred during payment processing."})


def payment_cancel(request):
    """
    Обробляє скасування платежу.
    """
    return render(request, "payment_cancel.html", {"message": "The payment was canceled."})


def process_payment(request):
    """
    Додаткова обробка платежу (якщо потрібно).
    """
    if request.method == "POST":
        return JsonResponse({"message": "Payment processed successfully!"})
    return JsonResponse({"error": "Invalid request method."})
