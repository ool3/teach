from django.shortcuts import render
from django.views.generic import ListView
from .models import List, Book
# Create your views here.
class BookListView(ListView):
	model = Book

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['all'] = List.objects.all()
		data['books'] = Book.objects.all()

		return data