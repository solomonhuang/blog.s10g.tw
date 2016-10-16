title: Pelican 裝 ligquid tags plugin
slug: plugin-liquid-tags-graphviz
date: 2016-10-17T00:19:48T+0800
category: note
tags: graphviz, pelican, python


為了之後要畫圖方便，加裝了 [ligquid tags](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags) 的 plugin。方法很簡單只要加入 `PLUGIN_PATHS` 與 `PLUGIN` 即可。

```
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['liquid_tags.graphviz']
```

之後底下的 dot 語言就可以畫出 graphviz 的圖了。

```
{% graphviz
    dot {
        digraph graphname {
            a -> b -> c;
            b -> d;
        }
    }
%}

```
{% graphviz
    dot {
        digraph graphname {
            a -> b -> c;
            b -> d;
        }
    }
%}


### 但是

因為我用的是 Python 3 會因為 `base64.b64encode` 會輸出 byte string。這會導致 inline base64 encodeing 的格式跑掉，所以圖會出不來。改了一下程式碼發了個 [PR #798](https://github.com/getpelican/pelican-plugins/pull/798)。

底下是 python 3 的執行結果，只要加了 `decode('utf-8')` 就可以了。

```
>>> print(base64.b64encode(b'\01'))
b'AQ=='
>>> print(base64.b64encode(b'\01').decode('utf-8'))
AQ==
```

