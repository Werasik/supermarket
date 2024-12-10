import paypalrestsdk
from django.conf import settings
from .paypal import paypalrestsdk

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # "sandbox" або "live"
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})
