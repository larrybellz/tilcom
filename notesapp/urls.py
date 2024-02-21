from django.urls import  path
  
from .views import NotesListView, NotesDetailView,NotesUpdateView

urlpatterns=[
    path('',NotesListView.as_view(), name='notesapp-home'),
    path('mynotes/<int:pk>', NotesDetailView.as_view(),name='notes-detail'),
    path('update/<int:pk>',NotesUpdateView.as_view(),name='notes-update'),
   # path('about/',views.about, name='notesapp-about'),
   # path('addnote/',views.notes,name='notesapp-addnote'),
    #path('login/',views.login, name="login"),
  #  path('update/',views.update, name='notesapp-update')
]