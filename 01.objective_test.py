# 복습 문제 1: 문자열 길이 필터링 함수 제작
# 문제 설명
# 알파벳으로 이루어진 문자열 하나를 입력받아, "길이가 5 이상인 경우에만" 문자열 전체를 대문자로 변환하여 반환하는 함수를 정의하시오.
# 길이가 5 이하라면 '길이가 5 이하입니다' 메시지를 반환합니다.

# 예시

# 입력: 'abc'
# 출력: '길이가 5 이하입니다'
# 입력: 'abcde'
# 출력: 'ABCDE'

import sys

my_input = sys.stdin.readline()

# print(len(my_input()))

def function(my_input):
    if len(my_input) - 1 < 5:
        print("길이가 5 이하입니다")
    else:
        print(my_input.upper())

function(my_input)

# 복습 문제 2: N 이하 짝수 제곱수 리스트 반환하는 함수 제작
# 문제 설명
# 정수 N을 입력받아, N 이하의 숫자 중에서 짝수만을 제곱하여 리스트를 만들어 반환하는 함수를 정의하시오.

# 예시

# 입력: N = 5
# 출력: [4]
# 입력: N = 10
# 출력: [4, 16, 36, 64, 100]

import sys

N = int(sys.stdin.readline())

my_list = [i * i for i in range(N+1) if i % 2 == 0 and i != 0]

print(my_list)

# 복습 문제 3: 리스트 컴프리헨션을 이용하여 특정 문자 변형하기
# 문제 설명
# 리스트 컴프리헨션을 이용하여, 알파벳으로 된 이름의 특정 문자(e)만 2개로 늘려서 변형시키는 코드를 작성해 봅시다!

# name = 'Heybob'
# new_name_list = [# TODO]
# new_name = ''.join(new_name_list)
# print(new_name)
# 예시

# 입력: name = 'Heybob'
# 출력: 'Heeybob'

import sys

my_input = sys.stdin.readline()

new_name_list = [i * 2 if i == 'e' else i for i in my_input]

new_name = ''.join(new_name_list)

print(new_name)

# 복습 문제 4: map 함수와 람다 함수를 활용하여 특정 문자 변형하기
# 문제 설명
# map 함수와 람다 함수를 활용하여, 알파벳으로 된 이름의 특정 문자(e)만 2개로 늘려서 변형시키는 코드를 작성해 봅시다!

# name = 'Heybob'
# new_name_list = list(map(#TODO, name))
# new_name = ''.join(new_name_list)
# print(new_name)

import sys

my_input = sys.stdin.readline()

def my_function(str):
    for i in str:
        if i == 'e':
            return i * 2
        else:
            return i

new_name_list = list(map(my_function, my_input))
new_name = ''.join(new_name_list)
print(new_name)

# 복습 문제 5: 리스트 변환 및 zip 함수 활용하기
# 문제 설명
# 다음과 같이 길이가 같은 사람 이름과 나이가 '공백으로 구분된 문자열'로 입력됩니다.

# [ ]
# names = '가희 라희 나희 다희 마희'
# ages = '32 22 34 54 28'
# 1. 각 문자열을 리스트로 변환하고, ages는 정수의 리스트로 변환하세요.
# [ ]
import sys

my_input1 = sys.stdin.readline()
my_input2 = sys.stdin.readline()

my_names = [i for i in my_input1.split()]
my_ages = list(map(int, my_input2.split()))

print(my_names)
print(my_ages)

# 2. 리스트 컴프리헨션을 이용하여, 이름과 나이 리스트의 정보를 다음과 같은 2차원 배열로 만드세요.
# [ ]
# # 예시 출력: [['가희', 32], ['라희', 22], ['나희', 34], ['다희', 54], ['마희', 28]]
# res = #TODO
# print(res)

import sys

my_input1 = sys.stdin.readline()
my_input2 = sys.stdin.readline()

my_names = [i for i in my_input1.split()]
my_ages = list(map(int, my_input2.split()))

res = [[my_names[i], my_ages[i]] for i in range(5)]
print(res)

# 3.zip() 함수를 이용하여, 이름과 나이 리스트의 정보를 다음과 같은 'list of tuples'로 만드세요.
# [ ]
# # 예시 출력: [('가희', 32), ('라희', 22), ('나희', 34), ('다희', 54), ('마희', 28)]
# res2 = #TODO
# print(res2)

import sys

my_input1 = sys.stdin.readline()
my_input2 = sys.stdin.readline()

my_names = [i for i in my_input1.split()]
my_ages = list(map(int, my_input2.split()))

res2 = list(zip(my_names, my_ages))
print(res2)