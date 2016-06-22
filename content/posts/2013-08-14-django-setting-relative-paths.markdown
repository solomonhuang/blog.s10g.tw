---
layout: post
title: Django setting 設定相對路徑
date: 2013-08-14 14:12
comments: true
category: note
tags: python, django
---

Django 的 `settings.py` 中要設定相關的 template, media 路徑都需要絕對路行。但是往往我們需要相對路徑來符合實際需求。

只要在 `settings.py` 加入簡單的幾行就可以達成這個需求。

```
import os
import django

DJANGO_PATH = os.path.dirname(os.path.realpath(django.__file__))
SITE_PATH = os.path.dirname(os.path.realpath(__file__))
```

`DJANGO_PATH` 與`SITE_PATH` 這兩個變數就可以在後面使用。

```
MEDIA_ROOT = os.path.join(SITE_PATH, 'assets')
```

搞定，收工。

