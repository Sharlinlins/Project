from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm, AddCategoryForm
from django.urls import reverse_lazy, reverse

def index(request):
    return render(request, 'index.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked  = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']
    # ordering = ['-id']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categorylist.html',{'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',{'cats':cats.title(), 'category_posts': category_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'addcategory.html'
    # fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editpost.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    # form_class = EditForm
    template_name = 'deletepost.html'
    # fields = ['title', 'title_tag', 'body']
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'addcomment.html'
    success_url = reverse_lazy('home')
    ordering = ['-date_added']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)