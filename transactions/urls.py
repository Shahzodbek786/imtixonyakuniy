from django.urls import path
from . import views

urlpatterns = [

    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:pk>/', views.delete_transaction, name='delete_transaction'),

]