from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['count'] = 0
    return render(request, "index.html")
    
def random_word(request):
    request.session['count'] += 1
    request.session['random_word'] = get_random_string(14)
    return render(request, "random_word.html")

def reset(request):
    request.session.flush()
    return redirect('/')