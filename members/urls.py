from django.conf.urls import url

from members.views import MemberTypeListAPIView, MemberListAPIView, MemberCreateAPIView, MemberDetailAPIView, \
    MemberUpdateAPIView, MemberTitleListAPIView

urlpatterns = [

    url(r'^$', MemberListAPIView.as_view()),
    url(r'^create/$', MemberCreateAPIView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', MemberDetailAPIView.as_view()),
    url(r'^(?P<pk>[0-9]+)/edit/$', MemberUpdateAPIView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$', MemberUpdateAPIView.as_view()),

    url(r'^types/$', MemberTypeListAPIView.as_view()),
    url(r'^titles/$', MemberTitleListAPIView.as_view()),
]