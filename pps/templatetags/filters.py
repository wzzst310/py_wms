# 自定义过滤器
# 过滤器其实就是python函数
from django.template import Library

# 创建一个Library对象
register = Library()


# 自定义函数至少有一个参数(本身) 最多有两个参数
@register.filter
def mod(num):
    '''判断num是不是为偶数'''
    return num % 2 == 0


@register.filter
def mod_val(num, val):
    '''判断num能否被val整除'''
    return num % val == 0
