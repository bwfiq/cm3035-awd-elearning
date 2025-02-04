import re 
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")
    
    # # Filter name arg to only letters (using regex)
    # # URL args can contain arbitrary text. Always filter user provided info
    # match_object = re.match("[a-zA-Z]+", name)
    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"
        
    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return HttpResponse(content)
    return render(
        request,
        "users/hello_there.html",
        {
            "name": name,
            "date": datetime.now()
        }
    )