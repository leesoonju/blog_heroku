from django.contrib import admin

# migrate 하고 나서 admin 사이트한테도 데이터 알려주기
from .models import Portfolio  # 같은 폴더에 있는 models 로부터 Portfolio 클래스를 임포트

admin.site.register(Portfolio) # 어드민 사이트에 등록해라