title: dropbox 保存密碼的安全措施筆記
slug: dropbox-password
date: 2016-09-24T00:42:11T+0800
category: note
tags: dropbox, security, password

Dropbox 寫了一篇[文章](https://blogs.dropbox.com/tech/2016/09/how-dropbox-securely-stores-your-passwords/)來告訴大家他們如何安全地保存用戶的密碼。我認為蠻有趣的，有一些是我沒有接觸過的。

# 保存密碼的方式

簡單用一行來寫

```
AES256(bcrypt(SHA512(PASSWORD)))
```

* AES256 加密用的是另外存的金鑰 (global pepper)，每個用戶都一樣。
* bcrypt 做 hash 的 salt 是每個使用者分開的，強度是 10
    * 這是引起我細讀的地方

# bcrypt 是什麼

[bcrypt](https://en.wikipedia.org/wiki/Bcrypt)是基於[Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher))所發展出來的 hash function。因為有 salt 的關係，所以可以對抗 rainbow table 的攻擊。

同時，bcrypt 的 cost (上面寫的強度)會以 2 的 cost 次方來增加運算次數。這樣子可以增加暴力破解的難度。而且 bcrypt 的設計就是慢又很難用客製硬體(我想就是 FPGA，ASIC 之類的吧)及 GPU 來加速。

# Dropbox 的選擇

同時 Dropbox 也解釋了為什麼用這樣子的技術實現。

### 為什麼密碼要先經過 SHA512 再用 bcrypt

這解決了兩個問題

1. 有一些 bcrypt 的實做會把 input 切成 72 bytes，這降低了密碼的熵。
2. 避免 DoS 攻擊。其他不把 input 剪掉的 bcrypt 實做會因為 input 太長而消耗 server 的計算資源，從而達到 DoS 的效果。

所以用 SHA512 把任意長度的密碼 hash 成固定長度的值直接處理了上面兩種 bcrypt 實做會碰到的問題。

### 還有什麼？

* 為什麼不用 scrypt 或 argon2 來取代 bcrypt？
    * 比較會用 bcrypt
    * argon2 在未來的考慮清單中
    * bcrypt 從 1999 年發表到現在沒有被發現任何嚴重的弱點
* 為什麼用 global pepper (就是 AES256 的加密金鑰) 來給密碼 hash 值加密，而不是再做一次 hash？
    * 因為用 global pepper 來做 hash 的話，就很難換掉 hash salt 了。
    * 加密的方式提供了類似的安全性，但是同時也可以定期更換。
    * 上面這兩點我沒有真正理解所謂的類似的安全性是什麼。
