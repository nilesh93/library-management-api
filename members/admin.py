from django.contrib import admin

from members.models import MemberType, Member, MemberTitle

admin.site.register(MemberType)
admin.site.register(Member)
admin.site.register(MemberTitle)
