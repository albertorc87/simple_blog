from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Models
from posts.models import Post
from categories.models import Category
from comments.models import Comment

# Forms
from comments.forms import CreateCommentForm


class PostsFeedView(ListView):
    """Index."""
    template_name = 'posts/index.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_draft=False)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    
class PostDetailView(DetailView):
    """Detail post."""
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'


    def get_queryset(self):
        return Post.objects.filter(is_draft=False)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post=self.get_object()).all()
        context['form_comments'] = CreateCommentForm()
        return context


@login_required
def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.id,
            'profile': request.user.id,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', url=url)
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)
    