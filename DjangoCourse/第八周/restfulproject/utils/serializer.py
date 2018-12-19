from rest_framework import serializers

class RolesSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    #要定义需要序列化的字段、注意:这里定义的字段的值必须和models.py中的字段保持一致。
    title=serializers.CharField()
class UsersSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    #要定义需要序列化的字段、注意:这里定义的字段的值必须和models.py中的字段保持一致。
    #如果这个字段时choices((1,'普通用户'))类型的，那么该字段有一个内置的函数，用于获取数字对应的值。get_字段名称_display

    #source参数可以指定字段名(username,password),也可以指定函数名get_user_type_display,如果source='username'已经指定了根据models.py中的username进行序列化，此时这个字段的名称就不能和Model中的字段保持一致了。
    user_type=serializers.CharField(source='get_user_type_display')
    username=serializers.CharField()
    password=serializers.CharField()

    #序列化用户所在的组的信息
    #orm:根据从表的一条数据查询主表的数据 user.group.id/user.group.title
    group=serializers.CharField(source='group.title')

    #序列化用户所有的角色(多对多):通过自定义显示字段实现。
    role=serializers.SerializerMethodField()
    #get_字段名称:自定义显示字段实现需要定义这样的一个方法。
    def get_role(self,obj):
        #obj就是UserInfo的对象  user.role.all()/ role.user_set.all()
        roles=obj.role.all()
        results=[]
        for role in roles:
            results.append({
                'id':role.id,
                'title':role.title
            })
        return results

class GroupsSerializer(serializers.Serializer):
    title=serializers.CharField()
    #orm中:主表一条数据查从表多条数据 group.user_set.all
    #主表查询从表
    #当通过GroupsSerializer序列化UserGroup的一个model的时候，由于一个UserGroup的model对应了多个UserInfo的Model，在这里需要使用UsersSerializer对每一个UserInfo再次进行序列化。
    user=UsersSerializer(many=True)

from apitest.models import *
class UserModelSerializer(serializers.ModelSerializer):
    #ModelSerializer继承于Serializer，所以Serializer中的语法仍然是可以使用的。
    class Meta:
        #指定要序列化哪一个模型
        model=UserInfo
        #ModelSerializer类使用fields控制需要序列化的字段。
        #显示所有的
        # fields="__all__"
        #想显示那几个就添加那几个
        fields=('role','group','user_type')

class Valication(object):
    def __call__(self, value,*args, **kwargs):
        # 当把POST数据传给这个ValicationSerializer类的时候，会执行__call__方法。
        if len(value)<6:
            raise serializers.ValidationError('数据长度不够6位')
class ValicationSerializer(serializers.Serializer):
    #给password字段绑定一个验证器validators，它内部可以设置多个类。等把数据交给这个ValicationSerializer类的时候，就会执行验证。
    # password=serializers.CharField(validators=[Valication()])
    #内置的验证,required=True字段必填
    #验证:内置的验证，和form验证原理一样的。自定义的验证规则:validators=[Valication()]
    password = serializers.CharField(min_length=6,required=True,error_messages={
        'required':'不能为空',
        'min_length':'长度不够'
    })
    #validate_password:前面validate是固定写法，password是你的字段名
    # def validate_password(self):
    #     pass