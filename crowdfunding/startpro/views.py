from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from project.models import ProjectInfo,RepayInfo

'''
阅读协议
'''
class StartProView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'startpro/start.html', context=context)

'''
项目信息
'''
class ProjectInfoView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'startpro/start-step-1.html', context=context)
    
    def post(self,request):
        # 和此页面无关的字段在提交时报错，在创建模型时需要指定默认值，不然插入数据时报错！！！！
        data = dict()
        category_type = request.POST.get('category_type','')
        projectname = request.POST.get('projectname','')
        projectdesc = request.POST.get('projectdesc','')
        target_money = request.POST.get('target_money','')
        total_time = request.POST.get('total_time','')
        brief_intro = request.POST.get('brief_intro','')
        detail_intro = request.POST.get('detail_intro','')
        mobile = request.POST.get('mobile','')
        service_phone = request.POST.get('service_phone','')
        
        # 关联的外键需要增加当前用户的id！！！！
        proinfo = ProjectInfo.objects.create(
            category=category_type,name=projectname,desc=projectdesc,target_money=target_money,
            total_time=total_time,brief_intro=brief_intro,detail_intro=detail_intro,mobile=mobile,
            service_phone=service_phone,user_id=request.user.id
        )
        # 把创建的项目保存到seesion中，下一个回报的视图使用！！！
        request.session['project_id'] = proinfo.id
        print('request.session[project_id]',request.session['project_id'])
        print(category_type,projectname,projectdesc,target_money,total_time,brief_intro,detail_intro,service_phone)
        data['res'] = 200
        # data['project_id'] = proinfo.id
        return JsonResponse(data)
    
'''
回报信息
'''
class ProjectRepayView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'startpro/start-step-2.html', context=context)
    
    def post(self,request):
        data = dict()
        repay_type = request.POST.get('repay_type', '')
        support_money = request.POST.get('support_money', '')
        repay_content = request.POST.get('repay_content', '')
        repay_num = request.POST.get('repay_num', '')
        is_limit_buy = request.POST.get('is_limit_buy', '')
        limit_buy_num = request.POST.get('limit_buy_num', '')
        freight = request.POST.get('freight', '')
        receipt = request.POST.get('receipt', '')
        repay_time = request.POST.get('repay_time', '')
    
        print('request.session[project_id]----------------------',request.session['project_id'])

        # 要添加关联项目的外键
        repayinfo = RepayInfo.objects.create(
            type=repay_type,support_money=support_money,repay_content=repay_content,
            repay_num=repay_num,is_limit_buy=is_limit_buy,limit_buy_num=limit_buy_num,
            freight=freight,receipt=receipt,repay_time=repay_time,
            # project_id=request.session['project_id']
            project_id=6,
            
        )
    
        data['res'] = 200
        return JsonResponse(data)

'''
收款账号信息
'''
class AccountInfoView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'startpro/start-step-3.html', context=context)