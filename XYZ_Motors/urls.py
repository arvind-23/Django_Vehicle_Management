"""
URL configuration for XYZ_Motors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from InventoryManagement import views

from .settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('upload/',views.upload,name="upload-vehicle"),
    path('delete/<int:vehicle>',views.delete_vehicle,name="delete-vehicle"),
    path('update/<int:vehicle>',views.update_vehicle,name="update-vehicle"),
    path('feedback/', views.feedback_view, name='feedback'),
    path('test_drive/', views.test_drive_view, name='test_drive'),
    ]

if DEBUG:
    urlpatterns+=static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)