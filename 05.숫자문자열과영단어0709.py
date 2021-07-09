# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"

# 내 풀이
def solution(s):
    answer = 0
    tmp = ''
    nums = {'zer': 0, 'one': 1, 'two': 2, 'thr': 3, 'fou': 4,
            'fiv': 5, 'six': 6, 'sev': 7, 'eig': 8, 'nin': 9}
    for i in range(len(s)):
        if s[i].isdigit():
            tmp += str(s[i])
        else:
            if s[i:i+3] in nums.keys():
                print('a')
                tmp += str(nums[s[i:i+3]])
    answer = int(tmp)
    return answer




# 다른 사람 풀이
num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
