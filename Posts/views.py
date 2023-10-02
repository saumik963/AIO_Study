from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages


def User_post(request):
    if request.method == "POST":
        # Bind the form with POST data and FILES for the image
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            PostTitle = form.cleaned_data['PostTitle']
            Description = form.cleaned_data['Description']
            image = form.cleaned_data['image']
            is_post = form.cleaned_data['is_post']

            # Post.objects.create(
            #     user=request.user, PostTitle=PostTitle, Description=Description, image=image, is_post=is_post)

            Post(user=request.user, PostTitle=PostTitle,
                 Description=Description, image=image, is_post=is_post).save()
            messages.success(request, 'Post published successfully.')

            return redirect('Post')
        else:
            pass
    else:
        form = PostForm()

    context = {
        "form": form,
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

    paginator = Paginator(posts, 3)  # Show num of contacts per page.

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

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PostForm(instance=post)

    # Access and print the values inside taskTitle and taskDescription
    # print("taskTitle:", task.taskTitle)
    # print("taskDescription:", task.taskDescription)

    return render(request, 'edit_post.html', {'form': form, "post": post})
