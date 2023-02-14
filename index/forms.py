#第一步index/views.py 创建Form对象。
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

class LoginForm(forms.Form): #继承自Form类，
    user_name = forms.CharField(label="用户名", min_length=6, max_length=12)    # 新建表单字段
    user_password = forms.CharField(label="用户密码", min_length=8)

class BookSearch(forms.Form):
    error_css_class = "error"
    required_css_class = "required"

    title = forms.CharField(label='书名', required=True, widget=forms.TextInput,
                            ) #error_messages='"required":"请输入正确的title"' initial='请输入书名',
    public = forms.CharField(label='出版社', required=False)
    # author = forms.CharField(label='作者', required=False)

    def clean(self):
        cln = super().clean()
        title = cln.get('title')
        public = cln.get('public')
        if title or public:
            raise forms.ValidationError('书名和出版社均不能为空')


class TestForm1(forms.Form):
    a = forms.CharField(required=False)
    b = forms.CharField(max_length=20)
    c = forms.IntegerField(min_value=1, max_value=10)


class PubForm(forms.Form):
    name = forms.CharField(label='出版社名称', max_length=30, min_length=1, error_messages={
        'required':'请输入正确的title',
        'min_length': '用户名不能少于1位字符',
        'max_length': '用户名不能大于30位字符',
    })
    addr = forms.CharField(label='地址', required=False)

    def clean(self):
        cleaned_data = super(PubForm, self).clean()
        name = cleaned_data.get('name')

        if not name:
            print('name is empty')
            raise forms.ValidationError(u"出版社名称不能为空", code='required')

    def clean_addr(self):
        addr = self.cleaned_data['addr']
        if addr.find('a') >= 0:
            raise forms.ValidationError('地址中不能有字符a')
        return addr


def even_validator(value):
    if value % 2 != 0:
        raise ValidationError('%d is not a even number'%value)

class EvenField(forms.IntegerField):
    def __init__(self, **kwargs):
        super().__init__(validators=[even_validator], **kwargs)

from index.models import UserInfo
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        labels = {'username':'姓名1'}
        #exclude = {'password'}
        help_texts = { 'username':'请输入用户的名字' }
        fields = "__all__"
       # widgets = {'password': widgets.PasswordInput()}





