from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # re_path(r'^books/(?P<date_string>[-\d]+)/$', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # path('authors/', views.AuthorListView.as_view(), name='author-list'),
    # path('authors/<id>/', views.AuthorDetailView.as_view, name='author-detail')
]