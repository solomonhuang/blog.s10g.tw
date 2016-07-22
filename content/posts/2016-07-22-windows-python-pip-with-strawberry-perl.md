title: pip 在 windows 下無法使用
slug: windows-python-pip-with-strawberry-perl
date: 2016-07-22T16:20:00+0800
category: note
tags: python, pip, perl

紀錄一下，主要原因是因為我同時安裝了 [Strawberry Perl](http://strawberryperl.com/)。

輸入 `where pip` 查詢一下，

```
C:\Strawberry\perl\bin\pip
C:\Strawberry\perl\bin\pip.bat
C:\Users\Solomon\AppData\Local\Programs\Python\Python35-32\Scripts\pip.exe
```

所以直接打 `pip` 就會出現奇怪的訊息。因為執行到 Strawberry 的 `pip` 了。

```

Did not provide a command

```

解決方式就是調整一下 PATH 環境變數，或是使用完整路徑。
