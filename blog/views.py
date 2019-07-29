from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, Page
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects # 클래스이름.objects쓰면 models.py로부터 객체 목록을 전달받을 수 있게 됨 
                         # 쿼리셋 = models.py로부터 전달받은 객체 목록
                         # 메소드 = 쿼리셋을 이용해 데이터베이스로부터 받은 기능들을 표시해줌
                         #       = 쿼리셋 활용할 수 있게 함 (쿼리셋 만들고, 지우고 등등)
                         # 메소드 형식은 -> 모델이름.쿼리셋 -> objects.메소드
                         # home.html에서 blogs.all에는 내가 작성한 모든 블로그 글들이 담김 (.all도 메소드)


    blog_list = Blog.objects.all()       # 블로그의 모든 글들을 대상으로 한다
    paginator = Paginator(blog_list, 3)   # blog_list 객체 3개를 한 페이지로 가르겠다
                                          # Paginator 함수는 객체들을 원하는 갯수만큼 잘라주는 역할, 잘라서 paginator 변수에 담음
    page = request.GET.get('page')        # request된 페이지가 뭔지 알아내고, request 페이지를 변수에 담아냄
                                          # GET방식으로 얻어낸 데이터 중 key값이 page인 딕셔너리형의 value값을 담아준다
    posts = paginator.get_page(page)      # request된 페이지를 얻어온 뒤 return
                                          # Paginator 함수 중에 get_page 사용, 인자로 page사용 (page변수 안에는 page번호 들어있음)
    return render(request, 'home.html', {'blogs' : blogs , 'posts' : posts})


def detail(request, blog_id):
        blog_detail = get_object_or_404(Blog, pk = blog_id)   # (어떤 클래스로부터, 몇 번 인자를 받을 지)
        return render(request, 'detail.html', {'blog': blog_detail})

def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request):   # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()   #Blog 클래스로부터 blog객체 생성 -> blog객체 안에는 title, body, pub_date 변수 있음
    blog.title = request.GET['title']  #new.html에서 만든 name = "title"에 해당하는 내용 가져와서 안에 담음
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # .save()는 쿼리셋메소드중 하나임, blog라는 객체에 title 변수에 넣은 내용, 
                # body에 넣은 내용, pub_date에 넣은 내용을 데이터베이스에 저장해라 라는 메소드이다.
    return redirect('/blog/' +str(blog.id)) #blog.id는 int형이므로 문자열로 바뀌주기 위해 str 붙여줌


def search(request, blog_id):  # new.html을 띄워주는 함수
    blog = Blog()
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
            if request.POST['search'] == request.GET['title']:
                return render(request, '/blog/' + str(blog.id), {'blog': blog_detail})
    return render (request, 'home.html')

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능
    if request.method == 'POST':           
        forms = BlogPost(request.POST)     # forms이라는 변수 안에 POST방식으로 들어온 내용(입력받은 내용) 담기
        if form.is_valid():                # form이 잘 입력됐나 검사하는 과정/ 잘 됐으면  True 반환
            post = form.save(commit=False) # 모델 객체를 가져오되, 아직 저장하지 마라
            post.pub_date = timezone.now() # 입력공간에서는 title, body만 입력했음 pub_date는 views에서 자동으로 입력되게끔
            post.save()
            return redirect('home')

    # 2. 빈 페이지를 띄워주는 기능 (request.method가 GET일때)
    else:  
        form = BlogPost()                  # BlogPost의 객체 form 만들기 -> 비어있는 입력공간이 생김
        return render(request, 'new.html', {'forms':forms})
