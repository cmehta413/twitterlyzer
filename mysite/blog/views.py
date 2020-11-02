from django.shortcuts import render

# Create your views here.

from .models import Post
from django.views import generic

from .forms import CommentForm
from django.shortcuts import get_object_or_404

# only post with status published showed at front end of blog, blog posts sorted by creation date
class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on') # dash before created_on means latest post at top
	template_name = 'index.html'

'''
class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'
'''

def post_detail(request, slug):
    template_name = "post_detail.html" # assign html template to template_name
    post = get_object_or_404(Post, slug=slug) # assign post object to post variable
    comments = post.comments.filter(active=True).order_by("-created_on") # queryset
    new_comment = None # page to create new comments, so start new_comment as None

    if request.method == "POST": # if post request is made
        comment_form = CommentForm(data=request.POST) # get user input
        if comment_form.is_valid(): # if user input is valid
            new_comment = comment_form.save(commit=False) # create new comment object
            new_comment.post = post # assign comment object to current post
            new_comment.save() # save object to database
    else: #if the request.method is GET
        comment_form = CommentForm() # initialize form object, pass to template

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )