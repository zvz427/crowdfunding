from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from project.models import RepayInfo

'''
创建订单信息
'''
class CreateOrderView(View):
    def get(self, request, repay_id):
        repayinfo = RepayInfo.objects.get(id=repay_id)
        project = repayinfo.project
        context = {
            'repayinfo':repayinfo,
            'project':project,
        }
        return render(request, 'order/pay-step-1.html', context=context)
    
    def post(self):
        data = dict()
        
        data['res'] = 200
        return JsonResponse(data)
        pass
