from django.urls import path

from .views import UserList, UserDetail, PostList, PostDetail


urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]
