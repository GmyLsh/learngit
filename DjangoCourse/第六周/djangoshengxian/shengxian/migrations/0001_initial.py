# Generated by Django 2.1.2 on 2018-11-27 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('food_price', models.IntegerField(default=0, verbose_name='商品价格')),
                ('food_count', models.IntegerField(default=0, verbose_name='商品库存')),
                ('food_image', models.ImageField(upload_to='uploads/%Y/%m')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'ordering': ['-food_price'],
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.CharField(max_length=100, verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.IntegerField(default=0, verbose_name='为1购物车清空')),
                ('shop_code', models.IntegerField(null=True, verbose_name='购买商品数量')),
                ('shop_price', models.IntegerField(null=True, verbose_name='商品单价')),
                ('shop_price_total', models.IntegerField(null=True, verbose_name='小计')),
                ('add_shop_time', models.DateTimeField(auto_now_add=True, verbose_name='添加购物车的时间')),
                ('food_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shengxian.FoodProduct', verbose_name='购物车添加商品')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='ShopDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_detail', models.CharField(max_length=100, verbose_name='商品详情')),
                ('shop_intro', models.CharField(max_length=100, verbose_name='商品简介')),
                ('food_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shengxian.FoodProduct', verbose_name='所属商品')),
            ],
            options={
                'verbose_name': '商品详情',
                'verbose_name_plural': '商品详情',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=20, null=True, verbose_name='联系方式')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='联系地址')),
                ('post_code', models.IntegerField(max_length=20, null=True, verbose_name='邮编')),
                ('receiver', models.CharField(max_length=20, null=True, verbose_name='收件人')),
            ],
        ),
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='用户昵称')),
                ('name_password', models.CharField(max_length=100, verbose_name='用户密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shengxian.UserModels', verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='shopcart',
            name='nickname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shengxian.UserModels', verbose_name='添加购物车用户'),
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='sort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shengxian.FoodType', verbose_name='所属分类'),
        ),
    ]
