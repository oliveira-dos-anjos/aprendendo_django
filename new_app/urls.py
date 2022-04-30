from django.urls import path

from . import views

app_name = "new_app"


urlpatterns = [
    path('', views.PostListView.as_view(), name= 'new_app'),
    path('<slug:slug>', views.PostDetailView.as_view(), name= 'detail'),
]
