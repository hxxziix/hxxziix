# 프로그래머스 대소문자 바꿔서 출력하기
# isupper(): 문자열이 모두 대문자이면 True, 아니면 False 반환
# islower(): 문자열이 모두 소문자이면 True, 아니면 False 반환
# 두 함수 모두 문자열 중 숫자가 있더라도 소문자, 대문자만 확인하여 결과 반환함.

st = "aBcDeF"
res = []

for s in st:
    if s.isupper():
        res.append(s.lower())
    elif s.islower():
        res.append(s.upper())
result = "".join(res)
print(result)
