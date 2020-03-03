from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addTodo,name='add'),
    path('complete/<int:todo_id>',views.completedTodo,name='complete'),
    path('deleteCompleted',views.deleteCompletedTodo,name='deleteCompleted'),
    path('deleteAll',views.deleteAll,name='deleteAll'),
    path('search',views.search,name='search'),
]