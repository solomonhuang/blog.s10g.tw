title: [Paper Study] ACT-AP
slug: paper-study-ACT-AP
date: 2017-06-28 16:59:29
category: paperstudy
tags: infocom, wireless, wifi, multicast


這篇 INFOCOM 2017 的論文主要目的是只修改 AP 的軟體而不修改 client 端的運作前提下，讓 multicast 封包的送達率提高。

* 論文題目：ACT-AP: ACTivator Access Point for Multicast over WLAN
* 作者：Gyujin Lee, Yeonchul Shin, Jonghoe Koo, Junyoung Choi, and Sunghyun Choi

# 問題簡述

大多數的 WiFi client 為了省電會進到 power saving mode(PSM)，在 PSM 情況下 client 往往會收不到 AP 發射出來的 multicast 封包。作者設計了 ACT-AP 讓 client 不會因為 PWM 而沒收到 multicast 封包。

# 主要問題

一般市售 WiFi client 有三種情況會造成 PDR (packet deliver rate) 下降。

* ReceiveDTIMs off
    - 收到 DTIM 但是沒有反應
* Early sleep
    - 太早睡覺了
* Inappropriate wakeup
    - 因為送了 NULL-DATA(PM bit 0) 之後沒多久，就又送了 NULL-DATA(PM bit 1)，進入 PSM。

![undesired functions](/images/2017-06-28-ACT-AP-undesired-functions.png "undesired functions")

# 解決方案

在 AP 端發 ACT-packet(1 byte 的 data)，讓 client 端保持清醒。

![ACT-AP desgin](/images/2017-06-28-ACT-AP-design.png "ACT-AP desgin")

圖中的重點是 `ACT-packet Interval Controller`。作者的演算法會去逼近 client 的 tail time(沒收到封包進入PWM的時間)，在 tail time 結束前對 client 發 ACT-packet，所以 client 就可以醒著接收 multicast 封包了。

