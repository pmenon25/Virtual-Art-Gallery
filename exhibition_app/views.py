from .forms import ArtForm
from django.shortcuts import render, redirect
from exhibition_app.models import Exhibition, Art, Comment, Like
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from .forms import CommentForm  
import uuid
import boto3
S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'exhibitionart'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def info(request):
  return render(request, 'about.html')

def artist(request):
  exhibition = Exhibition.objects.all()
  return render(request, 'artist.html' , {'exhibition' : exhibition})

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
  comment_form = CommentForm()
  art_form = ArtForm()
  return render(request , 'exhibition/details.html' , {'exhibition' : exhibition, 'art_form' : art_form, 'comment_form': comment_form})

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
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/exhibition')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

#Comment view functions
def create_comment(request, exhibition_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.exhibition_id = exhibition_id
    new_comment.save()
  return redirect('details', exhibition_id=exhibition_id)

def delete_comment(request, comment_id):
  delete = Comment.objects.get(id=comment_id)
  delete.delete()
  return redirect(f'/exhibition/{delete.exhibition.id}')

def edit_comment(request, comment_id): 
  result = Comment.objects.get(id=comment_id)
  return render(request , 'comment/update.html' , {'comment':result})

# Art views functions
def add_art(request, exhibition_id):
  form = ArtForm(request.POST) 
  print(form.errors)
  if form.is_valid():
    print('hello')
    new_art = form.save(commit=False)
    photo_file = request.FILES.get('image', None)   
    print(photo_file)
    if photo_file:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      print("key:" ,key)
      s3.upload_fileobj(photo_file, BUCKET, key)
    new_art.exhibition_id = exhibition_id
    new_art.save()
    print

  return redirect('details', exhibition_id=exhibition_id)

def delete_art(request , art_id):
  result = Art.objects.get(id=art_id)
  result.delete()
  return redirect(f'/exhibition/{result.exhibition.id}') 

def edit_art(request, art_id):
  result = Art.objects.get(id=art_id)
  return render(request , 'art/update.html' , {'art':result})

def update_art(request , art_id):
  art = Art.objects.get(id=art_id)
  art.name = request.POST['name']
  art.description = request.POST['description']
  art.exhibition_id = art.exhibition_id
  print(art.exhibition_id)
  art.save()
  return redirect(f'/exhibition/{art.exhibition_id}')

# def add_photo(request, art_id , exhibition_id):
#     photo_file = request.FILES.get('photo-file', None)
#     print('works!  - 1', photo_file)
#     if photo_file:
#         s3 = boto3.client('s3')
#         print('works - 2! ', s3)
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         print('works! - 3 ', key)
#         s3.upload_fileobj(photo_file, BUCKET, key)
#         print('works! -4 ')
#         Photo.objects.create(
#             url= f"{S3_BASE_URL}{BUCKET}/{key}",
#             art=art_id
#             )
#         print(art_id)
#     return redirect(f'/exhibition/{exhibition_id}')
 
