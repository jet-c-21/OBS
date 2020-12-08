"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2020/12/7
"""
# coding: utf-8
import os
from typing import Union
from tqdm import tqdm

from OBS.cls.doc import Doc
from OBS.pdf_parser import PDFParser
from OBS.search import Search
from OBS.ult import Ult


class OBS:
    def __init__(self, doc_path: str):
        """
        thr recommended structure example:
        - doc
            - math
                - ch1.pdf
                - ch2.pdf
                - doc.pptx

            - history
                - ch1.pdf
                - ch2.pdf
                - doc.pptx

        :param doc_path: str
        """

        self.doc_path = doc_path
        self.library = list()

    @staticmethod
    def _convert_path(root: str, sub_dir: Union[str, list], file_name: str) -> tuple:
        if root and isinstance(root, str):
            root = Ult.path_converter(root)

        if sub_dir and isinstance(sub_dir, str):
            sub_dir = Ult.path_converter(sub_dir)

        if file_name and isinstance(file_name, str):
            file_name = Ult.path_converter(file_name)

        return root, sub_dir, file_name

    @staticmethod
    def _parse_path(root: str, sub_dir) -> tuple:
        r_ls = root.split('/')
        if isinstance(sub_dir, str):
            sub_dir = sub_dir.split('/')

        new_root = r_ls[0]
        if len(r_ls) > 1:
            for t in r_ls[1:]:
                sub_dir.append(t)

        new_sub_dir = ''
        while sub_dir:
            pt = sub_dir.pop(0)
            new_sub_dir += pt
            if sub_dir:
                new_sub_dir += '/'

        return new_root, new_sub_dir

    @staticmethod
    def pprint_result(data: list, view=None):
        if not view:
            view = len(data)

        for i, d in enumerate(data[:view], start=1):
            doc = d[0]
            count = d[1]
            print(f"result - {i}    match: {count}")
            s = f"file name : {doc.name} \n" \
                f"  sub dir : {doc.sub_dir} \n" \
                f"     path : {doc.path}\n"
            print(s)

    def load(self):
        msg = 'loading documents ...'
        Ult.prt_log(msg)

        # load doc meta to library
        for root, sub_dir, files in os.walk(self.doc_path):
            for file_name in files:
                root, sub_dir, file_name = OBS._convert_path(root, sub_dir, file_name)
                root, sub_dir = OBS._parse_path(root, sub_dir)
                doc = Doc(root, sub_dir, file_name)
                if doc.type == 'pdf':
                    self.library.append(doc)

        # self.library = self.library[0:3]

        # extract text for each doc
        text_data = PDFParser.get_text_mp(self.library)
        for doc, text in zip(self.library, text_data):
            doc.text = text

        msg = 'finish loading documents'
        Ult.prt_log(msg)

    def search_by_match(self, q: str) -> list:
        q = q.lower()
        return Search.search_by_match(self.library, q)

    def query_by_match(self, q: str, view=5):
        q = q.lower()
        data = self.search_by_match(q)
        OBS.pprint_result(data, view)

    def search(self, q: str):
        q = q.lower()
        return Search.search_by_token(self.library, q)

    def query(self, q: str, view=5):
        q = q.lower()
        data = self.search(q)
        OBS.pprint_result(data, view)

    def search_mp(self, q: str):
        q = q.lower()
        return Search.search_by_token_mp(self.library, q)

    def query_mp(self, q: str, view=5):
        q = q.lower()
        data = self.search_mp(q)
        OBS.pprint_result(data, view)
