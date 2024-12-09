"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
urlpatterns = [
    path('G3h9bX1m2kT7vRz8Pj7236/', admin.site.urls),
    path('', include('home.urls')),
    path('messages/', include('message.urls')),
    path('earning/', include('earning.urls')),
    path('payment/', include('payment.urls')),
    path('community/', include('community.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
