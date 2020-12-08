# OBS - Open Book Star
## A cool tool for your open book test
---
<br>

## Dependency
> Python >= 3.7 (The develope version is 3.7.9) <br>
> All needed packages are listed in ```requirements.txt```
<br>

## Getting Started
### Be sure you can run ```jupter notebook``` on your device
### Be sure all your document are in the directory
### The clearly example code is in the jupyer-notebook file ```search_test.ipynb```

```python=
''' in your terminal'''
$ jupyter notebook

''' notebook cell-[1] '''
from OBS.obs import OBS

''' notebook cell-[2] '''
DOC_PATH = 'doc'

''' notebook cell-[3] '''
if __name__ == '__main__':
    obs = OBS(DOC_PATH)
    obs.load()

''' notebook cell-[4] '''
q = 'what is compiler'

''' notebook cell-[5] '''
# query-mode-1 : query by match
obs.query_by_match(q, view=5)

''' notebook cell-[6] '''
# query-mode-2 : query by word token
obs.query(q, 20)

```
