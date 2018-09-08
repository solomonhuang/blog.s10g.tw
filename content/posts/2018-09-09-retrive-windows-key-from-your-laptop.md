title: 取得 windows 的序號
slug: retrive-windows-key-from-your-laptop
date: 2018-09-09 01:11:52
category: note
tags: windows, linux


買 notebook 通常會有隨機安裝的 windows，但是像我已經裝了 linux 如果重新安裝 windows 沒有序號怎麼辦？

只要一行指令

```
sudo cat /sys/firmware/acpi/tables/MSDM | tail -c 32 | xargs -0 echo
```

ref. [Brandon Prry](https://twitter.com/BrandonPrry/status/1038269038881898498)
