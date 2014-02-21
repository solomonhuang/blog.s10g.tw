---
layout: post
title: "apt preferences pinning"
date: 2014-02-21 15:10:26 +0800
comments: true
categories: [apt, preferences, debian]
---

將 debian stable 加入 testing 但是只在需要安裝 testing 套件的時候才安裝。

# 在 `/etc/apt/sources.list` 加入 `testing`
# 在 `/etc/apt/preferences.d/` 建立 `testing` 檔案。內容如下
```
Package: *
Pin: release a=testing
Pin-Priority: 200
```


這樣就可以在 `aptitude` 中選擇 `testing` 的套件。或是用 `apt-get -t testing install <package>` or `aptitude -t testing` 來指定安裝 `testing` 套件。

