title: docker 更新 jenkins
slug: docker-jenkins-update
date: 2016-09-13T16:39:18T+0800
category: note
tags: docker, jenkins

因為自己家的 jenkins 是用 docker 裝的，紀錄一下自動更新 weekly 版本的方式。

### 安裝 jenkins

照著 jenkins 自己的[正式文件](https://github.com/jenkinsci/docker/blob/master/README.md)來做。這邊就不寫了。

我的選擇是建一個 jenkins 專用的 volume image。run jenkins container 的時候再掛上來。這樣子的好處是不會看到亂亂的目錄，雖然說實際上還是存在系統上。但是我就不用額外指定了。

### 自動更新 jenkins

重點只是要紀錄一下我自己用的 script。

```
#!/bin/bash

docker pull jenkinsci/jenkins
docker stop jenkins_container
docker rm jenkins_container
docker run --name jenkins_container --restart=always -p 127.0.0.1:8081:8080 -p 50000:50000 --volumes-from jenkins_data -d jenkinsci/jenkins
```

jenkins_container 是我的容器名字，jenkins_data 是我的資料容器。

另外因為我自己的機器跑了不同服務，所以把 8080 mapping 到 127.0.0.1:8081。上面的 script 丟到 cron 去跑就好了。
