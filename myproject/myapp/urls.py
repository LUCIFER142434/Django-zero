from django.urls import path
from .views import create,list,update

urlpatterns = [
    path('create/',create,name='create'),
    path('',list,name='list'),
    path('update/<int:pr_id>/',update,name='update')
]