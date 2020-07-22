from ppt2json import PPT2JSON
import os

ppt_dir = 'DATA'

for ppt in os.listdir(ppt_dir):
    ppt_path = f'{ppt_dir}/{ppt}'
    ppt_json = PPT2JSON(ppt_path).get_json()
    print(ppt_json)
    print()
