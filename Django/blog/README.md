# Django



## 安装 Django



## 创建项目

```
django-admin startproject blog .
```



## 数据库配置（settings.py）

```python
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'w_f1216570180',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

https://docs.djangoproject.com/en/2.2/ref/settings/#databases



## 数据库驱动（安装mysqlclient）

https://docs.djangoproject.com/en/2.2/ref/databases/



## 创建应用

```
python manage.py startapp user
```



## 注册应用（settings.py）

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
]
```



## 模型Model

### 创建User的Model类（models.py）

### 迁移Migration

```
python manage.py migrate
```



## Django后台管理

### 创建管理员

```
python manage.py createsuperuser
```

### 本地化（settings.py）

```python
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'  # 'en-us'

TIME_ZONE = 'Asia/Shanghai'  # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

### 启动WEB Server

```
python manage.py runserver
```

### 登录后台管理

http://127.0.0.1:8000/admin/

### 注册应用模块（admin.py）

```python
from django.contrib import admin

# Register your models here.
from .models import User
admin.site.register(User)
```

## 路由（urls.py）





## 命令

+ url参数获取

  ```python
  # http://127.0.0.1:8000/?num=123
  num = request.GET.get('num')
  ```

+ 页面跳转

  ```python
  redirect()
  ```

+ 命名和反转

  ```python
  name=''
  reverse()
  ```

  

