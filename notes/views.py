from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from .models import Note
from .forms import NotesForms

class NotesListView(LoginRequiredMixin ,ListView):
   model = Note
   context_object_name = 'notes'
   template_name = 'notes/notes_list.html'
   login_url = '/login'

   def get_queryset(self):
      return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin, CreateView):
   model = Note
   form_class = NotesForms
   template_name = 'notes/notes_form.html'
   success_url = '/notes'
   login_url = '/login'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())

class NotesDetailView(DetailView):
   model = Note
   context_object_name = 'note'
   template_name = 'notes/notes_detail.html'

class NotesUpdateView(UpdateView):
   model = Note
   success_url = '/notes'
   form_class = NotesForms
   template_name = 'notes/notes_form.html'

class NotesDeleteView(DeleteView):
   model = Note
   context_object_name = 'note'
   success_url = '/notes'
   template_name = 'notes/notes_delete.html'