from rest_framework_filters.backends import DjangoFilterBackend
from books.models import BookCopy
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from books.others.filters import CopyFilter
from books.serializers.CopySerializers import CopyViewSerializer, CopySerializer


class CopyDetailAPIView(RetrieveAPIView):
    serializer_class = CopyViewSerializer
    queryset = BookCopy.objects.all()


class CopyListAPIView(ListAPIView):
    serializer_class = CopyViewSerializer
    queryset = BookCopy.active_objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = CopyFilter

    def get_queryset(self):
        queryset = BookCopy.active_objects.all()
        book_title = self.request.GET.get('title')
        if book_title is not None:
            queryset = queryset.filter(book_detail__title__istartswith=book_title)
        return queryset


class CopyDestroyAPIView(DestroyAPIView):
    queryset = BookCopy.active_objects.all()
    serializer_class = CopySerializer


class CopyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = BookCopy.active_objects.all()
    serializer_class = CopySerializer


class CopyCreateAPIView(CreateAPIView):
    serializer_class = CopySerializer
    queryset = BookCopy.active_objects.all()
