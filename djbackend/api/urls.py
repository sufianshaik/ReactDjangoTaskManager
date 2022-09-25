from django.urls import path
from api import views

urlpatterns = [
    path('todo/',views.List_of_Todo.as_view()),

]