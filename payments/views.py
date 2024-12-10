from django.shortcuts import render, redirect
from django.http import JsonResponse
from .paypal import paypalrestsdk

def create_payment(request):
    if request.method == "POST":
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://127.0.0.1:8000/payment-success/",
                "cancel_url": "http://127.0.0.1:8000/payment-cancel/"
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
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, "payment_success.html", {"message": "Payment successful!"})
    else:
        return render(request, "payment_error.html", {"error": payment.error})


def payment_cancel(request):
    return render(request, "payment_cancel.html", {"message": "The payment was canceled."})
