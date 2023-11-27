from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,PostImages
from .forms import PostForm,PostImagesForm
from django.contrib import messages
import os



def User_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        images_form = PostImagesForm(request.POST, request.FILES)
        if form.is_valid() and images_form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            images = request.FILES.getlist('images')
            for image in images:
                PostImages.objects.create(post=post, images=image)

            messages.success(request, 'Post published successfully.')
            return redirect('Post')
        else:
            # Handle form validation errors here
            pass
    else:
        form = PostForm()
        images_form = PostImagesForm()

    context = {
        "form": form,
        "images_form": images_form,
    }
    return render(request, 'post.html', context)



# def User_post(request):
#     if request.method == "POST":
#         post = Post()
#         post.PostTitle = request.POST.get("PostTitle")
#         post.Description = request.POST.get("Description")
#         post.is_post = request.POST.get("is_post")

#         if len(request.FILES) != 0:
#             post.image = request.FILES("image")

#             post.save()
#             messages.success(request, 'Posted successfully.')
#             return redirect("Post")

#     return render(request, 'post.html')


def View_posts(request):
    posts = Post.objects.filter(is_post=True)

    if request.method == "GET":
        sp = request.GET.get('searchPost')
        if sp != None:
            posts = Post.objects.filter(PostTitle__icontains=sp, is_post=True)

    paginator = Paginator(posts, 12)  # Show num of contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        "post_act": "active",
    }

    return render(request, 'posts.html', context)


def post_detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail_post.html', context)


def public(request, id):
    post = Post.objects.get(id=id)
    if post.is_post == False:
        post.is_post = True
    else:
        post.is_post = False

    post.save()
    return redirect('profile')


def DeletePost(request, id):
    post = Post.objects.get(pk=id).delete()
    return redirect('profile')


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    # print("==>> ", post.Coverimage.path)
    previous_image_path = None

    if post.Coverimage.path:
        previous_image_path = post.Coverimage.path


    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            if len(previous_image_path) >0:
                os.remove(previous_image_path)
            else:
                print(f"File not found at: {previous_image_path}")

            form.save()
            
            messages.success(request, 'Post updated successfully.')
            return redirect('profile')
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'edit_post.html', context)

