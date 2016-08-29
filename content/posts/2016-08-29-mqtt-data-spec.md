title: MQTT 資料格式
slug: mqtt-data-spec
date: 2016-08-29T23:38:32+0800
category: note
tags: mqtt, iot, protocol

看了一下 [MQTT](http://mqtt.org/documentation) 的文件，隨手紀錄一下。

### 資料格式的表示

* 位元組 bit 0 ~ bit 7
    * bit 0 是 least significant bit, bit 7 是 most sigificant bit
* 整數
    * big endian 排列的 16 bits 數字，也就是最大是 65535。
* 字串
    * UTF-8 編碼
    * 字串長度從 0-65535
    * 字串結構中，前兩個 byte 放整數，表示 UTF-8 編碼字串的位元組長度。

### 控制封包結構

* 固定表頭
    * 全部的 MQTT control packet 都有
    * 佔 `1+n` bytes，n = 1-4
    * byte 1, bits 7-4 是 control packet type
    * byte 1, bits 3-0 是 flags
    * remaining length 是後續變動表頭與 payload 的長度
        * 1 byte 只能表示 127
        * 大於 127 的時候，把每個 byte 的 bit 7 OR 1 來表示下個 byte 還是表示長度
        * 1 byte `0 (0x00)` to `127 (0x7F)`
        * 2 bytes `128 (0x80, 0x01`) to `16 383 (0xFF, 0x7F)`
        * 3 bytes `16384 (0x80, 0x80, 0x01)` to `2097151 (0xFF, 0xFF, 0x7F)`
        * 4 bytes `2097152 (0x80, 0x80, 0x80, 0x01)` to `268435455 (0xFF, 0xFF, 0xFF, 0x7F)`
* 變動表頭
    * 2 bytes 的 packet identifier
* 資料 payload
    * 只有下列控制封包有 payload
        * CONNECT
        * PUBLISH (optional)
        * SUBSCRIBE
        * SUBACK
        * UNSUBSCRIBE

