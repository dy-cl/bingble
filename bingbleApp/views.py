from django.shortcuts import render, redirect
from .forms import PostForm, ProfilePictureForm
from .models import Post

########################################################################################################
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
########################################################################################################
def home(request):
    posts = posts = Post.objects.order_by('-timestamp')  # Fetch all posts from the database

    user = request.user

    profile_picture = None
    if user.is_authenticated:
        profile_picture = user.profile_picture


    context = {
        'posts': posts,
        'user': user,
        'profile_picture': profile_picture,
    }

    return render(request, 'home.html', context)
########################################################################################################
def profile(request):
    user = request.user
    profile_picture = user.profile_picture
    print(profile_picture)

    context = {
        'user': user,
        'profile_picture': profile_picture,
    }

    # Additional logic to fetch and pass relevant profile data
    return render(request, 'profile.html', context)
########################################################################################################
def update_profile_picture(request):
    user = request.user
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=user)
    return render(request, 'update_profile_picture.html', {'form': form})
########################################################################################################