from django import http
def register(request):
    """
       用户注册函数视图
       :param request: 请求对象，包含了请求报文信息
       :return: 响应对象，用于构造响应报文，并响应给用户
       """
    return http.HttpResponse('这里假装返回注册页面')