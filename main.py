from ipynb.fs.defs.script import *


with open("texts.txt", 'r') as f:
    text = f.read()
    texts = text.split("=====")


main(texts)
