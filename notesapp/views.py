from audioop import reverse
from dataclasses import fields
import re
from sre_constants import SUCCESS
from symtable import Class
from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import note,user
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView,UpdateView
from django.template import loader

# Create your views here.
# def home(request):
#     context={
#         'notes': note.objects.all()
#     }
#     mynote=note()
#     if request.method=='POST':
#         if request.POST.get('title') and request.POST.get('content'):
          
#             mynote.title=request.POST.get('title') 
#             mynote.content=request.POST.get('content')
#             mynote.save()
#             return HttpResponseRedirect(request.path_info)

#     else:
#         return render(request,'notesapp/home.html',context)

#this view is working as expected
class NotesListView(ListView):#view to view notes
    model=note #select the model to  use
    template_name = 'notesapp/home.html'  #select the template to use
    context_object_name='notes' #change the variable it loop over in our template since by default it uses object_list
    ordering=['-pk']

    def post(self,request):

        mynote=note()
        if request.method=='POST':
            if request.POST.get('title') and request.POST.get('content'):
            
                mynote.title=request.POST.get('title') 
                mynote.content=request.POST.get('content')
                mynote.save()
                return HttpResponseRedirect(request.path_info)
            else:
                return render(request,'notesapp/home.html')
      





#this view is for showing the data we have saved in our database
class NotesDetailView(DetailView):
    model=note
    template_name = 'notesapp/detail.html'

    ordering=['-pk']

#display the side bar elements  
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['other_objects']=note.objects.all()
        return context 
    

class NotesUpdateView(UpdateView):
    model= note #specify the database model to use
    template_name='notesapp/update.html'#specify the template to render
    fields=[
         'title',
         'content'
     ]
  

def about(request):
    context={
        'notes': note.objects.all()
    }

    return render(request,'notesapp/about.html',context)

# def notes(request):
#     if request.method=='POST':
#         if request.POST.get('title') and request.POST.get('content'):
#             mynote=note()
#             mynote.title=request.POST.get('title') 
#             mynote.content=request.POST.get('content')
#             mynote.save()
#             return render(request, 'notesapp/home.html')

#     else:
#             return render(request, 'notesapp/addnote.html')


def login(request):
    if request.method=="POST":
        if request.POST.get("username") and request.POST.get("password"):
            newuser=user()
            newuser.username= request.POST.get("username")
            newuser.password= request.POST.get("password")
            newuser.save()
            return render(request,'notesapp/applogin.html')

    return render(request,'notesapp/applogin.html')




# def update(request, id):
#     mynote = note.objects.get(id=id)
#     template = loader.get_template('update.html')
#     context = {
#         'mynote': mynote,
#     }
#     return HttpResponse(template.render(context, request))



          
        

