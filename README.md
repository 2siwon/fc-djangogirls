# Djangogirls Tutorial

## requirements

- Python 3.6

## 프로젝트 구조

```
projects/
    django/ # Django project들
        djangogirls_project/ # Django project folder
            .git
            .gitignore
              Django, Python, Linux, macOS,
              PyCharm
              # Custom
              .idea/
            .python-version (pyenv local)
            requirements.txt

            djangogirls/ # Django application folder
                manage.py
                djangogirls/ # Django settings folder
                    __init__.py
                    settings.py
                    urls.py
                    wsgi.py
```

## 새 프로젝트 구성
1. djangogirls폴더 생성
2. git init
3. gitignore작성
 3-1. gitignore내부에 .idea/ 추가
4. pyenv virtualenv fc-djangogirls생성
5. pyenv local로 적용할 가상환경 설정
6. GitHub에 Djangogirls저장소 추가
7. 로컬 git에 GitHub remote저장소 추가
8. PyCharm으로 해당 프로젝트 폴더 open후 interpreter설정
  macOS: /usr/local/var/pyenv/versions/
  Linux: $HOME/.pyenv/versions


## MTV모델

### MVC pattern

Model-View-Controller pattern 

> Django: Model-Template-View, MTV

- Model: Data (DB)
- View: 사용자에게 제공되는 화면(또는 기능)
    - Template (HTML)
    
- Controller: Model과 View사이에서 데이터를 가공하는 역할 <- urlresolver에 연결
    - View (Python function)

### Request와 Response간에 일어나는 일

1. 사용자의 요청이 server에 도달 (URL로의 HTTP요청)
2. server는 해당 요청 URL을 Django에 전달
3. Django는 전달받은 URL을 urlresolver로 분석해서 작업을 처리할 Controller(View)에 연결
4. Controller는 요청을 받아 사용자에게 제공할 View(Template)를 응답으로 리턴
5. server는 리턴받은 응답을 사용자에게 전달
