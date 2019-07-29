# class와 함수 만들어주고 
# url을 타고 들어온 파일이 데이터베이스에 저장되도록, 데이터베이스가 데이터 알아듣도록 migration 해주기
from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
