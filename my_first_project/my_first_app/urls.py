from django.http import HttpResponse
from django.urls import path
from .views import my_test_view, my_view, CarLiisView
urlpatterns = [

    path('listado/', my_view),
    path('listado/', CarLiisView.as_view()),
    path('detalle/<int:id>', my_test_view),
    path('marcas/<str:brand>', my_test_view)

]
