title: Python 安裝 matlab engine
slug: install-the-matlab-engine-for-python
date: 2019-05-21 11:56:15
category: note
tags: matlab, python, ubuntu, linux


Matlab 有教學，其實很簡單。主要是記錄一下如果是要安裝在 virtualenv 中的時候要怎麼辦。

* 找出 python 套件的目錄。在 matlab 的命令列輸入底下的指令，就會得到目錄
```matlab
fullfile(matlabroot,'extern','engines','python')
```

* 在你的 python virtual env 中，切換剛剛得到的目錄。再打下面的指令就可以安裝。

```bash
python setup.py install
```

現在就可以在 python 使用 matlab engine 了。
```python
import matlab.engine
eng = matlab.engine.start_matlab()
eng.sqrt(4.0)
eng.quit()
```

ref. [Install MATLAB Engine API for Python](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

ref. [Install MATLAB Engine API for Python in Nondefault Locations](https://www.mathworks.com/help/matlab/matlab_external/install-matlab-engine-api-for-python-in-nondefault-locations.html)
