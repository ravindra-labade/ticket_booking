from django.urls import path
from .views import add_ticket, show_ticket, update_ticket, cancel_ticket

urlpatterns = [
    path('add/', add_ticket, name='add_url'),
    path('show/', show_ticket, name='show_url'),
    path('update/<int:pk>/', update_ticket, name='update_url'),
    path('cancel/<int:pk>/', cancel_ticket, name='cancel_url'),

]
