# 레스토랑을 운영하고 있는 "스카피"는 레스토랑 내부가 너무 낡아 친구들과 함께 직접 리모델링 하기로 했습니다. 레스토랑이 있는 곳은 스노우타운으로 매우 추운 지역이어서 내부 공사를 하는 도중에 주기적으로 외벽의 상태를 점검해야 할 필요가 있습니다.

# 레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있습니다. 따라서 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는 지, 주기적으로 친구들을 보내서 점검을 하기로 했습니다. 다만, 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한했습니다. 친구들이 1시간 동안 이동할 수 있는 거리는 제각각이기 때문에, 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사를 돕도록 하려고 합니다. 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다. 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다.

# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성해주세요.
def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_lst = [()]  # 현재까지 고칠 수 있는 취약점들
    cnt = 0  # 투입친구 수
    dist.sort(reverse=True)

    # 고칠 수 있는 것들 리스트
    for can_move in dist:
        repairs = []  # 친구별 고칠 수 있는 취약점들 저장
        cnt += 1

        # 수리 가능한 지점 찾기
        for i, wp in enumerate(weak):
            start = wp
            ends = weak[i:] + [n+w for w in weak[:i]]  # 시작점 기준 끝 포인트들 저장
            can = [end % n for end in ends if end -
                   start <= can_move]  # 가능한 지점들
            repairs.append(set(can))

        # 수리 가능한 경우 탐색
        cand = set()
        for r in repairs:  # 새친구의 수리가능 지점
            for x in repair_lst:  # 기존 수리 가능 지점
                new = r | set(x)  # 새로운 수리 가능 지점
                if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
                    return cnt
                cand.add(tuple(new))
        repair_lst = cand

    return -1

#다른사람 풀이

from collections import deque

def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))

                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
    return -1
