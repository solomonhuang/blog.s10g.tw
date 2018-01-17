title: Call Call Graph 
slug: call-call-graph
date: 2018-01-09 19:03:47
category: note
tags: cscope, graphviz, dot,

為了讀 [OAI](https://gitlab.eurecom.fr/oai/openairinterface5g) 的程式碼，一直找一些 call graph 的工具。最後用了 [chihchun](https://github.com/chihchun) 好久以前寫的 [callgraphviz](https://github.com/chihchun/callgraphviz) 來改成 [Call Call Graph](https://github.com/solomonhuang/callcallgraph)。

叫 Call Call Graph 只是因為我要畫 caller 與 callee。大架構沒有改太多，還是照原本的用 cscope 當後端的資料庫。查詢後生出 dot 的圖再餵給 xdot 來畫圖。花最多時間的就是查 python 3 的語法及 PyGObject 的 api。

我自己加了可以把現在的查詢資料清掉的功能，只要按一下 reload 鈕就可以清掉。不然累積太多查詢會造成節點太多。另外加了可以忽略特定 symbol 的功能，因為我會把 function 的 caller 與 callee 都找出來。所以像是 `memset`、`printf` 或是 debug function 可以濾掉，不然會有太多噪音。

之後有空的話，會再把 function 所在的目錄與檔名加到圖上，可能還要用目錄來切 cluster。不然大專案還是不知道這些 caller/callee 在哪裡。

最後附圖

### 查 linux-4.14.12 的 add_del_if

![add_del_if](/images/2018-01-09-linux-4.14.12-add_del_if.png "add_del_if")

