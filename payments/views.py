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
    Створює платіж у PayPal
    """
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

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)
        else:
            return JsonResponse({"error": payment.error})
    return render(request, "create_payment.html")

def payment_success(request):
    """
    Обробляє успішну оплату
    """
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, "payment_success.html", {"message": "Payment successful!"})
    else:
        return render(request, "payment_error.html", {"error": payment.error})

def payment_cancel(request):
    """
    Обробляє скасування платежу
    """
    return render(request, "payment_cancel.html", {"message": "The payment was canceled."})

def process_payment(request):
    """
    Додаткова обробка платежу (якщо потрібно)
    """
    if request.method == "POST":
        return JsonResponse({"message": "Payment processed successfully!"})
    return JsonResponse({"error": "Invalid request method."})
