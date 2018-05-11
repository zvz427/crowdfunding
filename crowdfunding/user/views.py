from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from .models import UserProfile,UserCertify
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from project.models import ProjectInfo
from util.email_send import sendemail

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

'''
用户的众筹项目页面
'''
class UserFundingView(View):
    def get(self,request):
        return render(request,'user/minecrowdfunding.html',{})
    
'''
用户认证申请
'''
class UserCertifyApplyView(View):
    def get(self,request):
        return render(request, 'user/accttype.html')
        #
        # data = dict()
        # try:
        #     usercertify = UserCertify.objects.get(user=request.user)
        # except Exception as e:
        #     return render(request,'user/accttype.html')
        # else:
        #     if usercertify.realname_certify == '0':
        #         context = {
        #             'msg':'认证审核中，请稍后！'
        #         }
        #         data['msg'] = '认证审核中，请稍后！'
        #         data['res'] = 0
        #         return JsonResponse(data)
        #         # return render(request, 'user/member.html',context=context)
        #     elif usercertify.realname_certify == '1':
        #         context = {
        #             'msg': '已认证通过！'
        #         }
        #         data['msg'] = '已认证通过！'
        #         data['res'] = 1
        #         return JsonResponse(data)
        #         # return render(request, 'user/member.html', context=context)
        
    def post(self,request):
        # 前端传过来的信息无法获取，此处为js的固定值————————————————————？？？？？？？？？？？、
        data = dict()
        usercertify_type = request.POST.get('certify_type','')
        usercetify = UserCertify.objects.create(usercertify_type=usercertify_type,user=request.user)
        data['res'] = 200
        return JsonResponse(data)

'''
用户认证基本信息
'''
class UserCertifyBaseInfoView(View):
    def get(self,request):
        return render(request,'user/apply.html')
    def post(self,request):
        data = dict()
        realname = request.POST.get('realname')
        id_card = request.POST.get('id_card')
        mobile = request.POST.get('mobile')
        usercetify = UserCertify.objects.get(user=request.user)
        usercetify.realname = realname
        usercetify.id_card = id_card
        usercetify.mobile = mobile
        usercetify.save()
        data['res'] = 200
        return JsonResponse(data)

'''
用户认证基本信息
'''
class UserCertifyLoadImgView(View):
    def get(self,request):
        return render(request,'user/apply-1.html')
    def post(self,request):
        data = dict()
        file = request.FILES.get("Filedata", None)
        usercetify = UserCertify.objects.get(user=request.user)
        #保存图片在静态文件的目录下
        #将文件路径保存到数据库中————————————未实现？？？？？？？？？？？？
        print('假装文件已保存')
        data['res'] = 200
        return JsonResponse(data)
    
'''
用户认证邮箱信息
'''
class UserCertifyEmailView(View):
    def get(self,request):
        return render(request,'user/apply-2.html')
    def post(self,request):
        data = dict()
        email = request.POST.get('email','')
        usercetify = UserCertify.objects.get(user=request.user)
        usercetify.email = email
        usercetify.save()
        result = sendemail(email=email,send_type='realname_certify')#同步发送邮件
        if result:
            data['res'] = 200
            data['msg'] = '邮件发送成功'
            return JsonResponse(data)
    
'''
用户认证确认邮箱
'''
class UserCertifyVerifyView(View):
    def get(self,request):
        return render(request,'user/apply-3.html')
    def post(self,request):
        data = dict()
        verifycode = request.POST.get('verifycode','')
        try:
            usercetify = UserCertify.objects.get(verifycode=verifycode)
        except Exception as e:
            print(e)
            data['res'] = 0
            data['msg'] = '验证码错误'
            return JsonResponse(data)
        else:
            data['res'] = 200
            return JsonResponse(data)
        # 审核通过后将实名状态设置为1