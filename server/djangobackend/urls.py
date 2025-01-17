"""djangobackend URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('api/', api_views.get_api_view),
    path('api/dealership_rest', api_views.get_dealership_list),
    path('api/dealership_rest_set', api_views.set_dealership),
    path('api/dealership_rest_del/<str:pk>/', api_views.del_dealership),
    path('api/reviews_rest', api_views.get_reviews_list),
    path(r'api/dealership', api_views.get_dealership_with_state),
    path(r'api/review', api_views.get_review_with_dealer_id),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
