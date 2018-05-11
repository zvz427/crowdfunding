from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from project.models import ProjectInfo

'''
首页
'''
class IndexView(View):
    def get(self,request):
        all_project = ProjectInfo.objects.all().order_by('-fav_num')[:3]
        context = {
            'all_project':all_project,
            
        }
        return render(request,'index.html',context=context)
'''
用户登录
'''
class LoginView(View):
    def get(self,request):
        print('run get')
        return render(request,'user/login.html',{})
    
    #post ajax的数据没有传过来，使用的是form表单？？？？？？？？？？？
    def post(self,request):
        print('run post')
        data = dict()
        username = request.POST.get('username')
        password = request.POST.get('password')
        zxy = request.POST.get('zxy')
        print(username,password)
        data['res'] = 200
        return redirect(reverse('index'))
    
'''
用户注册
'''
class RegisterView(View):
    def get(self,request):
        return render(request,'user/reg.html',{})
    
    def post(self,request):
        data = dict()
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        usercategory = request.POST.get('usercategory')
        user = UserProfile.objects.create(username=username,password=make_password(password),email=email,usercategory=usercategory)
        data['res'] = 200
        return JsonResponse(data)
    
'''
用户中心
'''
class UserInfoView(View):
    def get(self,request):
        return render(request,'user/member.html',{})


    