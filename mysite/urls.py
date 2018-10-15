# 장고 내장 함수 url() 임포트
from django.conf.urls import url, include  # include('bookmark.urls') 함수
from django.contrib import admin

# URL 패턴에 따라 뷰를 호출할 예정(아직 해당 뷰 코드는 작성 전 상태)
# from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import * # 모든 뷰 항목을 일괄 임포트

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('bookmark.urls')),
    # 원래 있던 내용을 모두 bookmark/urls.py 파일로 옮기자.
]