from django.conf.urls import url
from .views import CreateOrderView

urlpatterns = [
    url(r'^createorder/(?P<repay_id>\d+)/$',CreateOrderView.as_view(),name='createorder'),


]