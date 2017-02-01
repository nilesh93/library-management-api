import rest_framework_filters as filters
from members.models import Member


class MemberFilter(filters.FilterSet):
    class Meta:
        model = Member
        fields = {
            'name': ['istartswith'],
            'nic': ['istartswith'],
            'mobile': ['istartswith'],
            'ref_id': ['istartswith']
        }
