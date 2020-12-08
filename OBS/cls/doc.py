"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2020/12/8
"""


# coding: utf-8

class Doc:
    def __init__(self, root=None, sub_dir=None, name=None):
        self.name = name
        self.type = None
        if self.name and isinstance(self.name, str):
            self.type = self.name.split('.')[-1]

        self.sub_dir = sub_dir
        self.root = root
        self.path = None

        if self.root and self.sub_dir and name:
            self.path = f"{self.root}/{self.sub_dir}/{self.name}"

        self.text = ''

    def __str__(self):
        s = f"   name : {self.name}\n" \
            f"   type : {self.type}\n" \
            f"sub dir : {self.sub_dir}\n" \
            f"   root : {self.root}\n" \
            f"   path : {self.path}\n" \
            f"   text : {len(self.text)}\n"
        return s
