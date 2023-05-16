from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if the form is meet the requirement to create a user,
        # save the user infomation to the database.
        # redirect to the login page
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        # if the data(username and password) entered by user cannot meet the requirement,
        # the system will display the miss requirement for user to edit the username and password
        form = UserCreationForm()
    return render(request, 'Users/register.html', {'form': form})


