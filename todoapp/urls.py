from .import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('delete/<int:task_id>',views.delete_task,name = 'delete_task')
    
]