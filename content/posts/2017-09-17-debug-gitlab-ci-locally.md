title: 本地 debug GitLab CI
slug: debug-gitlab-ci-locally
date: 2017-09-17 23:55:00
category: note
tags: gitlab, gitlab-ci


最近在自己的小專案設定 GitLab-CI 發生了很多問題，但是 debug 很麻煩。每次都要修改再 push。於是找了一下發現可以很簡單的本地端 debug。

* 安裝 docker
* 安裝 gitlab-ci-multi-runner
* 執行 `gitlab-ci-multi-runner exec docker {test_name}`

收工

ref. [How to: Debug GitLab CI Builds Locally](https://substrakt.com/how-to-debug-gitlab-ci-builds-locally/)

