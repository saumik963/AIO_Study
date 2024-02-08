from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from .models import Post,PostImages,Comments
from .forms import PostForm,PostImagesForm
from django.contrib import messages
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

=======
from .models import Post,PostImages
from .forms import PostForm,PostImagesForm
from django.contrib import messages
import os
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47



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
<<<<<<< HEAD
    comments= Comments.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments
=======

    context = {
        'post': post,
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47
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


<<<<<<< HEAD


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    previous_image_path = None

    if post.Coverimage:
        previous_image_path = post.Coverimage.path

=======
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    # print("==>> ", post.Coverimage.path)
    previous_image_path = None

    if post.Coverimage.path:
        previous_image_path = post.Coverimage.path


>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
<<<<<<< HEAD
            new_image_uploaded = 'Coverimage' in request.FILES

            if new_image_uploaded:
                if previous_image_path:
                    os.remove(previous_image_path)
                else:
                    print(f"File not found at: {previous_image_path}")

            form.save()
=======
            if len(previous_image_path) >0:
                os.remove(previous_image_path)
            else:
                print(f"File not found at: {previous_image_path}")

            form.save()
            
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47
            messages.success(request, 'Post updated successfully.')
            return redirect('profile')
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'edit_post.html', context)

<<<<<<< HEAD

class Comment(LoginRequiredMixin,CreateView):
    model = Comments
    fields = ['review']

    def form_valid(self, form):

        post = get_object_or_404(Post, id=self.kwargs['id'])
        form.instance.post = post
        form.instance.user = self.request.user
        messages.success(self.request, "Comment successfully")
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'id': self.kwargs['id']})
    


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comments
    context_object_name = 'comment'
    template_name = 'comments_confirm_delete.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def get_success_url(self):
        comment = self.get_object()
        post_id = comment.post.id
        return reverse_lazy('post_detail', kwargs={'id': post_id})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Comment deleted successfully.")
        return super().delete(request, *args, **kwargs)
=======
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47
