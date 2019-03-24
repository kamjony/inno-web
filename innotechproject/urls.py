from django.contrib import admin
from django.urls import path
import innotech.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', innotech.views.home, name='home'),
    path('products/', innotech.views.productlist, name='productlist'),
    path('products/<int:product_id>', innotech.views.product_detail, name='product_detail'),
    path('contact/', innotech.views.contact, name='contact'),
    path('about/', innotech.views.about, name='about'),
    path('success/', innotech.views.successView, name='success'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
