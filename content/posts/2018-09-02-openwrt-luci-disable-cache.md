title: OpenWRT-LuCi disable cache
slug: openwrt-luci-disable-cache
date: 2018-09-02 09:21:52
category: note
tags: openwrt, luci


非常簡單

```
uci set luci.ccache.enable=0; uci commit luci
```

ref. [Development Environment How To](https://github.com/openwrt/luci/wiki/DevelopmentEnvironmentHowTo)
