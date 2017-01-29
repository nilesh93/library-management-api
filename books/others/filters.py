import rest_framework_filters as filters
from books.models import BookDetail, BookCopy


# from rest_framework_filters.filters import RelatedFilter

class BookFilter(filters.FilterSet):
    class Meta:
        model = BookDetail
        fields = {
            'title': ['istartswith'],
            'author': ['istartswith'],
            'editor': ['istartswith'],
            'publisher': ['istartswith'],
            'cl_num': ['startswith']
        }


class CopyFilter(filters.FilterSet):
    # book_detail = RelatedFilter(BookFilter, queryset=BookDetail.objects.all())

    class Meta:
        model = BookCopy
        fields = {
            'ref_id': ['istartswith']
        }
