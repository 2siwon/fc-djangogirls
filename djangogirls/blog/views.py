from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from blog.models import Post

User = get_user_model()


def post_list(request):
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정
    posts = Post.objects.filter(published_date__isnull=False)

    context = {
        # posts key의 value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


# post_detail 기능을 하는 함수 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post객체를 전달
# 템플릿은 'blog/post_detail.html'을 사용

def post_detail(request, pk):
    # Post 인스턴스 1개만 가져옴 변수명은 posts가 아닌 단일객체를 나타내는 post사용
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return HttpResponse('No Post')

    # 'post'key값으로 Post인스턴스 하나 전달
    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    # ==========================================================================
    # 1. post_form.html에 checkbox를 추가
    #    이를 이용해서 publish여부를 결정
    #
    # 2. Post생성 완료 후(DB에 저장 후), post_list페이지로 돌아가기
    #    https://docs.djangoproject.com/ko/1.11/topics/http/shortcuts/#redirect
    #     extra) 작성한 Post에 해당하는 post_detail페이지로 이동
    #
    # 3. Post생성시 Post.objects.create()메서드 사용
    #
    # extra) Post delete기능 구현
    #   def post_delete(request, pk):
    #   (POST요청에서만 동작해야함)
    #   -> pk에 해당하는 Post를 삭제하고, post_list페이지로 이동
    # ==========================================================================
    if request.method == 'POST' and request.POST.get('title') and request.POST.get('content'):
        # ========================================================================================
        # title이나 content값이 오지 않았을 경우에는 객체를 생성하지 않고 다시 작성페이지로 이동 (render또는 redirect)
        #   extra) 작성페이지로 이동 시 '값을 입력해주세요'라는 텍스트를 어딘가에 표시 (render)
        #   extra*****) Bootstrap을 사용해서 modal띄우기
        # ========================================================================================
        title = request.POST['title']
        content = request.POST['content']

        author = User.objects.get(username='siwon')


        post = Post.objects.create(
            author=author,
            title=title,
            content=content,
        )gg

        try:
            if request.POST['is_published']:
                post.publish()
        except MultiValueDictKeyError:
            post.hide()

        # return redirect('/')
        return redirect('/post/detail/{}'.format(post.pk))

    # elif request.method == 'GET':
    else:
        context = {

        }
    return render(request, 'blog/post_form.html', context)


def post_delete(request, pk):
    Post.objects.get(pk=pk).delete()

    context = {

    }

    return redirect('/')
