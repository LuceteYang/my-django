from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

import logging

logger = logging.getLogger(__name__)


from blog.forms import *

def hello(request):
	# print(reverse('blog:post_detail', args=[10]))
	logger.debug("list")
	return HttpResponse('hello')


def get_json_response(request):
	return JsonResponse({
		'message': 'JsonResponse 메세지',
		'title': 'JsonResponse 타이틀',
		 },
		json_dumps_params={'ensure_ascii': False})


@login_required
def write(request):
	if request.method == 'POST':
		form = Form(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save(commit = False)
			new_post.user = request.user
			new_post = form.save()
			return redirect('/view/'+str(new_post.pk))
		else:
			return render(request, 'write.html',{'form' : form})
	else:
		form = Form()
		return render(request, 'write.html',{'form' : form})


class WriteView(generic.View):
	def post(self, request):
		form = Form(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save(commit = False)
			new_post.user = request.user
			new_post = form.save()
			return redirect('/view/'+str(new_post.pk))
		else:
			return render(request, 'write.html',{'form' : form})
	def get(self, request):
		form = Form()
		return render(request, 'write.html',{'form' : form})


class WriteFormView(generic.FormView):
	form_class = Form
	template_name = 'write.html'
	pk = None
	def form_valid(self, form):
		new_post = form.save(commit = False)
		new_post.user = self.request.user
		new_post = form.save()
		self.pk = new_post.pk
		return super(WriteFormView, self).form_valid(form)
	def get_success_url(self):
		return reverse('blog:view', kwargs={'pk': self.pk})

class ListView(generic.ListView):
	#print("here")
	context_object_name = 'articleList'
	template_name = 'list.html'
	def get_queryset(self): # 메소드 오버라이딩
		# c = q.choice_set.filter(choice_text__startswith='Just hacking')
		return Article.objects.all().order_by('cdate')

class DetailView(generic.DetailView):
	model = Article
	template_name = 'view.html'

@login_required
def article_remove(request, pk):
	article = get_object_or_404(Article, pk=pk)
	print(article.user)
	print(request.user)
	if article.user == request.user:
		article.delete()
		# comment.is_removed = True
		# comment.save()
	return redirect('blog:list')


def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			django_login(request, new_user)
			return redirect('blog:list')
		else:
			# login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
			return render(request, 'join.html', {'form': form})
	else:
		form = UserForm()
		return render(request, 'join.html', {'form': form})


def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			django_login(request, user)
			return redirect('blog:list')
		else:
			form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
			return render(request, 'login.html', {'form': form})
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})


def logout(request):
	django_logout(request)
	return redirect('blog:list')

