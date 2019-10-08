from django.shortcuts import render, redirect

from .forms import UserCreationForm

from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'تهانينا  {} لقد تمت عملية التسجيل بنجاح'.format(username))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'title': 'التسجيل', 'form': form,})


def login(request):
    pass