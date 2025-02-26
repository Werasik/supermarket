from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Products.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('shipping/', include('shipping.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
