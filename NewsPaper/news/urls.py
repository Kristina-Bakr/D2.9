from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('<int:pk>/add_subscribe/', add_subscribe, name='add_subscribe'),
    path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),
]