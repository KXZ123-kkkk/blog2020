from rest_framework.views import exception_handler as drf_exception_handler  # drf原生处理异常函数取别名 drf_exception_handler
from rest_framework.views import Response
from rest_framework.exceptions import AuthenticationFailed



def exception_handler(exc, context):  # 自定义处理异常函数
    # drf的exception_handler做基础处理
    response = drf_exception_handler(exc, context)
    if isinstance(exc, AuthenticationFailed):
        return Response({'status': 10, 'msg': str(exc)})

    # 为空，就是drf框架处理不了的异常
    if response is None:  # 处理之后为空，再进行自定义的二次处理
        # print(exc)    #错误原因   还可以做更详细的原因，通过判断exc信息类型
        # print(context)  #错误信息
        print('%s - %s - %s' % (context['view'], context['request'].method, exc))
        return Response({'status': 11, 'msg': '服务器错误'})
    if str(exc) == 'Invalid page.':
        return Response({'status': 0, 'msg': 'noPage'})
    return Response({'status': 1, 'msg': str(exc)})  # 处理之后有值，就直接返回结果
