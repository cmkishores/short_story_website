from django.urls import path
from .views import OrdersView,charge

urlpatterns = [
	path('',OrdersView.as_view(),name='orders'),
	path('done/', charge, name='done'),
]