title: pdftk 移除 pdf 的浮水印
slug: pdf-watermark-remove
date: 2017-06-19 00:42:05
category: note
tags: pdf, linux, pdftk, watermark


### 目標：移除 pdf 中的文字浮水印

手上有一些 pdf 有浮水印，突然想要移除看看。找了一下 [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) 可以做到這件事。Superuser 上的 [How to remove watermark from pdf using pdftk?](https://superuser.com/questions/448519/how-to-remove-watermark-from-pdf-using-pdftk) 寫得很清楚又簡單。

**做修改之前應該要先備份原檔**

**做修改之前應該要先備份原檔**

**做修改之前應該要先備份原檔**

### 步驟

#### 1. 把壓縮過的 pdf 解壓縮

如果你的 pdf 有被壓縮，要先解壓縮

```
:::bash
pdftk input.pdf ouput uncompress.pdf uncompress
```

#### 2. 把浮水印的文字去除

```
:::bash
sed -e "s/watermarktextstring/ /g" uncompress.pdf > unwatermarked.pdf
```

#### 3. 修復破損的 pdf

```
:::bash
pdftk unwatermarked.pdf output result.pdf
```

如果要壓縮，加上 `compress`

```
:::bash
pdftk unwatermarked.pdf output result.pdf compress
```
