from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .tasks import send_new_mail


class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'text'
    context_object_name = 'posts'
    template_name = 'news.html'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

    def form_valid(self, form):
        Post = form.save(commit=True)
        Post.categoryType = 'NW'
        send_new_mail.delay()
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
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


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    queryset = Post.objects.order_by('-dateCreation')
    context_object_name = 'post'
    paginate_by = 3

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'news/category_list.html'
    context_object_name = 'Сategory'


@login_required
def add_subscribe(request, pk):
    Category.objects.get(id=pk).subscribers.add(request.user)
    message = 'Вы успешно подписались '
    return redirect((request, 'sub.html', {'category': Category.objects.get(id=pk), 'message': message}))


@login_required
def del_subscribe(request, pk):
    Category.objects.get(id=pk).subscribers.remove(request.user)
    return redirect('/news/')