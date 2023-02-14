from django import template
register = template.Library()

#注册自定义简单标签
@register.simple_tag
def addstr_tag(strs):
    return '[' + strs + ']'

@register.simple_tag(name='ta1')
def addstr2_tag(strs):
    return strs + '|后面加个A'

#注册自定义引用标签
@register.inclusion_tag('inclusion.html', takes_context=True)
#定义函数渲染模板文件 inclusion.html
def add_webname_tag(context, namestr): #使用takes_context=True此时第一个参数必须为context
    return {'hello':'%s %s' % (context['variable'], namestr)}
    #return {'hello':'yehello1213'}


@register.filter(name='myfil1')
def hello_my_filter(value):
    return value.replace('django', 'Python')

@register.filter(name='myfil2')
def my_filter_for_sort(value):
    return sorted(value[0])

