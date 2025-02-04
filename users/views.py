import re 
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.forms import LogMessageForm
from users.models import LogMessage
from django.views.generic import ListView

def log_message(request):
    form = LogMessageForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "users/log_message.html", {"form": form})

class HomeListView(ListView):
    """Renders the home page with a list of all messages."""
    model = LogMessage
    
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
    

def about(request):
    return render(request, "users/about.html")

def contact(request):
    return render(request, "users/contact.html")

def hello_there(request, name):
    return render(
        request,
        "users/hello_there.html",
        {
            "name": name,
            "date": datetime.now()
        }
    )