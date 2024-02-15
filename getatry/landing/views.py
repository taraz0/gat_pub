from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pyth import my_function
import pyth

from django.http import HttpResponse

def index(request):
    return render(request, 'landing/index.html')

def page_a(request):
    return render(request, 'landing/page_a.html')

@login_required
def features_page(request):
    context = {}
    if request.method == 'POST':
        if 'button1' in request.POST:
            context['output'] = pyth.my_function()
        elif 'button2' in request.POST:
            context['output'] = pyth.my_function()
        elif 'button3' in request.POST:
            context['output'] = pyth.my_function()

    return render(request, 'landing/features_page.html', context)

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after signup
    template_name = 'registration/signup.html'
