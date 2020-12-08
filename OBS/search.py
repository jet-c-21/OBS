"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2020/12/8
"""
# coding: utf-8
from OBS.cls.doc import Doc
from functools import partial
import multiprocessing as mp


class Search:
    @staticmethod
    def search_by_match(library: [Doc], q: str) -> list:
        book_shelf = list()

        for doc in library:
            found = doc.text.count(q)
            data = (doc, found)
            book_shelf.append(data)

        book_shelf = sorted(book_shelf, key=lambda x: x[1], reverse=True)

        return book_shelf

    @staticmethod
    def search_by_token(library: [Doc], q: str) -> list:
        book_shelf = list()

        targets = q.split(' ')

        for doc in library:
            found = 0
            for token in targets:
                found += doc.text.count(token)

            data = (doc, found)
            book_shelf.append(data)

        book_shelf = sorted(book_shelf, key=lambda x: x[1], reverse=True)
        return book_shelf

    @staticmethod
    def _search_by_token_mp(doc: Doc, targets: list) -> (Doc, int):
        found = 0
        text = doc.text
        for token in targets:
            found += text.count(token)

        return doc, found

    @staticmethod
    def search_by_token_mp(library: [Doc], q: str) -> list:
        targets = q.split(' ')

        with mp.Pool() as pool:
            job = partial(Search._search_by_token_mp, targets=targets)
            book_shelf = pool.map(job, library)

        book_shelf = sorted(book_shelf, key=lambda x: x[1], reverse=True)
        return book_shelf
