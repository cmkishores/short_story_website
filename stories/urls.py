from django.urls import path
import stripe
from .views import StoryListView,StoryDetailView,EditStoryView,DeleteStoryView,SearchStoryView,AddStoryView,charge


urlpatterns= [
	path('',StoryListView.as_view(),name='home'),
	path('<int:pk>/',StoryDetailView.as_view(),name='story'),
	path('new/', AddStoryView.as_view(),name='addstory'),
	path('<int:pk>/edit',EditStoryView.as_view(),name='editstory'),
	path('<int:pk>/delete/',DeleteStoryView.as_view(),name='deletestory'),
	path('search/', SearchStoryView.as_view(),name='search'),
	path('done/', charge, name='done'),
]