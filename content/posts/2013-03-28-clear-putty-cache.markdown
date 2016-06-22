---
layout: post
title: Clear putty cache
date: 2013-03-28 16:42
comments: true
category: note
tags: putty, windows
---

PuTTY 的 ssh 連線可以把 host key cache 起來。

`HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\SshHostKeys`

上面這個就是 host key 存的地方。找到相對應的機碼就可以刪掉了。
