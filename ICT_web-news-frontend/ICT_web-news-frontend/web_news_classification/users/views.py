from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if the form is meet the requirement to create a user,
        # save the user infomation to the database.
        # redirect to the login page
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'Users/register.html', {'form': form})


