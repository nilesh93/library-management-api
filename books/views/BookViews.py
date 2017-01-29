from rest_framework_filters.backends import DjangoFilterBackend
from books.models import BookDetail, BookCategory
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from books.others.filters import BookFilter
from books.serializers.BookSerializers import BookListSerializer, BookCreateSerializer, BookDetailSerializer
from books.serializers.CategorySerializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = BookCategory.objects.all()


class BookListAPIView(ListAPIView):
    serializer_class = BookListSerializer
    queryset = BookDetail.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = BookFilter


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookCreateSerializer
    queryset = BookDetail.objects.all()


class BookUpdateAPIView(UpdateAPIView):
    serializer_class = BookCreateSerializer
    queryset = BookDetail.objects.all()


class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
