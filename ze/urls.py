"""ze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import ze

#import my_users, patient







urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('my_users.urls')),
    path('patients/', include('patient.urls')),
    path('rv/', include('rv.urls')),
    path('', include('home.urls')),
]

handler404 = 'ze.views.error_404'
handler500 = 'ze.views.error_500'
handler403 = 'ze.views.error_403'
handler400 = 'ze.views.error_400'
