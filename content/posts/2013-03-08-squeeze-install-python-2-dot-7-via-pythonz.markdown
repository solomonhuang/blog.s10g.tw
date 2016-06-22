---
layout: post
title: Debian Squeeze install python 2.7 via pythonz
date: 2013-03-08 16:05
comments: true
category: note
tags: debian, squeeze, python
---

要配合 vitrualenv 有幾個重點：

 * 安裝 pythonz
 * 用 pythonz 安裝 2.7.x
 * 從 pythonz 的 build.log 來看少哪些 module，把相對應的 dev package 補上。
 * 再把裝好的 python 2.7.x 路徑放到 PATH。
 * 安裝 `easy_install` (setuptools)
 * 安裝 `pip`
 * 從 `pip` 安裝 `vitrualenv`

參考 [pythonz install Debian Squeeze][1]

[1]: http://note.harajuku-tech.org/pythonz-install-debian-squeeze

