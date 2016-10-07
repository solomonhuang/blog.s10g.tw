title: Lua 中的 ipairs 與 pairs 的差異。
slug: difference-between-ipairs-and-pairs-in-lua
date: 2016-10-07T11:31:55T+0800
category: note
tags: lua

# Lua 中的 `ipairs` 與 `pairs` 的差異。

[PIL 7.3 – Stateless Iterators](https://www.lua.org/pil/7.3.html) 中有提到

> ipairs, which iterates over all elements in an array, as illustrated next

及

> The pairs function, which iterates over all elements in a table

也就是說 `ipairs` 是遍歷 array (Lua 中以數字為 index 的 table, 1 為起始)，而 `pairs` 則是遍歷 table 中所有的元素。

__當你把 Lua 的 table 當 array 用的時候，你只有純數字的 key 當 index。這時候就是用 `ipairs` 來迭代。__

__當你把 Lua 的 table 當成 dict 來用的時候，你會有各式各樣的 key。這時候要用 `pairs` 來迭代。__



