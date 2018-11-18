"""test.py

DB에 like 쿼리를 날리는 연산이 너무 무거워
미리 계산해 놓으려고 함

data는 file 하나 당
	[
		['tag','tag,'tag'],
		['tag','tag,'tag'],
		['tag','tag,'tag'],
	]
모양

첫 버전은 1-gram index (임시 방편)

TODO:
	- 0-gram
	- 연관 단어(추천 단어) 딕셔너리 생성
		- apriori, fp-growth...
"""
from collections import Counter 
import json
from os import listdir
from os.path import join

path = './data'

word_list = []
word_set = set() 

# 파일 읽기 및 단어 리스트 통합(단어:빈도수 딕셔너리 만들기 위해)
for filename in listdir(path):
	f = open(join(path, filename))
	rows = json.load(f)
	print(filename, 'is loaded')

	for row in rows:
		row = [word for word in row if ('개발팀' not in word) and ('테스트' not in word)]
		word_list += row
	
# 단어: 빈도수 딕셔너리 생성
word_counter = Counter(word_list)
# print("most common 100:", word_counter.most_common(100))

word_count_dict = dict(word_counter)

# 1-gram 추출 -> token_set
words = word_count_dict.keys()
token_set = set()
for word in words:
	for char in word:
		token_set.add(char)

# 토큰 : [단어 리스트] 매핑 만들기
mapping_for_search = dict()
for token in token_set:
	# token이 포함되는 단어들 후보군으로
	candidate = [word for word in words if token in word]
	# 빈도수 순 정렬
	candidate = sorted(candidate, key=lambda word: word_counter[word], reverse=True)
	mapping_for_search[token] = candidate

with open('mapping.json', 'w') as output:
	json.dump(mapping_for_search, output)
	

