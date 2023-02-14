from django.db import models


class Pub(models.Model):
    name = models.CharField(max_length=50, verbose_name="出版社")
    addr = models.CharField(max_length=80, verbose_name="地址", null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name="书名")
    # public = models.CharField(max_length=50, verbose_name="出版社")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="定价", null=True)

    def default_price(self):
        return '9'

    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="零售价", default=default_price)
    public = models.ForeignKey(to=Pub, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'title:%s pub:%s price:%s' % (self.title, self.public, self.price)


class Author(models.Model):     # 创建作者表
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        return '作者：%s' % (self.name)


class UserInfo(models.Model):   # 创建用户信息表
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=24, verbose_name='密码')
    sexitems = (
        ('m', '男性'),
        ('w', '女性'),
    )
    sex = models.CharField(max_length=1, verbose_name='性别', choices=sexitems)

    def __str__(self):
        return '%s(%s)' % (self.username, self.sex)


class Test01(models.Model):
    fd01 = models.CharField(max_length=10, verbose_name='字段1')
    fd02 = models.CharField(max_length=40, verbose_name='字段2')


# class Test02(models.Model):     # Test02
#     fd01 = models.CharField(max_length=10, verbose_name='字段11', keyword=True, unique=True)
#     fd02 = models.CharField(max_length=40, verbose_name='字段22')
#
#     class Meta:
#         db_table = 'Test0222'
#         table_name = '表Test02名称'
#         index = ['fd02']
#         permissions = [('have_read_permission', '有读的权限')]
#





