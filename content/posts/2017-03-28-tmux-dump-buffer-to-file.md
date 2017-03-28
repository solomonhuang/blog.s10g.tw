title: Tmux dump buffer to file
slug: tmux-dump-buffer-to-file
date: 2017-03-28T16:53:03T+0800
category: note
tags: tmux, linux, utlls


### 將 `tmux` buffer 中的資料寫到檔案中

參考 [Unix stackexchange](http://unix.stackexchange.com/questions/26548/write-all-tmux-scrollback-to-a-file)

> prefix + :, then type in capture-pane -S -3000

上面這行把 3000 行的資料複製到 buffer 中。

> prefix + : again, and type in save-buffer filename.txt

上面這行把 buffer 中的資料寫到 `filename.txt` 中

`prefix` 預設值是 `Ctrl+b`
