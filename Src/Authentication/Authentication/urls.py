from django.contrib import admin
from django.urls import path, include
import Auth
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Auth.urls'))
]
