# 2020.03.19
# 자료구조 
# 스택
"""
acmicpc.net/problem/9012
문제: 괄호 문자열은 두 개의 괄호 기호인 '('와 ')' 만으로 구성되어 있는 문자열이다. 
    입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해서 그 결과를 YES와 NO로 나타내어야 한다.
입력: 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 제이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.  
    각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.
출력: 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 "YES", 아니면 "NO"를 한 줄에 하나씩 차례대로 출력해야 한다.
"""
import sys
input = sys.stdin.readline

def find_VPS(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            return "NO"

    if cnt == 0:
        return "YES"
    else:
        return "NO"


T = int(input())
for i in range(T):
    s = list(input().rstrip())
    print(find_VPS(s))