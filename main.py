from utilities import *
import sys
import uuid
EXIT_FAILURE = 1
DEFAULT_FILENAME = f'{uuid.uuid4().hex[:6]}.txt'

if get_log(DEFAULT_FILENAME) == 1:
    sys.exit(EXIT_FAILURE)

if len(sys.argv) == 1:
    # no user name is given
    day_map = process_log(DEFAULT_FILENAME)
elif len(sys.argv) == 2:
    # one username is given
    day_map = process_log(DEFAULT_FILENAME, sys.argv[1])
else:
    print("Too many arguments provided.")
    sys.exit(EXIT_FAILURE)
total_coding_time = get_total_coding_time(day_map=day_map)
print(format_coding_time(total_coding_time))
