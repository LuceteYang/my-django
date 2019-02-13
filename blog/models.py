from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='%Y/%m/%d/filtered')
    title = models.CharField(max_length=50)
    contents = models.TextField()	# 글자수 제한없는 긴 텍스트 
    url = models.URLField()
    # email  = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)	# 날짜 시간

    # 어드민 리스트에서 노출될 이름으로 사용
    def __str__(self):
    	return '%s by %s' % (self.title, self.name_id)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Article, self).delete(*args, **kwargs)

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
