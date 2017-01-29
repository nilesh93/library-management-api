from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination


class PostLimitOffsetPagination(LimitOffsetPagination):
    default = 2
    max_limit = 10


