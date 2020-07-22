from ppt2json import PPT2JSON
import os
import json
from collections import Counter


class SM:
    def __init__(self, ppt_dir_path: str):
        self.ppt_dir = ppt_dir_path
        self.data = list()
        self.__load_all_ppt()

    def __load_all_ppt(self):
        for ppt in os.listdir(self.ppt_dir):
            ppt_path = f'{self.ppt_dir}/{ppt}'
            ppt_json = PPT2JSON(ppt_path).get_json()
            self.data.append(json.loads(ppt_json))

    def search(self, words: str):
        ppt_list = list()
        pages_list = list()

        for ppt in self.data:
            for slide in ppt['slides']:
                if words in slide['text']:
                    # print('File name: {} - Page: {}'.format(ppt['name'], slide['page']))
                    ppt_list.append(ppt['name'])

        return dict(Counter(ppt_list))

