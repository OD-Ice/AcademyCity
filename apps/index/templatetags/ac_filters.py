from django import template
from datetime import datetime
from django.utils.timezone import now as now_func, localtime

register = template.Library()


@register.filter()
def time_since(value):
    """
    time距离现在的时间间隔
    1.如果时间间隔小于1分钟，显示'刚刚'
    2.如果大于1分钟小于1小时，显示'xx分钟前'
    3.如果大于1小时小于24小时，显示'xx小时前'
    4.如果大于24小时小于7天，显示'xx天前'
    5.否则显示具体时间'xxxx-xx-xx xx:xx'
    """
    if not isinstance(value, datetime):
        return value
    now = now_func()
    timestamp = (now-value).total_seconds()
    if timestamp <= 60:
        return '刚刚'
    elif 60 < timestamp <= 60*60:
        return f'{int(timestamp/60)}分钟前'
    elif 60*60 < timestamp <= 60*60*24:
        return f'{int(timestamp/60/60)}小时前'
    elif 60*60*24 < timestamp <= 60*60*24*7:
        return f'{int(timestamp/60/60/24)}天前'
    else:
        return localtime(value).strftime('%Y-%m-%d %H:%M')


@register.filter()
def time_format(value):
    if not isinstance(value, datetime):
        return value
    else:
        return localtime(value).strftime('%Y-%m-%d')