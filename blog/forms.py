from django.forms import ModelForm
from blog.models import *
from django.contrib.auth.models import User

class Form(ModelForm):
	class Meta:
		model = Article
		fields=['title', 'contents', 'url','image']
		exclude = ('filtered_image', )

# 회원가입 폼
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# 로그인폼
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
