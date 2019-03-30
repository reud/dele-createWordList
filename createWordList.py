#!/usr/local/bin/python3
import argparse
import itertools

parser = argparse.ArgumentParser(description=' dele 1話に出てくるプログラムの再現スクリプト')

parser.add_argument('words', help='組み合わせる単語', nargs='*')
parser.add_argument('--output', '-o', help='ファイルの出力先 設定ないなら output.txt')

args = parser.parse_args()

ouput_lists = []

for i in range(1, len(args.words) + 1):
    ouput_lists += itertools.permutations(args.words, i)

str_list=[]
for el in ouput_lists:
    word='\n'.join(el).replace('\n', '')
    str_list.append(word)
    print(word)

path: str = args.output if args.output else 'output.txt'

with open(path, 'w') as file:
    file.write('\n'.join(str_list))

print(len(ouput_lists))
