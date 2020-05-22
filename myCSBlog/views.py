from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create postList view
def postList(request):

    posts = posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # query DB for post objects, ordered by published date

    return render(request, 'CS_BSc_Yr1_bridging_coursework/post-list.html', {'posts' : posts }) # Render HTML for the Post List page, parsing posts query results
