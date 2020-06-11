from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create postList view
def postList(request):

    # Get list of posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # query DB for post objects, ordered by published date

    # return HTML doc (query results will be used building template into HTML)
    return render(request, 'myCSBlog/post-list.html', {'posts' : posts})

def post(request, pk):

    # select post record by primary key, or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)

    # return html doc, using query result to render html from post.html template
    return render(request, 'myCSBlog/post.html', {'post' : post})

def handler404(request, exception):
    return render(request, 'myCSBlog/404.html', status=404)