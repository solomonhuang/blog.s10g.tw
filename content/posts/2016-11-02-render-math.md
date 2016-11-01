title: Tex 數學式
slug: tex-math
date: 2016-11-02T02:33:03T+0800
category: note
tags: tex, math


[render_math](https://github.com/getpelican/pelican-plugins/tree/master/render_math) 可以把 tex 語法的數學式畫出來。語法參考 [MathJax](http://docs.mathjax.org/en/latest/tex.html)


### 範例 - inline

```
:::tex
$e=mc^2$
```
這是行內數學式的範例： $e=mc^2$ 這樣就可以了。

### 範例 - block 

```
:::tex
$$e=mc^2$$
```

$$e=mc^2$$

### 範例 - block with label

```
:::tex
\begin{equation}
    \label{eq}
    X^2
\end{equation}

\begin{equation}
    \label{eq2}
    e=mc^2
\end{equation}

Ref: \ref{eq}

Ref: \ref{eq2}

\begin{array}{cc}
  a & b \\
  c & c
\end{array}

```


\begin{equation}
    \label{eq}
    X^2
\end{equation}

\begin{equation}
    \label{eq2}
    e=mc^2
\end{equation}

Ref: \ref{eq}

Ref: \ref{eq2}

\begin{array}{cc}
  a & b \\
  c & c
\end{array}
