from django.shortcuts import render

from app1.forms import LoginForm


# Create your views here.
def index(request):
    return render(request, 'app1/index.html', {})


def login(request):
    username = "not logged in"

    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
        else:
            MyLoginForm = LoginForm()

        return render(request, 'registration/login.html', {"usermane": username})
