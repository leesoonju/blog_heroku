from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# 장고의 contribution에서 authorization(계정 권한에 대한 내용)의 모델에서 User라는 class를 가져와라
from django.contrib import auth

def signup(request):
    if request.method == 'POST': 
    # signup.html에서 POST방식으로 request가 들어온다면 (=signup.html에서 회원가입 버튼을 누른다면)
        if request.POST['password1'] == request.POST["password2"]:        
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            # user라는 변수에 User클래스의 쿼리셋 메소드의 create_user함수써서 담을 거임, 함수에 넣는 인자는 뒤에 오는 두 가지 애들
            auth.login(request, user)
            # auth.login은 로그인해주는 함수(auth임포트 해온 거에 들어있음)/ 뒤에 쓴 user는 방금 User.objects.~~써서 만든 변수
            return redirect('/')
    return render(request, 'signup.html')
    # request.method != 'POST'라면 다시 html띄워주라

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        # auth.authenticate 는 진짜 등록된 회원이 맞는지 확인해주는 함수
        # 그 결과를 user에 담아줌 -> 회원 정보가 없다면 user변수 안에는 None이 담김
        if user is not None: 
        # 이미 존재하는 회원이라면
            auth.login(request, user)
            return redirect('home')
        else: 
        # 이미 존재하는 회원이 아니라면
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':     # 로그아웃 버튼을 누른다면
        auth.logout(request)         # 로그아웃 시켜주는 함수 실행
        return redirect('home')
    return render(request, 'login.html') # requset가 제대로 들어오지 않았으면 login.html로 가라

