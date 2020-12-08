"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2020/12/7
"""
# coding: utf-8
import ntpath


class Ult:
    @staticmethod
    def path_converter(path_str: str, path_type='linux') -> str:
        if path_type == 'win':
            return path_str.replace('/', '\\')

        elif path_type in ['unix', 'linux', 'mac']:
            return path_str.replace('\\', '/')

    @staticmethod
    def prt_log(msg: str, log_type='INFO', debug=True):
        if debug:
            s = f"[{log_type}] ➤ {msg}"
            print(s)
