from django.db import models
# django 모델은 sql 상관없이 DB와 연동 가능
from django.utils import timezone
# 시간대 설정, 게시일, 생성일에 시간데이터 불러올때

class Post(models.Model):
    #Model 객체를 상속받아 Post클래스를 통해 DB와 연결해줘!
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # 제목 글자수 200자까지 허용 (CharFIeld; 255글자)
    text = models.TextField()
    # 게시글 (TextFIeld; 많은 글자 쓸때)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    # null,blank = True ; 널값,blank 허용

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
