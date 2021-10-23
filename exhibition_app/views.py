from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def info(request):
  return render(request, 'info.html')

def artist(request):
  return render(request, 'artist.html')

# Exhibition view functions

def create_exhibition(request):

  return render(request , 'exhibition/create.html')
  