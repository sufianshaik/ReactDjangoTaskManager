from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

# create api

class List_of_Todo(ListAPIView) :
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer