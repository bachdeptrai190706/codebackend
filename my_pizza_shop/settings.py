import os
from pathlib import Path

# Đường dẫn gốc của project
BASE_DIR = Path(__file__).resolve().parent.parent

# Bảo mật
SECRET_KEY = 'django-insecure-thay_bang_chuoi_bi_mat_cua_ban'

# Phát triển (DEBUG=True) => khi deploy cần đặt DEBUG=False
DEBUG = True

# Cho phép chạy trên localhost
ALLOWED_HOSTS = []

# Ứng dụng được cài
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pizza_shop',  # ứng dụng bạn tạo
]

# Middleware cần thiết
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Bắt buộc cho admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Bắt buộc
    'django.contrib.messages.middleware.MessageMiddleware',      # Bắt buộc
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Định nghĩa gốc URL
ROOT_URLCONF = 'my_pizza_shop.urls'

# Cấu hình Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Bạn có thể thêm đường dẫn nếu dùng template riêng
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI cho server
WSGI_APPLICATION = 'my_pizza_shop.wsgi.application'

# Cấu hình CSDL (mặc định là SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Kiểm tra password
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Cài đặt ngôn ngữ và múi giờ
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Cấu hình file tĩnh (CSS, JS, ảnh…)
STATIC_URL = '/static/'

# Tên default cho primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

