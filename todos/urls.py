from django.urls import path
from . import views 

urlpatterns =[
    path('list/',views.list_todo_items),
    path('insert_todo/', views.insert_todo_item,name='insert_todo_item')
]