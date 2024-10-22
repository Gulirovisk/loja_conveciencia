from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        produtos =  Produto.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
    def post(self, request):
        pass