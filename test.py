from janome.tokenizer import Tokenizer
import sys

text = sys.argv
tokenizer = Tokenizer()
for token in tokenizer.tokenize(text[1]):
    print(token)
