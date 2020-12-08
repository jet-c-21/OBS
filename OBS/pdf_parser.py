"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2020/12/8
"""
# coding: utf-8
from PyPDF2 import PdfFileReader
from OBS.ult import Ult
from typing import Union
from OBS.cls.doc import Doc
import multiprocessing as mp
from tqdm import tqdm


class PDFParser:
    @staticmethod
    def read(pdf_path) -> Union[PdfFileReader, None]:
        with open(pdf_path, 'rb') as f:
            try:
                return PdfFileReader(f)
            except Exception as e:
                msg = f"failed to parse file via PyPDF2.PdfFileReader  Error: {e}"
                Ult.prt_log(msg, 'WARN')

    @staticmethod
    def get_text(pdf_path: str) -> str:
        text = ''
        with open(pdf_path, 'rb') as f:
            try:
                pdf = PdfFileReader(f)
                if pdf:
                    for page_index in range(pdf.getNumPages()):
                        page = pdf.getPage(page_index)
                        page_text = page.extractText()
                        page_text = page_text.replace('\n', ' ')
                        text += page_text.lower()
            except Exception as e:
                msg = f"failed to parse file via PyPDF2.PdfFileReader  Error: {e}"
                Ult.prt_log(msg, 'WARN')

        return text

    @staticmethod
    def _get_text_mp(doc: Doc) -> str:
        pdf_path = doc.path
        return PDFParser.get_text(pdf_path)

    @staticmethod
    def get_text_mp(library: list) -> Union[list, None]:
        for doc in library:
            if doc.type != 'pdf':
                msg = 'some document are not pdf file, plz recheck!'
                Ult.prt_log(msg, 'WARN')
                return

        with mp.Pool() as pool:
            result = list(
                tqdm(
                    pool.imap(PDFParser._get_text_mp, library), total=len(library)
                )
            )

        return result
