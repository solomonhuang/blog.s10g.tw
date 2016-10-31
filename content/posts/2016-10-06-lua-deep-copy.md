title: lua 複製物件
slug: lua-deep-copy
date: 2016-10-06T13:31:55T+0800
category: note
tags: lua

之前踩到一個坑，因為沒注意到指定 array table 中的物件時是 reference 到原有物件，所以整個 table 中的東西都長得一樣，而且還牽一髮動全身。解決方式就是複製生出新的物件。

```
:::lua
function deepcopy(orig)
	local orig_type = type(orig)
	local copy
	if orig_type == 'table' then
		copy = {}
		for orig_key, orig_value in next, orig, nil do
			copy[deepcopy(orig_key)] = deepcopy(orig_value)
		end
		setmetatable(copy, deepcopy(getmetatable(orig)))
	else -- number, string, boolean, etc
		copy = orig
	end
	return copy
end
```
