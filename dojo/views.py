from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from .forms import PostForm
from .models import Post


# Create your views here.

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            #방법 1
            '''
            #post.title = form.cleaned_data['title']
            #post.content = form.cleaned_data['content']
            #post.save()
            '''
            #방법 2
            '''
            post = Post(title=form.cleaned_data['title'],
                        content = form.cleaned_data['content'])
            '''
            #방법 3
            '''
            post=Post.objects.create(title=form.cleaned_data['title'],
                                    contene = form.cleaned_data['content'])
            '''
            #방법 4
            post = Post.objects.create(**form.cleaned_data)
            return redirect('/dojo/')  #namespace:name사용
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {'form':form,
})

def mysum(request, numbers):
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name, age))

#직접 문자열로 HTML형식 만들기
def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))

#템플릿을 통해 만들기
def post_list2(request):
    name = '공유'
    response = render(request, 'dojo/post_list.html', {'name': name})
    return response

#JSON파일로 응답하기
def post_list3(request):
    return JsonResponse({
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})

#엑셀 다운로드 응답하기
def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'SearchResultList.xls')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
