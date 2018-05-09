from django.conf.urls import url
from .views import ProjectDetailView,ProjectListView

urlpatterns = [
    url(r'^project_detail/$',ProjectDetailView.as_view(),name='project_detail'),
    url(r'^project_list/$', ProjectListView.as_view(), name='project_list'),

]