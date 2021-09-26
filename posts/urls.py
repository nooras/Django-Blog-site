from django.contrib import admin
from django.urls import path, include
# from posts import views as post_home
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete
)

app_name="posts"


urlpatterns = [
    path('', post_list, name="home"),
    path("create/", post_create),
    path("detail/<id>/", post_detail, name="detail"),
    path("update/<id>/", post_update, name="update"),
    path("delete/<id>/", post_delete),
]