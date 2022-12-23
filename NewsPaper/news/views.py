from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    ordering = 'text'
    context_object_name = 'posts'
    template_name = 'news.html'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'
    def form_valid(self, form):
        Post = form.save(commit=True)
        Post.categoryType = 'NW'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostCreateArticles(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'
    def form_valid(self, form):
        Post = form.save(commit=True)
        Post.categoryType ='AR'
        return super().form_valid(form)


class PostEditArticles(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class PostDeleteArticles(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')