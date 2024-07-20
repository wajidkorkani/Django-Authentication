from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', Home, name='home'),
    path('authentication', UserRegistration, name='ur'),
    path('login', LoginUser, name='login'),
    path('logout', LogoutUser, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
