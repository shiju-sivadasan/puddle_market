from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.details,name='details')
]