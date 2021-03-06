from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user_registration.forms import LoginForm


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

    def singup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'registration/signup.htm', {'form': form})

    class SignUp(generic.CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'signup.html'
