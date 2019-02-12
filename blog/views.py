from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
# from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
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

# @login_required
def write(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			new_post = form.save()
			return redirect('/view/'+str(new_post.pk))
		else:
			return render(request, 'write.html',{'form' : form})
	else:
		form = Form()
		return render(request, 'write.html',{'form' : form})

class WriteView(generic.View):
	def post(self, request):
		form = Form(request.POST)
		if form.is_valid():
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
		item = form.save()
		self.pk = item.pk
		return super(WriteFormView, self).form_valid(form)
	def get_success_url(self):
	    return reverse('blog:view', kwargs={'pk': self.pk})
		
class ListView(generic.ListView):
	#print("here")
    context_object_name = 'articleList'
    template_name = 'list.html'
    def get_queryset(self): # 메소드 오버라이딩

    	return Article.objects.all().order_by('cdate')

class DetailView(generic.DetailView):
    model = Article
    template_name = 'view.html'

	# c = q.choice_set.filter(choice_text__startswith='Just hacking')
def article_remove(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('blog:list')