from django.conf.urls import url
from books.views.BookViews import BookListAPIView, BookCreateAPIView, BookDetailAPIView, BookUpdateAPIView, \
    CategoryListAPIView
from books.views.CopyViews import CopyDetailAPIView, CopyListAPIView, CopyDestroyAPIView, CopyUpdateAPIView, \
    CopyCreateAPIView

app_name = 'books'

urlpatterns = [

    url(r'^$', BookListAPIView.as_view()),
    url(r'^create/$', BookCreateAPIView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', BookDetailAPIView.as_view()),
    url(r'^(?P<pk>[0-9]+)/edit/$', BookUpdateAPIView.as_view()),

    url(r'^copy/$', CopyListAPIView.as_view()),
    url(r'^copy/create/$', CopyCreateAPIView.as_view()),
    url(r'^copy/(?P<pk>[0-9]+)/$', CopyDetailAPIView.as_view()),
    url(r'^copy/(?P<pk>[0-9]+)/edit/$', CopyUpdateAPIView.as_view()),
    url(r'^copy/(?P<pk>[0-9]+)/delete/$', CopyDestroyAPIView.as_view()),

    url(r'^categories/$', CategoryListAPIView.as_view()),

]
