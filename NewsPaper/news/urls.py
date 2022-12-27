from django.urls import path
from .views import (
   PostList, PostDetail, PostCreate, PostUpdate, PostDelete,PostCreateArticles, PostDeleteArticles, PostUpdateArticles
)

urlpatterns = [
   path('', PostList.as_view(), name="post_list"),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostList.as_view(), name='post_list'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('create2/', PostCreateArticles.as_view(), name='post_createarticles'),
    path('<int:pk>/delete2/', PostDeleteArticles.as_view(), name='post_deletearticles'),
    path('<int:pk>/edit2/', PostUpdateArticles.as_view(), name='post_editarticles'),
]