from django.urls import path
from .views import IndexView, DeleteTodo, CompleteTodo, UpdateTodo

app_name = 'todos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo/<id>/delete/', DeleteTodo.as_view(), name='delete'),
    path('todo/<id>/complete/', CompleteTodo.as_view(), name='complete'),
    path('todo/<id>/update/', UpdateTodo.as_view(), name='update')
]
