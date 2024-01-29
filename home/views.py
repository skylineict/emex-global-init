from django.shortcuts import render
from django.views.generic import list,View


# Create your views here.


class Home(View):
    def get(self,request):
        return render(request,'hompage/index.html')
    


    def post(self,request):
        return render(request,'hompage/index.html')