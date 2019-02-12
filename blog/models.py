from django.db import models
from django.utils import timezone


class Article(models.Model):
    name = models.CharField(max_length=50)	# 글자수 제한된 텍스트 
    title = models.CharField(max_length=50)
    contents = models.TextField()	# 글자수 제한없는 긴 텍스트 
    url = models.URLField()
    email  = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)	# 날짜 시간

    # 어드민 리스트에서 노출될 이름으로 사용
    def __str__(self):
    	return self.title

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)