from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.api_root),
    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
    path(
        "snippets/<int:pk>/hightlight/",
        views.SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="name-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
