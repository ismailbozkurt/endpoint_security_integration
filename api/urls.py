from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.ProductAPIView.as_view()),
    path("integration/<str:product>", views.IntegrationAPIView.as_view()),
]
