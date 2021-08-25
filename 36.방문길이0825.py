# 문제 설명
# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

# U: 위쪽으로 한 칸 가기

# D: 아래쪽으로 한 칸 가기

# R: 오른쪽으로 한 칸 가기

# L: 왼쪽으로 한 칸 가기

# 캐릭터는 좌표평면의(0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.


def solution(dirs):
    answer = 0
    dic = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    current = (0, 0)
    way = []
    for i in dirs:
        if (current[0] == 5 and i == 'R') or\
            (current[0] == -5 and i == 'L') or \
            (current[1] == 5 and i == 'U') or \
                (current[1] == -5 and i == 'D'):
            continue
        new = (current[0]+dic[i][0], current[1]+dic[i][1])
        if (current + new) in way or (new + current) in way:
            pass
        else:
            way.append((current + new))
            answer += 1
        current = new

    return answer
