from django.urls import path
from logs import views

urlpatterns = [
     path('add/', views.show_form, name="show-form")
]
