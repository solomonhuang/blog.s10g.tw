title: [Paper Study] Mant-to-one, many-to-many protocol
slug: paper-study-many-to-one
date: 2017-06-28 17:57:34
category: paperstudy
tags: infocom, wireless, protocol

這一篇 INFOCOM 2017 的論文提出的 protocol 是為了改善低功耗產品 (如：ZigBee) 中，同時要把 data 回傳給同一個 node 的情況下，減少碰撞，減少 radio-on time。另外就是多個 node 要把自己的資料傳遞給其他 node，同時也是要減少碰撞與 radio-on time。

* 論文題目：Design and Application of a Many-to-OneCommunication Protocol
* 作者：Sudipta Saha, Mun Choon Chan

直接看圖講重點

# Many-to-one: SyncMerge

> 架構圖

![Many to one](/images/2017-06-28-many-to-one.png "many to one")

圖中的 (b) 就是 source nodes 要回應資料給 initiator。

> 四個 source nodes 要傳送回應資料

![](/images/2017-06-28-many-to-one-reps.png)

這邊有幾個前提：

* 每個 source nodes 的 header 是一樣的。
* initiator 發出的 INIT 封包中已經讓全部的 source nodes 知道自己的傳送順序。
* 時間同步靠 INIT 封包

所以每個 source nodes 同時發射 header segment，這樣可以確保訊號被正增強，收到的內容是對的。然後每個 source nodes 在自己的傳送時間把 txpower 調到最大，不是自己的時間就把 txpower 關掉或是調到最小，進而達到不會相互碰撞的結果。

# Many-to-many: ByteCast

Many-to-many 利用了 many-to-one 的方式改善。直接看底下的圖。

圖中的 (a) 指出這是一個雙層四 nodes 的架構，(b) 是作者的 ByteCast，(c) 是另一篇論文提出的 Chaos 方法。

ByteCast 在兩層的架構只要三步就讓每個 node 都拿到全部的資料了。

1. Layer 1 的 node 1 TX，node 2-4 收到 data 1
2. Layer 2 的 node 2-4 分別在各自的時間點 TX，node 1 收到 data 2-4。此時 node 1 有了 data 1-4。
3. Node 1 TX，node 2-4 都拿到自己所欠缺的 data。

> 雙層架構模擬圖

![](/images/2017-06-25-many-to-many.png)
