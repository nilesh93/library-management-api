from django.contrib import admin
from .models import BookCopy, BookDetail, BookCategory
# Register your models here.

admin.site.register(BookCopy)
admin.site.register(BookDetail)
admin.site.register(BookCategory)
