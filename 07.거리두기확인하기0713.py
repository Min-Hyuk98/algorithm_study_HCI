# 개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

# 코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
# 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

# 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.



# 내풀이
from collections import deque
def solution(places):
    answer = []
    for room in places:
        end = 0
        for i in range(5):
            for j in range(5):
                # (i,j) and (i,j+1)
                # (i,j) and (i+1,j)
                # (i,j) and (i+1,j+1)
                # (i,j) and (i+1,j-1)
                # (i,j) and (i,j+2)
                # (i,j) and (i+2,j)

                if room[i][j] == 'P':
                    if j < 4 and room[i][j+1] == 'P':
                        answer.append(0)
                        end = 1
                        break
                    if i < 4 and room[i+1][j] == 'P':
                        answer.append(0)
                        end = 1
                        break
                    if i < 4 and j < 4 and room[i+1][j+1] == 'P' and (room[i+1][j] != 'X' or room[i][j+1] != 'X'):
                        answer.append(0)
                        end = 1
                        break
                    if i < 4 and j > 0 and room[i+1][j-1] == 'P' and (room[i][j-1] != 'X' or room[i+1][j] != 'X'):
                        answer.append(0)
                        end = 1
                        break
                    if i < 3 and room[i+2][j] == 'P' and room[i+1][j] != 'X':
                        answer.append(0)
                        end = 1
                        break
                    if j < 3 and room[i][j+2] == 'P' and room[i][j+1] != 'X':
                        answer.append(0)
                        end = 1
                        break
            if end == 1:
                break
        if end == 0:
            answer.append(1)
    return answer


# 다른 사람 풀이


def check(place, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([x, y, 0])
    visited = set()
    visited.add(tuple([x, y]))
    while queue:
        a, b, c = queue.popleft()
        if c == 2:
            continue
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx <= len(place)-1 and ny >= 0 and ny <= len(place[0])-1:
                if tuple([nx, ny]) not in visited:
                    visited.add(tuple([nx, ny]))
                    if place[nx][ny] == 'P':
                        return False
                    if place[nx][ny] == 'X':
                        continue
                    queue.append([nx, ny, c+1])

    return True


def solution(places):
    answer = []

    for place in places:
        people = []
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    people.append([i, j])

        flag = True
        for x, y in people:
            if not check(place, x, y):
                flag = False
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer
