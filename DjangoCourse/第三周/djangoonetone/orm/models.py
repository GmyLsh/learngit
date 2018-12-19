from django.db import models

# Create your models here.
#ORM数据库的一对一关系:一个表中的一条数据对应着另外一个表中的一条数据。
#例如：一个账户只对应着一个联系人，一个联系人只能有一个账户。身份证。结婚证
class Account(models.Model):
    """
    一个账户类
    """
    #账户名称
    a_name=models.CharField(max_length=20)
    #账户密码
    a_pwd=models.CharField(max_length=10)
    #账户激活时间
    #DateField()参数为空，这个字段的值需要自己填加。
    #auto_now=True：当这个Account这个对象的属性被修改了，在保存的时候，这a_register_date个时间会自动更新为保存时间；(强调更新时间)
    #auto_now_add=True:含义就是这个时间字段不会随着对象的修改而更新这个时间，只在这个对象被第一次创建的时候自动填充创建的时间。以后也不会再变动了。(强调创建时间)
    #auto_created=True:表示使用当前时间作为值，自动创建这个字段的值，默认是False。当创建对象的时候就不需要给这个字段赋值了，会自动穿件。
    a_register_date=models.DateField(auto_now_add=True)
    a_update_date=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='account'


class Contact(models.Model):
    """
    一个账户的拥有人
    """
    #所有人的姓名
    c_name=models.CharField(max_length=20)
    #所有人的住址
    c_address=models.TextField()
    #所有人的联系方式
    c_phone=models.CharField(max_length=20)

    #添加账户和所有人的一对一关系。
    #当account表中的一条数据删除时，对应的contact表中的数据也要删除。
    account=models.OneToOneField(Account,on_delete=models.CASCADE)
    class Meta:
        db_table='contact'

#将OneToOneField设置在哪一个表中，哪一个表就是从表():OneToOneField()的第一个参数就是主表；
#OneToOneField不强调位置关系，两个表中任选一个作为主表，另一个表作为从表

#一对多：一必须是主表，多是从表，强调位置关系。


