# 문제 설명
# 개발자가 사용하는 언어와 언어 선호도를 입력하면 그에 맞는 직업군을 추천해주는 알고리즘을 개발하려고 합니다.

# 아래 표는 5개 직업군 별로 많이 사용하는 5개 언어에 직업군 언어 점수를 부여한 표입니다.

# 점수	SI	CONTENTS	HARDWARE	PORTAL	GAME
# 5	JAVA	JAVASCRIPT	C	JAVA	C++
# 4	JAVASCRIPT	JAVA	C++ JAVASCRIPT C
# 3	SQL	PYTHON	PYTHON	PYTHON	JAVASCRIPT
# 2	PYTHON	SQL	JAVA	KOTLIN	C
# 1	C  # C++	JAVASCRIPT	PHP	JAVA
# 예를 들면, SQL의 SI 직업군 언어 점수는 3점이지만 CONTENTS 직업군 언어 점수는 2점입니다. SQL의 HARDWARE, PORTAL, GAME 직업군 언어 점수는 0점입니다.

# 직업군 언어 점수를 정리한 문자열 배열 table, 개발자가 사용하는 언어를 담은 문자열 배열 languages, 언어 선호도를 담은 정수 배열 preference가 매개변수로 주어집니다. 개발자가 사용하는 언어의 언어 선호도 x 직업군 언어 점수의 총합이 가장 높은 직업군을 return 하도록 solution 함수를 완성해주세요. 총합이 같은 직업군이 여러 개일 경우, 이름이 사전 순으로 가장 빠른 직업군을 return 해주세요.


def solution(table, languages, preference):
    sum = []
    for i in table:
        n = 6
        tmp = 0
        for j in i.split(' '):
            for k in range(0, len(languages)):
                if j == languages[k]:
                    tmp += n * preference[k]
            n -= 1
        sum.append(tmp)
    # print(sum)
    ma = max(sum)
    lst = []
    for i in range(len(sum)):
        if ma == sum[i]:
            lst.append(table[i].split(' ')[0])
    return sorted(lst)[0]


# 다른사람 풀이

def solution(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) + \
                    (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key=lambda item: [-item[1], item[0]])[0][0]
