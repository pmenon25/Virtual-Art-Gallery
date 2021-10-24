from django.shortcuts import render,redirect

from exhibition_app.models import Exhibition
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def info(request):
  return render(request, 'info.html')

def artist(request):
  return render(request, 'artist.html')

# Exhibition view functions

def exhibition(request):
  exhibition = Exhibition.objects.filter(user=request.user)
  return render(request , 'exhibition/prof  ile.html' , {'exhibition' : exhibition})
  
def new(request):
  return render (request , 'exhibition/create.html')

def create_exhibition(request):
  Exhibition.objects.create(
    title = request.POST['title'],
    artist_name = request.POST['artist_name'],
    description = request.POST['description'],
    date = request.POST['date'],
    user_id = request.user.id
  )
  return redirect('/exhibition')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/exhibition')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
