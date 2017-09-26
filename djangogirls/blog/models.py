from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        """
        게시글을 발행상태로 만듬
            자신의 published_date를 timezone.now()로 할당
            이후 self.save()를 호출
        :return:
        """
        self.published_date = timezone.now()
        self.save()
    def hide(self):
        """
        게시글을 미발행상태로 만듬
            자신의 published_date를 None으로 할당
            이후 self.save()를 호출
            변경내용이 데이터베이스에 적용되려면 save
        :return:
        """
        self.published_date = None
        self.save()