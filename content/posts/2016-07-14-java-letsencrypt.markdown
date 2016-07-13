title: Java 與 Let's Encrypt
slug: java-letsencrypt
date: 2016-07-01T12:33:44+0800 
category: note
tags: java, tls, letsencrypt

在弄 Jenkins windows slave 的時候踩到 Java 還沒有把 [Let's Encrypt](https://letsencrypt.org) 的根憑證放到信任清單中。弄了半天才真的搞定。

[stackoverflow](http://stackoverflow.com/questions/34110426/does-java-support-lets-encrypt-certificates) 上有人說了，Oracle Java 8u101 就會放進去了。

ref. [JDK-8154757](https://bugs.openjdk.java.net/browse/JDK-8154757)


