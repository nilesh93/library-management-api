from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from books.models import BookDetail
from books.serializers.CategorySerializers import CategorySerializer
from books.serializers.CopySerializers import CopySerializer


class BookDetailSerializer(ModelSerializer):
    category = CategorySerializer(many=False, read_only=False)
    copies = CopySerializer(source='get_copies', many=True, read_only=True)
    total_copies = IntegerField(source='count_copies', read_only=True)
    available_copies = IntegerField(source='count_available_copies', read_only=True)
    taken_copies = IntegerField(source='count_taken_copies',read_only=True)

    class Meta:
        model = BookDetail
        fields = "__all__"


class BookListSerializer(ModelSerializer):
    total_copies = IntegerField(source='count_copies', read_only=True)
    available_copies = IntegerField(source='count_available_copies', read_only=True)

    class Meta:
        model = BookDetail
        fields = ("id", "title", "author", "editor", "publisher", "cl_num", "total_copies", "available_copies")


class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = BookDetail
        fields = "__all__"
