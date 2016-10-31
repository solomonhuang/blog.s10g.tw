title: Kernel Support for miscellaneous Binary Formats
slug: linux-kernel-binfmt
date: 2016-10-20T03:09:43T+0800
category: note
tags: linux, kernel, binfmt

Linux Kernel 文件 [binfmt_misc.txt](https://www.kernel.org/doc/Documentation/binfmt_misc.txt) 提到的功能。主要就是告訴 kernel 如果把特定的檔案當成執行檔來呼叫。判斷的方式分成 extension 及 magic。

### 第一步掛載 binfmt_misc

```
:::bash
mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc 
```

### 向 binfmt 註冊你的格式

註冊字串組成

```
:name:type:offset:magic:mask:interpreter:flags
```

* name 是識別用的字串，註冊後會出現在 `/proc/sys/fs/binfmt_misc`
* type 有 `M` 與 `E`。`M` 就是 magic number，`E` 則是 extension。
* offset 是 magic 與 mask 的位移量，預設值是 `0`。
* magic 是 binfmt 要拿來比較的 binary file 的。
* mask 也是 binfmt 在比較 magic 時會拿來當遮罩用的。
* interpreter 就是實際要呼叫的程式，而你的檔案會是 interpreter 第一個參數
* flags 略

範例 lua 用 luac 編過的 binary file

```
:::bash
echo ':luac:M:0:\x1b\x4c\x75\x61::/usr/bin/lua:' > /proc/sys/fs/binfmt_misc/register
```
