---
layout: post
title: gitlab cannot locate ruby with rvm
date: 2013-10-25 11:32
comments: true
category: note
tags:  git, gitlab, rvm, ruby 
---

Gitlab 安裝時若採用 rvm 的 ruby 而不是安裝在 system 上，在 push 的時候會被抱怨找不到 ruby 或是執行到系統的 ruby。

最簡單的解決方式：將 user git 的 .bashrc 中的 `PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting` 移到最前面就可以了。

