from rest_framework.serializers import ModelSerializer
from members.models import MemberType, Member, MemberTitle


class TitleSerializer(ModelSerializer):
    class Meta:
        model = MemberTitle
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = MemberType
        fields = "__all__"


class MemberListSerializer(ModelSerializer):
    type = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = Member
        fields = ("id", "type", "title", "name", "nic", "ref_id", "registration_status", "registration_expire", "mobile")


class MemberCreateSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class MemberDetailSerializer(ModelSerializer):
    type = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = Member
        fields = "__all__"
