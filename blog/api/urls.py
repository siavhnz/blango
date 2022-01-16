from django.urls import path, include
from blog.api_views import post_list, post_detail

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
  path("posts/", post_list, name="api_post_list"),
  path("posts/<int:pk>", post_detail, name="api_post_detail",)
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    
    path("token-auth/", views.obtain_auth_token)
]