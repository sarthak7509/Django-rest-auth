from django.urls import path,include
from rest_framework import routers
from .views import MedFed

router = routers.DefaultRouter()
router.register('fed',MedFed)

urlpatterns = [
    path('',include(router.urls))
]
