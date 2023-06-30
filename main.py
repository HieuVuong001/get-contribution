from utilities import *
import sys
EXIT_FAILURE = 1
DEFAULT_FILENAME = 'log.txt'

if get_log(DEFAULT_FILENAME) == 1:
    sys.exit(EXIT_FAILURE)

day_map = process_log(DEFAULT_FILENAME)
total_coding_time = get_total_coding_time(day_map=day_map)
print(format_coding_time(total_coding_time))
clean_up(DEFAULT_FILENAME)
