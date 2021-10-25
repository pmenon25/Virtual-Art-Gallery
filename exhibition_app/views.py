from django.shortcuts import render, redirect
from exhibition_app.models import Exhibition, Art 
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
  return render(request , 'exhibition/profile.html' , {'exhibition' : exhibition})
  
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

def details_exhibition(request , exhibition_id):
  exhibition = Exhibition.objects.get(id=exhibition_id)
  return render(request , 'exhibition/details.html' , {'exhibition' : exhibition})

def delete_exhibition(request , exhibition_id):
  result = Exhibition.objects.get(id=exhibition_id)
  result.delete()
  return redirect('/exhibition') 

def edit_exhibition(request, exhibition_id):
  result = Exhibition.objects.get(id=exhibition_id)
  print('date:',result.date)
  return render(request , 'exhibition/update.html' , {'exhibition':result})

def update_exhibition(request , exhibition_id):
  exhibition = Exhibition.objects.get(id=exhibition_id)
  exhibition.title = request.POST['title']
  exhibition.artist_name = request.POST['artist_name']
  exhibition.description = request.POST['description']
  exhibition.date = request.POST['date']
  exhibition.user_id = request.user.id
  exhibition.save()
  return redirect('/exhibition')

# Signup function
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

# Art views functions
def new_art(request):
  return render (request , 'exhibition/create.html')

def create_art(request):
  Art.objects.create(
    name = request.POST['name'],
    description = request.POST['description'],
    exhibition_id = request.exhibition.id,
    art_img = request.POST['art_img']
  )
  return redirect('/exhibition')