from django.shortcuts import render,redirect
from django.views.generic import View #파이스크립트
from .models import Article,Comment
from .forms import ArticleForm,CommentForm
import asyncio
# Create your views here.


def test21(request):
    return render(request, 'articles/test1.html')
def test22(request):
    return render(request, 'articles/test2.html')
class PyscriptHandlerView(View):#파이스크립트
    def get(self, request):
        return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context={
        'article_form':article_form
    }
    return render(request, 'articles/create.html',context)
def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments=article.comment_set.all()
    context={
        'article':article,
        'comment_form':comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html',context)

def comment_create(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.article= article
        comment.save()
    return redirect('articles:detail', article.pk )

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

