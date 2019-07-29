from django.shortcuts import render
from .models import Portfolio 

def portfolio(request):
    portfolios = Portfolio.objects #portfolio라는 변수 안에 Portfolio 클래스를 통해 만든 객체들 담기
    return render(request, 'portfolio.html', {'portfolios': portfolios})

