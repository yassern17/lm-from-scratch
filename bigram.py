import numpy as np 

with open('training-data/input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def data_info(text: str) -> None:
    # basic information about lenghts of text
    print("length in characters:", len(text))
    print("number of lines:", text.count('\n'))
    print("number of words:", len(text.split()))

    # first 500 characters
    print("\nfirst 500 characters: \n\n\n", text[:500])


chars = sorted(set(text))
vocab_size = len(chars)
print(''.join(chars))
print("vocab size:", vocab_size)