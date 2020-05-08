from django.urls import path
from . import views

#posts urls
app_name = 'posts'
urlpatterns = [
    path('signup/',views.UserCreateView.as_view(),name='signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout, name='logout'),
    path('<int:pk>/detail/',views.UserDetailView.as_view(),name='detail'),
    path('<int:pk>/create-image/',views.SelectImage.as_view(),name='image-create'),
    path('<int:pk>/create-post/',views.CreatePost.as_view(),name='post-create'),
    path('<int:pk>/post',views.PostDetail.as_view(),name='post'),
    path('list/',views.PostList.as_view(),name='list'),
    # path('<int:pk>/view/',views.PostDetail.as_view(),name='post_detail'),
]
