from django.shortcuts import render
from django.views.generic import View #파이스크립트
# Create your views here.

class PyscriptHandlerView(View):#파이스크립트
    def get(self, request):
        return render(request, 'articles/index.html')


def test1(request):
    return render(request, 'articles/test1.html')
