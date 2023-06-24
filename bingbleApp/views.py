from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def home(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'home.html', {'posts': posts})