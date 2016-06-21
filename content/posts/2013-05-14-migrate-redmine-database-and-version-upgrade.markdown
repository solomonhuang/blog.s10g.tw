---
layout: post
title: "Redmine 升級與更換資料庫"
date: 2013-05-14 20:25
comments: true
category: note
tags: redmine, ruby, sysadmin
---

最近要把 Redmine 從 1.1.0 升級到最新的 2.3.1。附帶將資料庫從 MySQL 換成 PostgreSQL。跑去了 [serverfault][1]
問這個應該怎麼做比較安全。配合一些工具之後，升級一點痛苦也沒有。

<!--more-->

幾個主要的重點。

 1. 搬資料庫用 taps 很方便。可以把整個 database 搬好。Table 應該都有搬過來。只有兩個重點要注意：

    * UTF8 的問題。這個可以在 taps 的 server 端加上 `?encoding=UTF8` 來解決。
    * RACK 相依性的問題。這個安裝 Rack 1.0.1 就可以了。
``` bash
gem install taps
gem uninstall rack
gem install rack --version 1.0.1
```

 2. 在新的機器上準備好 redmine。再把資料庫跟信箱的設定設好。就可以執行 db:migrate 了。
 3. 我用 thin 配合 nginx。要記得在 `Gemfile.local` 加上 `thin` 這個 gem。不然在 rvm 的環境下會跑不起來。

[1]: http://serverfault.com/questions/506884/how-to-migrate-old-redmine-server-to-new-one-with-version-upgrade-and-database-c 
