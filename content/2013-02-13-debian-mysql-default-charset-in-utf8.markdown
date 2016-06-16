---
layout: post
title: "MySQL 設定 utf8 為預設 charset"
date: 2013-02-13 23:41
slug: debian-mysql-default-charset-in-utf8
comments: true
categories: [mysql, utf8, utf8mb4, unicode]
---

因為 debian 預設還是 latin1 所以找了一下如何設定。有一種設定在 5.5.x(不確定哪一版開始) 之後會讓 mysqld 開不起來。

```
[mysqld]
default-character-set = utf8
```
上面這個設定是錯的，底下才是對的。

<!--more-->

```
[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
init-connect = 'SET NAMES utf8mb4'

```
mysqld 的部分不能用 ```default-character-set```。

找了一下資料才發現 ```utf8``` 與 ```utf8mb4``` 不同。MySQL 中 ```utf8mb4``` 才能完全紀錄 unicode 的碼點。
可以參考：

* [How to support full Unicode in MySQL databases][1] ([Mathias Bynens][2])
* [The utf8mb4 Character Set (4-Byte UTF-8 Unicode Encoding)][3]
* [change mysql default character set to UTF8 in my.cnf?][4]

[1]: http://mathiasbynens.be/notes/mysql-utf8mb4
[2]: http://mathiasbynens.be/
[3]: http://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html
[4]: http://stackoverflow.com/questions/3513773/change-mysql-default-character-set-to-utf8-in-my-cnf

