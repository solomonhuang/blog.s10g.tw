title: VirtualBox 發生 VERR_INTNET_FLT_IF_NOT_FOUND 錯誤
slug: virtualbox-interface-not-found
date: 2016-08-11T11:34:46+0800
category: note
tags: virutalbox, windows

升級了 Windows 10 的年度更新之後，VirtualBox 就找不到 host only 網卡了。解決方式很簡單，就是把 `VirtualBox Host-Only Ethernet Adapter` 網卡的 `VirtualBox NDIS6 Bridge Networking Driver` 打開就可以了。

![乙太網路內容](/images/2016-08-11-virtualbox-interface-not-found.png "乙太網路內容")

