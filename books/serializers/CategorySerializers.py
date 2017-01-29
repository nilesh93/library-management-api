from rest_framework.serializers import ModelSerializer
from books.models import BookCategory


class CategorySerializer(ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ("id", "cat_name")
