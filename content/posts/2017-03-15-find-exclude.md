title: Find 排除目錄
slug: find-exclude
date: 2017-03-15T16:04:32T+0800
category: note
tags: find, linux, utlls

使用 find 可以很簡單的找出目標檔案來做處理，記錄一下要排除特定目錄怎麼做。

### 目標是排除 .git 下的所有檔案

```
:::bash
find . -path "./.git/*" -prune -o -type f -exec blahblah {} \;
```

`blahblah` 就是要對每個檔案做處理的程式。

### 單元解釋

```
:::bash
-path "./.git/*" -prune
```
除去 (`-prune`) 路徑符合 `./.git/*` 的部分

```
:::bash
-o -type f -exec blahblah {} \;
```
或者是 (`-o`) 找出類別是檔案 (`-type f`) 的項目交給程式處理 ( `-exec blahblah {} \;` )
