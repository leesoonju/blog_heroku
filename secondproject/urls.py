from django.contrib import admin
from django.urls import path, include
import blog.views
import port.views
from django.conf import settings
# django configuration으로부터 settings.py 를 import/ 외우기....ㅎ
from django.conf.urls.static import static # 외우기....ㅎ


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')), # blog.urls로부터 include해와서 blog/뒤에 쓰겠다 
    # path('blog/<int:blog_id>',blog.views.detail, name="detail"),
    # path('blog/new', blog.views.new, name="new"),
    # path('blog/create', blog.views.create, name="create"), # new.html에서 form action의 경로로 create라는 url을 새로 만들었음
                                                             #blog/create 경로로 가면 views안에 있는 create함수를 실행해라
                                                             #url을 추가해줬다, 즉 path를 추가해줬다고 해서 반드시 html띄워야 되는 거는 아님
    path('portfolio/', port.views.portfolio, name="portfolio"),
    path('account', include('account.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEFIA_ROOT)
# 위에 지우고 이런 식으로 해도 됨
