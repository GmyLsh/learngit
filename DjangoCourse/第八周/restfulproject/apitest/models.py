from django.db import models

class UserGroup(models.Model):
    """
    用户分组:A、B组
    """
    title=models.CharField(max_length=20)

class UserRole(models.Model):
    """
    用户角色表:演员、运动员、警察
    """
    title=models.CharField(max_length=20)

class UserInfo(models.Model):
    user_type_choices = ((1, '普通用户'), (2, 'VIP'), (3, 'SVIP'))
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    #用户组和用户是一对多
    group=models.ForeignKey(UserGroup,on_delete=models.DO_NOTHING,null=True,related_name='user')
    #角色和用户是多对多的关系
    #ORM:user.role.all() / role.user_set.all()
    role=models.ManyToManyField(UserRole)


class UserToken(models.Model):
    """
    保存用户token
    """
    #一个用户对应一个token。
    user = models.OneToOneField(UserInfo, on_delete=True, null=True)
    token = models.CharField(max_length=64, null=True)