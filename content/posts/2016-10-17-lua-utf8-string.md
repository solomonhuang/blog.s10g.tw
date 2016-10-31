title: Lua 處理 UTF-8 字串
slug: utf8-string-in-lua
date: 2016-10-17T16:38:52T+0800
category: note
tags: lua, utf8


最近要用 Lua 處理 UTF-8 字串，但是 Lua 到了 [5.3](http://www.lua.org/manual/5.3/manual.html#6.5) 才開始支援 UTF-8。

## UTF-8 字串長度及複製

我的需求很簡單，只要判斷字串長度及類似 `strncpy` 的字串複製。所以直接利用 [Lua 5.3 手冊](http://www.lua.org/manual/5.3/manual.html#6.5) 提到的 charpattern 來進行字串的操作。

```
[\0-\x7F\xC2-\xF4][\x80-\xBF]*
```

### utf8len

```
:::lua
function utf8len(s)
    _, len = string.gsub(s, '([\0-\x7F\xC2-\xF4][\x80-\xBF]*)', '%1')
    return len
end
```

### utf8strncpy

```
:::lua
function utf8strncpy(s, len)
    local result = ''
    local count = 0
    for c in string.gmatch(s, '([\0-\x7F\xC2-\xF4][\x80-\xBF]*)') do
        if count >= len then
            return result
        end
        result = result .. c
        count = count + 1
    end
    return result
end
```

### 範例

```
:::lua
a = '天天開心一二三四abcd'

print('length: #:' .. #a)
print('length: utf8len:' .. utf8len(a))
print(utf8strncpy(a, 1))
print(utf8strncpy(a, 3))
print(utf8strncpy(a, 5))
print(utf8strncpy(a, 7))
print(utf8strncpy(a, 9))
print(utf8strncpy(a, 11))
print(utf8strncpy(a, 13))
print(utf8strncpy(a, 15))
```

```
length: #:28
length: utf8len:12
天
天天開
天天開心一
天天開心一二三
天天開心一二三四a
天天開心一二三四abc
天天開心一二三四abcd
天天開心一二三四abcd
```

