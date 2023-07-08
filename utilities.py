import subprocess
import re
from rich.console import Console
from rich.progress import track

console = Console()

def get_log(filename='gitlog.txt'):
    with open(filename, 'w') as f:
        try:
            subprocess.run(['git', 'log'], stdout=f)
            return 0
        except Exception:
            console.print("Cannot get git to run. Are you in a git repository? Did you forget to install git?", style='red')
            subprocess.run(['rm', filename])
            return 1

def process_log(filename, github_user=None):
    dates = []
    day_map = {}

    hour_pattern = '\d+:\d+:\d+'
    day_pattern = '\w+ \w+ \d+'
    username_pattern = ' .+ '

    if github_user is None:
        with open(filename) as f:
            for line in track(f.readlines(), description="Reding file..."):
                if line[:4] == 'Date':
                    dates.append(line[5:].strip())

    with open(filename) as f:
        for line in track(f.readlines(), description="Reding file..."):
            if line[:6] == 'Author':
                username = re.search(username_pattern, line).group(0).strip()
                if username == github_user:
                    date_line = f.readline()
                    dates.append(date_line[5:].strip())



    for date in dates[::-1]:
        day = re.search(day_pattern, date).group(0)
        time = re.search(hour_pattern, date).group(0)

        if day not in day_map:
            day_map[day] = []
        day_map[day].append(time)

    return day_map


def get_time_diff(start, end):
    if end[1] < start[1]:
        # borrow 60, hour -1
        end[1] += 60
        end[0] -= 1

    temp_result = [end[0] - start[0], end[1] - start[1]]

    result = temp_result[0] * 60 + temp_result[1]
    return result

def get_total_time_diff(time_vec):
    # [[1,2], [3,4], [4,5]]
    total_time = 0
    for i in range(len(time_vec)):
        if i + 1 == len(time_vec):
            break
        total_time += get_time_diff(time_vec[i], time_vec[i + 1])
    
    return total_time

def get_coding_time_in_day(day): 
    time_vec = []

    for time in day:
        hour = time[:2]
        minute = time[3:5]
        time_vec.append([int(hour), int(minute)])
    
    total_time = get_total_time_diff(time_vec)
    return total_time

def get_total_coding_time(day_map):
    total = 0
    for day in day_map.keys():
        total += get_coding_time_in_day(day_map[day])
    
    return total

def format_coding_time(coding_time):
    return console.print(f'{coding_time // 60} hours, {coding_time - 60 * (coding_time // 60)} minute.')

def clean_up(filename):
    subprocess.run(['rm', filename])
