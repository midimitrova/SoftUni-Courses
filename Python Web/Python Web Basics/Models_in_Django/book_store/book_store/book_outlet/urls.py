from django.urls import path

from book_store.book_outlet.views import index, book_detail

urlpatterns = (
    path('', index, name='index'),
    path('<slug:slug>/', book_detail, name='book-detail'),
)