from django.db import models
from customuser.models import UserModels
from subject.models import Subject

class Stage(models.Model):
    #关联学科外键
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='学科')
    title = models.CharField(max_length=50,verbose_name='阶段标题')
    days = models.IntegerField(verbose_name='学时', null=True)
    project = models.CharField(max_length=255,verbose_name='项目')
    teaching = models.CharField(max_length=255,verbose_name='教学方法', null=True)
    learning = models.CharField(max_length=255,verbose_name='学习方法', null=True)
    sharing = models.CharField(max_length=255,verbose_name='学生分享', null=True)
    number = models.IntegerField(null=False)
    remark = models.CharField(max_length=255, null=True, blank=True,verbose_name='备注')
    status = models.IntegerField(null=True)
    creater = models.ForeignKey(UserModels, on_delete=models.DO_NOTHING, verbose_name='添加人', related_name='stage_creater')
    create_time = models.DateTimeField(null=False, auto_now_add=True,verbose_name='添加时间')
    updater = models.ForeignKey(UserModels, on_delete=models.DO_NOTHING, verbose_name='修改人',related_name='stage_updater')
    update_time = models.DateTimeField(null=False, auto_now=True)
    stage_id = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'stage'
        verbose_name = '阶段信息'
        verbose_name_plural = verbose_name
        ordering = ['number']

