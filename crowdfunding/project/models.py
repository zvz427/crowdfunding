from django.db import models
from user.models import UserProfile

CATEGORY_TYPE = {
    'technology': '科技',
    'design': '设计',
    'public_welfare': '公益',
    'agriculture': '农业',
}

TAGE_TYPE = {
    'mobile': '手机',
    'computer': '电脑',
    'digital': '数码',
}
# 项目状态
ACTIVE_STATUS = {
    '0': '审核中',
    '1': '众筹中',
    '2': '已结束',
}


'''
项目信息
'''
class ProjectInfo(models.Model):
    category_type = ((key, value) for key, value in CATEGORY_TYPE.items())
    tage_type = ((key, value) for key, value in TAGE_TYPE.items())
    active_status = ((key, value) for key, value in ACTIVE_STATUS.items())
    name = models.CharField(max_length=50, default='项目1', verbose_name='众筹项目名字')
    desc = models.CharField(max_length=200, verbose_name='项目一句话简述')
    fav_num = models.IntegerField(verbose_name='关注人数')
    target_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='目标金额')
    raised_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已筹金额')
    create_time = models.DateField(verbose_name='创建日期')
    category = models.CharField(max_length=10,choices=category_type, verbose_name='项目分类', default='technology')
    tage = models.CharField(max_length=10,choices=tage_type, default='mobile', verbose_name='项目标签')
    # detail = models.HTML(verbose_name='产品详情')
    active_status = models.CharField(max_length=10,choices=active_status, verbose_name='项目状态', default='0')
    project_img = models.ImageField(max_length=100, verbose_name='项目图片', upload_to='project_img/%Y/%m',
                                    default='project_img/default.png')

    brief_intro = models.CharField(max_length=100, verbose_name='自我介绍',default='自我介绍')
    detail_intro = models.TextField(verbose_name='详细自我介绍',default='详细自我介绍')
    mobile = models.CharField(max_length=11, verbose_name='联系电话',default='123')
    service_phone = models.CharField(max_length=11, verbose_name='客服电话',default='123')
    
    # initiator = models.ForeignKey(InitiatorInfo, verbose_name='项目发起人或机构')
    user = models.ForeignKey(UserProfile,verbose_name='发起项目的用户')
    
    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


'''
回报信息
'''
class RepayInfo(models.Model):
    type = models.CharField(max_length=10,choices=(('reality', '实物回报'), ('virtual', '虚拟物品回报')), default='reality',
                            verbose_name='回报类型')
    support_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='支持金额')
    repay_content = models.TextField(verbose_name='回报内容')
    repay_img = models.ImageField(max_length=100, verbose_name='项目图片', upload_to='repay_img/%Y/%m',
                                  default='repay_img/default.png')
    repay_num = models.IntegerField(verbose_name='回报数量')
    is_limit_buy = models.CharField(max_length=10, choices=(('0', '不限购'), ('1', '限购')), verbose_name='单笔限购')
    limit_buy_num = models.IntegerField(verbose_name='限购数量',null=True,blank=True)
    freight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='运费')
    receipt = models.CharField(max_length=10, choices=(('0', '不可开发票'), ('1', '可开发票')), verbose_name='是否开发票')
    repay_time = models.IntegerField(verbose_name='回报时间')
    project = models.ForeignKey(ProjectInfo, verbose_name='众筹项目')
    
    class Meta:
        verbose_name = '回报信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return str(self.support_money)+'--'+self.repay_content


'''
项目收款账号及身份核实
'''
class AccountNumInfo(models.Model):
    company_num = models.CharField(max_length=11, verbose_name='易付宝企业账号')
    id_card = models.CharField(max_length=18, verbose_name='法人身份证号')
    user = models.ForeignKey(UserProfile, verbose_name='收款的用户')
    project = models.ForeignKey(ProjectInfo, verbose_name='众筹项目')
    
    class Meta:
        verbose_name = '收款账号及身份核实'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.id_card


# '''
# 发起人或机构信息
# '''
# class InitiatorInfo(models.Model):
#     # user = models.ForeignKey(UserProfile,verbose_name='发起项目的用户') 报错
#     project = models.ForeignKey(ProjectInfo, verbose_name='众筹项目')
#     brief_intro = models.CharField(max_length=100, verbose_name='自我介绍')
#     detail_intro = models.TextField(verbose_name='详细自我介绍')
#     mobile = models.CharField(max_length=11, verbose_name='联系电话')
#     service_phone = models.CharField(max_length=11, verbose_name='客服电话')
#
#     class Meta:
#         verbose_name = '发起人信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.brief_intro
