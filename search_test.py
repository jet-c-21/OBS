"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2020/12/7
"""
# coding: utf-8
from OBS.obs import OBS

DOC_PATH = 'doc'

if __name__ == '__main__':
    obs = OBS(DOC_PATH)
    obs.load()

    q = 'DFA CFG'

    obs.query_by_match(q, view=5)
    obs.query(q, 20)


