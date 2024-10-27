"""
URL configuration for django_db1 project.

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
from django.contrib import admin
from django.urls import path
from computer_hardware_store import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('builders', views.BuilderAPI, basename='builders')
router.register('computers', views.ComputerAPI, basename='computers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('computers_list/', views.ComputersList.as_view(), name='computers_list'),
    path('computer/<int:pk>/', views.ComputersDetail.as_view(), name='computer_detail'),
    path('computer/<int:pk>/update/', views.ComputersUpdate.as_view(), name='computer_update'),
    path('computer_create/', views.ComputersCreate.as_view(), name='computer_create'),
    path('computer/<int:pk>/delete/', views.ComputersDelete.as_view(), name='computer_delete'),
#    path('computers_list_template_view/', views.ComputersListTemplateView.as_view(), name='computers_list_template_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls