from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from django.db.models.query_utils import Q

from django.urls import reverse_lazy

from .models import Story

class StoryListView(LoginRequiredMixin, ListView):
	model = Story
	template_name = 'home.html'
	context_object_name = 'storylist'
	login_url='login'

class StoryDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
	model = Story
	template_name = 'story.html'
	permission_required = 'Story.special_access'

class AddstoryView(LoginRequiredMixin,CreateView):
	model = Story
	template_name = 'addstory.html'
	fields = ['name','author','release_year','genre','cover''story',]
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class EditstoryView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Story
	template_name = 'editstory.html'
	fields = ['name','author','release_year','genre','cover''story',]
	
	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user

class DeletestoryView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Story
	template_name = 'deletestory.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user


class SearchStoryView(LoginRequiredMixin,ListView):
	model = Story
	template_name = 'search.html'
	context_object_name = 'searchstorylist'

	def get_queryset(self):
		query = self.request.GET['name']
		return Story.objects.filter(name__contains=query)

