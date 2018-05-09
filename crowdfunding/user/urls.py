from django.conf.urls import url
from .views import LoginView,RegisterView,UserInfoView

urlpatterns = [
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^userinfo/$', UserInfoView.as_view(), name='userinfo'),

]

