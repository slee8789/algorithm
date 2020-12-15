# n : 셔틀 운행 횟수
# t : 셔틀 운행 간격
# m : 한 셔틀에 탈 수 있는 최대 크루 수
# timetable : 크루가 대기열에 도착하는 시각을 모은 배열

def time_to_only_minute(time):
    # print((int(time.split(":")[0]) * 60) + int(time.split(":")[1]))
    ret = (int(time.split(":")[0]) * 60) + int(time.split(":")[1])
    # print(ret)
    return ret


# 09:00 -> 540

def solution(n, t, m, timetable):
    answer = 0
    origin_time = 540
    time = 540  # 09:00

    while time <= origin_time + (n * t):
        count = m
        for other in sorted(timetable):
            if count == 0:
                continue

            other_time = time_to_only_minute(other)
            if time > other_time:
                count -= 1
            else : break

        if answer != 0: break
        if count != 0:
            answer = time

        time += t

    return answer


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
# print(solution(10, 60, 45,
#                ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
#                 "23:59", "23:59", "23:59", "23:59", "23:59"]))
