from django.db import models
from customuser.models import UserModels
# Create your models here.
class Subject(models.Model):
    # 学科名称
    name = models.CharField(max_length=20, null=True, verbose_name='学科名称')
    days = models.IntegerField(null=True, verbose_name='学习时长')
    amount = models.FloatField(max_length=10, null=True, verbose_name='总金额')
    assurance = models.FloatField(max_length=20, null=True, blank=True, verbose_name='最低就业薪资')

    number = models.IntegerField(null=True, verbose_name='排序')
    remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    # status = models.IntegerField(null=False, default=2, verbose_name='状态')
    creater = models.ForeignKey(UserModels,on_delete=models.DO_NOTHING, verbose_name='添加人', null=True, default=None, related_name='creater')
    create_time = models.DateTimeField(null=True, auto_now_add=True, verbose_name='添加时间')
    updater = models.ForeignKey(UserModels,on_delete=models.DO_NOTHING, verbose_name='修改人', null=True, related_name='updater')
    update_time = models.DateTimeField(null=True, auto_now=True, verbose_name='修改时间')

    #由admin管理员给多个用户分配多个学科的管理权限。
    #一个用户可以管理多个学科；一个学科又可以被多个用户管理；所以，学科和用户Model之间就形成了多对多的关系。
    promession_users=models.ManyToManyField(UserModels,verbose_name='授权用户',null=True,related_name='promession_users')
    def __str__(self):
        return self.name


    class Meta:
        db_table = 'subject'
        verbose_name = '学科信息'
        verbose_name_plural = verbose_name
        # 按照number字段的升序排列
        #'-number'降序排列
        ordering = ['number']
