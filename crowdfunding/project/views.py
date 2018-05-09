from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from .models import ProjectInfo,RepayInfo


'''
项目详情
'''
class ProjectDetailView(View):
    def get(self, request):
        return render(request, 'project/project_detail.html', {})


'''
项目列表
'''
class ProjectListView(View):
    def get(self, request):
        all_project = ProjectInfo.objects.all()
        context = {
            'all_project':all_project
        }
        return render(request, 'project/project_list.html',context=context)

