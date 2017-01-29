from rest_framework.serializers import ModelSerializer
from books.models import BookCopy, BookDetail
from books.serializers.CategorySerializers import CategorySerializer


class BookDetailForCopiesSerializer(ModelSerializer):
    category = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = BookDetail
        fields = "__all__"


class CopySerializer(ModelSerializer):
    class Meta:
        model = BookCopy
        fields = "__all__"


class CopyViewSerializer(ModelSerializer):
    book_detail = BookDetailForCopiesSerializer(many=False, read_only=True)

    class Meta:
        model = BookCopy
        fields = "__all__"
