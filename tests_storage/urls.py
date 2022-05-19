from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('tests', views.ReadTestsList)

urlpatterns = [
    path('sections', views.sections_list),
]
urlpatterns += router.urls
