# Django



## 创建

```
django-admin startproject
```



## 结构



## 配置（settings.py）



## URL和视图函数（views.py）



## 路由配置（urls.py）

+ path
+ re_path



## 请求和响应

### request

> + path_info
> + method
> + GET
> + POST
> + FILES
> + COOKIES
> + session
> + body
> + scheme 协议
> + get_full_path() 
> + META
> + META['REMOTE_ADDR'] 客户端IP地址

### response

> | 类型                    | 作用           | 状态码 |
> | ----------------------- | -------------- | ------ |
> | HttpResponseRedirect    | 重定向         | 302    |
> | HttpResponseNotModified | 未修改         | 304    |
> | HttpResponseBadRequest  | 错误请求       | 400    |
> | HttpResponseNotFound    | 没有对应的资源 | 404    |
> | HttpResponseForbidden   | 请求被禁止     | 403    |
> | HttpResponseServerError | 服务器错误     | 500    |



## GET请求和POST请求



## 设计模式及模板层

+ MVC 模型层、视图层、控制

+ MTV 模型层、模板层、视图层

+ 模板层

  > 配置模板层 templates
  >
  > 加载模板 render()



## 模板层-变量和标签



## 模板层-过滤器和继承

+ block 修改
+ extends 继承



## url反向解析

+ ```
  {% url '别名' 参数='值' %}
  ```

+ reverse 反向解析

+ HttpResponseRedirect、redirect 重定向



## 静态文件（static）

+ 配置（settings.py）

+ 加载

  ```
  {% load static %}
  
  {% static '静态资源路径' %}
  ```



## 应用及分布式路由

```
python manage.py startapp

include('app.urls')
```



## 模型层

+ 安装 mysqlclient

+ 创建数据库

  ```
  create database default charset utf8
  ```

+ 配置 mysql（settings.py）

+ 创建模型类（models.py）

+ 生成迁移文件（migrations文件夹）

  ```
  python manage.py makemigrations
  ```

+ 执行迁移脚本程序

  ```
  python manage.py migrate
  ```



## 模型类 — 字段类型

+ BooleanField()
+ CharField(max_length)
+ DateField()
+ DateTimeField(auto_now)
+ FloatField()
+ DecimaField(max_digits(位数总数), decimal_places(小数点位数))
+ EmailField()
+ IntegerField()
+ ImageField()
+ TextField()



## 模型类 — 字段选项

+ primary_key
+ blank
+ null
+ default
+ db_index
+ unique
+ db_column
+ verbose_name = '中文名'



## 模型类 — Meta类（给模型赋予属性）

```python
class Meta:
    db_table = 'table_name'
    verbose_name = 'admin_name'  # 单数
    verbose_name_plural = verbose_name  # 复数=单数
```



## 创建数据

```
Model.objects.create(属性=值)

obj = Model(属性=值)
obj.save()
```



## 查询操作

+ all()
+ values()  返回字典
+ values_list()
+ order_by() 默认升序，"-"降序
+ get()
+ filter()
+ exclude()

格式输出（models.py）

```python
def __str__(self):
    return '{}'.format(self.属性)
```

查询谓词

+ __exact 等值匹配
+ __contains 包含指定值
+ __startswith
+ __endswith
+ __gt 大于
+ __lt 小于
+ __gte 大于等于
+ __lte 小于等于
+ __in
+ __range



## 更新操作

```
obj = Model.objects.方法(属性)

obj.属性=值
obj.save()

obj.update(属性=值)
```



## 删除操作

+ obj.delete()

+ 伪删除（models.py）

  ```
  is_active = models.BooleanField(default=True)
  ```



## F对象和Q对象

+=

+ & 与
+ | 或
+ ~ 非



## 聚合查询

```
Model.objects.aggregate(结果变量名=聚合函数('列'))

分组聚合
obj = Model.objects.values('列')
result = obj.annotate(名=聚合函数('列'))
```

+ Sum
+ Avg
+ Count
+ Max
+ Min



## 原生数据库操作

+ Model.objects.raw('sql语句', ['拼接参数'])

+ ```python
  from django.db import connection
  
  with connection.cursor() as cur:
      cur.execute('sql语句', ['拼接参数'])
  ```



## admin后台管理

```
python manage.py createsuperuser
```

+ 注册自定义模型类（admin.py）

  ```
  admin.site.register(Model, 模型管理器类(可选))
  ```

+ 模型管理器类（admin.py）

  ```python
  class nameManager(admin.ModelAdmin):
      # 列表页显示哪些字段的列
      list_display = ['列']
      # 控制list_display中的字段，哪些可以链接到修改页
      list_display_links = ['列']
      # 添加过滤器
      list_filter = ['列']
      # 添加搜索框，模糊查询
      search_fields = ['列']
      # 添加可在列表页编辑的字段
      list_editable = ['列']
  ```



## 关系映射

+ 一对一

  > 模型类创建
  >
  > ```
  > models.OneToOneField(Model(模型类名), on_delete)
  > 
  > on_delete 字段选项
  > models.CASCADE
  > models.PROTECT
  > SET_NULL
  > SET_DEFAULT
  > ```
  >
  > 数据创建
  >
  > 数据查询
  >
  > + 正向查询
  >
  > + 反向查询，反向关联属性——'实例对象.引用类名(小写)'

+ 一对多

  > 模型类创建
  >
  > ```
  > models.ForeignKey(Model(一的模型类名), on_delete)
  > ```
  >
  > 数据创建
  >
  > 数据查询
  >
  > + 正向查询
  >
  > + 反向查询
  >
  >   ```
  >   obj = Model.objects.get(属性=值)  # 一
  >     
  >   result = obj.Model(小写)_set.all()  # 多
  >   result = Model.objects.filter(ForeignKey_name==obj)
  >   ```

+ 多对多

  > 模型类创建
  >
  > ```
  > models.ManyToManyField(Model)
  > ```
  >
  > 数据创建
  >
  > 数据查询
  >
  > + 正向查询
  > + 反向查询



## 会话Cookies、Session

+ Cookies

  ```python
  # 设置
  res = HttpResponse()
  res.set_cookie(key, value=' ', max_age, expires)
  
  # 删除
  HttpResponse().delete_cookie(key)
  
  # 获取
  request.COOKIES.get()
  ```

+ Session

  ```python
  # 保存
  request.session['key'] = value
  
  # 获取
  request.session['key']
  request.session.get('key')
  
  # 删除
  del request.session['key']
  ```

  python manage.py clearsessions



## 缓存

+ 配置（settings.py）

  ```python
  CACHES = {
      'default': {
          'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
          'LOCATION': 'my_cache_table',  # 表名
          'TIMEOUT': 300,  # 保存时间
          'OPTIONS': {
              'MAX_ENTRIES': 300,  # 最大数量
              'CULL_FREQUENCY': 2  # 删除所占比例
          }
      }
  }
  ```

+ 创建缓存数据表

  ```
  python manage.py createcachetable
  ```

+ 使用缓存

  > 视图函数
  >
  > ```python
  > @cache_page(time)
  > ```
  >
  > 路由
  >
  > ```python
  > cache_page(time)(视图函数)
  > ```

+ 局部缓存

  ```
  cache.set(key, value, timeout)
  cache.get(key)
  cache.add(key, value)
  cache.get_or_set(key, value, timeout)
  cache.set_many(dict, timeout)
  cache.get_many(key_list)
  cache.delete(key)
  cache.delete_many(key_list)
  ```

+ 浏览器缓存

  强缓存

  > 响应头 Expires （绝对时间）
  >
  > 响应头 Cache-Control （相对时间）

  协商缓存

  ```
  Last-Modified 响应头
  If-Modified-Since 请求头
  
  Etag 响应头
  If-None-Match 请求头
  ```



## 中间件

+ 配置path（settings.py）

  ```
  'middleware.middleware.middleware_class_name'
  ```

+ 使用（middleware/middleware.py）

  ```python
  from django.utils.deprecation import MiddlewareMixin
  
  
  class MW(MiddlewareMixin):
      def process_request(self, request):
          print('MW process_request ---')
      def process_view(self, request, callback, callback_args, callback_kwargs):
          print('MW process_view ---')
      def process_response(self, request, response):
          print('MW process_response')
          return response
  ```

+ csrf

  ```
  {% csrf_token %}
  
  @csrf_exempt  #局部关闭视图函数 
  ```



## 分页

```python
paginator = Paginator(object_list, per_page)  # 构造

# 属性
count
num_pages
page_range
per_page  # 每页数据个数


page = paginator.page(页码)  # 返回Page对象

# 属性
object_list
number  # 当前页
paginator  # Paginator对象
has_next
has_previous
has_other_pages
next_page_number
previous_page_number
```



## 文件下载

```python
response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename="file_name.csv"'
writer = csv.writer(response)
writer.writerow(list_content)
```



## 内建用户系统

+ 创建用户

  ```
  user = User.objects.create_user()
  
  user = User.objects.create_superuser()
  ```

+ 删除用户

  ```
  user = User.objects.get(key=value)
  user.is_active = False
  user.save()
  ```

+ 校验密码

  ```
  user = authenticate(username=username, password=password)  # 返回user对象/None
  ```

+ 修改密码

+ 登录状态保存

  ```
  user = authenticate(username=username, password=password)
  login(request, user)
  ```

+ 登录状态校验

  ```
  @login_required
  ```

  配置（settings.py）

  ```
  # 未登录情况下的跳转地址
  LOGIN_URL = '/login/'
  ```

+ 登录状态取消

  ```
  logout(request)
  ```

+ 扩展字段

  > 配置（settings.py）
  >
  > ```
  > AUTH_USER_MODEL = 'app.model_class_name'
  > ```
  >
  > 继承
  >
  > ```
  > class UserNew(AbstractUser):
  > ```



## 文件上传

+ 表单<form>（html）

  ```
  enctype="multipart/form-data"
  ```

+ 配置（settings.py）

  ```
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

+ 添加路由（主urls.py）

  ```
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

+ ORM 字段 

  FileField(upload_to='子目录名')



## 邮件

SMTP 推送

IMAP 拉取

POP3 拉取

+ 配置（settings.py）

  ```
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.qq.com'
  EMAIL_PORT = 25
  EMAIL_HOST_USER = 'xxxx@qq.com'
  EMAIL_HOST_PASSWORD = '******'
  EMAIL_USE_TLS = False
  ```

+ 使用

  ```python
  mail.send_mail(subject='主题', message='内容', from_email='发件人', recipient_list='收件人')
  
  # middleware.py 邮件告警
  class ExceptionMW(MiddlewareMixin):
  
      def process_exception(self, request, exception):
          error = traceback.format_exc()
          mail.send_mail()
          return HttpResponse()
  ```





