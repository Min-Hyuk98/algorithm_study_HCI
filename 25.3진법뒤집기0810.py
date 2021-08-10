# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 내풀이
def solution(n):
    answer = 0
    three = ''
    while n >= 3:
        three += str(n % 3)
        n = n // 3
    three += str(n)
    n = len(three) - 1
    for i in three:
        answer += int(i) * (3**n)
        n -= 1
    return answer



#다른사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    # int() 이용해서 
    return answer

#정수로 변환할 값과 밑을 int(value, base)의 형태로 입력해줍니다.
# value는 0, base는 10이 디폴트이며,
# base에 2에서 36 사이의 값을 입력할 수 있습니다.
