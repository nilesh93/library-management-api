from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework_filters.backends import DjangoFilterBackend

from members.filters import MemberFilter
from members.models import MemberType, Member, MemberTitle
from members.serializers import CategorySerializer, MemberListSerializer, MemberCreateSerializer, MemberDetailSerializer, \
    TitleSerializer


class MemberTypeListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = MemberType.objects.all()


class MemberTitleListAPIView(ListAPIView):
    serializer_class = TitleSerializer
    queryset = MemberTitle.objects.all()


class MemberListAPIView(ListAPIView):
    serializer_class = MemberListSerializer
    queryset = Member.active_objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = MemberFilter


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberCreateSerializer
    queryset = Member.objects.all()


class MemberDetailAPIView(RetrieveAPIView):
    serializer_class = MemberDetailSerializer
    queryset = Member.objects.all()


class MemberUpdateAPIView(UpdateAPIView):
    serializer_class = MemberCreateSerializer
    queryset = Member.objects.all()
