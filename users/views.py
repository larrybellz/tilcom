from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib import messages 
from django.contrib.auth import login


# Create your views here.
def register(request):
    
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            username=form.cleaned_data.get('username')
            messages.success(request, f"Account for {username} successfully created")
            return redirect ('notesapp-home')

    else:
        form=NewUserForm()

    return render(request,"users/createuser.html",{'form':form})
