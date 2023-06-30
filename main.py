import re

dates = []

with open('test.txt') as f:
    for line in f.readlines():
        if line[:4] == 'Date':
            dates.append(line[5:].strip())

hour_pattern = '\d+:\d+:\d+'
day_pattern = '\w+ \w+ \d+'

day_map = {}

for d in dates[::-1]:
    day = re.search(day_pattern, d).group(0)
    time = re.search(hour_pattern, d).group(0)

    if day not in day_map:
        day_map[day] = []
    day_map[day].append(time)


def calc_time_diff(start, end):
    if end[1] < start[1]:
        # borrow 60, hour -1
        end[1] += 60
        end[0] -= 1

    temp_result = [end[0] - start[0], end[1] - start[1]]

    result = temp_result[0] * 60 + temp_result[1]
    return result

def total_time_diff(time_vec):
    # [[1,2], [3,4], [4,5]]
    total_time = 0
    for i in range(len(time_vec)):
        if i + 1 == len(time_vec):
            break
        total_time += calc_time_diff(time_vec[i], time_vec[i + 1])
    
    return total_time

def calculate_time_in_day(day): 
    time_vec = []

    for time in day:
        hour = time[:2]
        minute = time[3:5]
        time_vec.append([int(hour), int(minute)])
    
    total_time = total_time_diff(time_vec)
    return total_time


total = 0

for day in day_map.keys():
    total += calculate_time_in_day(day_map[day])

print(f'{total // 60} hours, {total - 60 * (total // 60)} minute.')