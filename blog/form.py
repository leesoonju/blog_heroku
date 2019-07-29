from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):  
    class Meta:                       # 메타클래스(클래스 안에 있는 클래스)
        model = Blog                  # 어떤 모델을 기반으로 할거냐 -> Blog 모델을 기반으로 할거다
        fields = ['title', 'body']    # 어떤 항목들을 입력받을거냐 -> title과 body를 입력받을거다


# 이 방식으로도 만들 수 있음!
# class BlogPost(forms.Form):
    # email = forms.EmailField()
    # files = forms.FileField()
    # url = forms.URLField()
    # words = forms.CharField(max_length=200)
    # max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')]) # choicefield는 선택 가능한 항목이 생김
    
