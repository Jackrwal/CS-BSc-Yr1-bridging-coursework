from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create postList view
def postList(request):

    # Get list of posts
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')  # query DB for post objects, ordered by published date

    # return HTML doc (query results will be used building template into HTML)
    return render(request, 'myCSBlog/post-list.html', {'posts' : posts})

def post(request, pk):

    # select post record by primary key, or return a 404 error if not found
    post = get_object_or_404(Post, pk = pk)

    # return html doc, using query result to render html from post.html template
    return render(request, 'myCSBlog/post.html', {'post' : post})

def newPost(request):

    if request.method == "POST":
        # If the view has been posted a completed form
        response = PostForm(request.POST)

        # validate form
        if response.is_valid():
            # get the new post model object. Do not save it immediately, as there are missing fields
            post = response.save(commit = False)

            # set fields outside of the form
            post.author = request.user
            post.published_date = timezone.now()

            # set post snatch
            if len(post.text) > 500:
                post.snatch = post.text[:247] + "..."
            else:
                post.snatch = post.text

            # save model to db
            post.save()

            # Once Post is saved re-direct to the post detail page
            return redirect('post', pk = post.pk)

        # TODO What happens is the form response is invalid

    # If the form is being requested of the view
    form = PostForm()
    return render(request, 'myCSBlog/post-edit.html', {'form': form})

def editPost(request, pk):

    post = get_object_or_404(Post, pk = pk)

    if request.method == "POST":
        response = PostForm(request.POST, instance = post)

        if response.is_valid():
            post = response.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()

            # set post snatch
            if len(post.text) > 500:
                post.snatch = post.text[:247] + "..."
            else:
                post.snatch = post.text

            post.save()

            return redirect('post', pk = post.pk)

    if request.method == "GET":
        # return the form filled with details from the post object
        form = PostForm(instance = post)
        return render(request, 'myCSBlog/post-edit.html', {'form':form})

def handler404(request, exception):
    return render(request, 'myCSBlog/404.html', status = 404)