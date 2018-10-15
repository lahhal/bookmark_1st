# 장고 내장 함수 url() 임포트
from django.conf.urls import url
from . import views  # views.~ 형식으로 변경해야 함

# from django.contrib import admin
# URL 패턴에 따라 뷰를 호출할 예정(아직 해당 뷰 코드는 작성 전 상태)
# from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import * # 모든 뷰 항목을 일괄 임포트
urlpatterns = [
    # 북마크 앱을 위한 클래스 기반 뷰
    # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
    url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
    url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
    # tabular list
    url(r'^bookmark_t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
    url(r'^bookmark_t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
]