#!/usr/bin/env python3

from collections import namedtuple, defaultdict
import sys


GuardSleep = namedtuple('GuardSleep', 'guard, flom, to')

def parse_records(records):
    sleep_schedule = []
    guard = None
    sleeping_from = None
    sleeping_to = None

    for record in records:
        minute = int(record[15:17])
        cmd = record[19:24]

        if cmd == 'Guard':
            guard = int(record.split('#')[1].split()[0])

        elif cmd == 'falls':
            sleeping_from = minute

        elif cmd == 'wakes':
            sleeping_to = minute

            sleep_schedule.append(GuardSleep(guard=guard, flom=sleeping_from, to=sleeping_to))

    return sleep_schedule

def find_guard_with_most_sleep(schedule):
    minutes_total = defaultdict(int)

    for s in schedule:
        minutes_total[s.guard] += s.to - s.flom

    max_minutes = sorted(minutes_total.items(), key=lambda i: i[1], reverse=True)[0]

    # return guard id
    return max_minutes[0]
    
def find_guards_most_asleep_min(guard, schedule):
    histogram = [0] * 60 

    for s in schedule:
        if s.guard == guard:
            for i in range(s.flom, s.to):
                histogram[i] += 1

    maximum = 0
    max_i = -1

    for i in range(0, 60):
        if histogram[i] > maximum:
            max_i = i
            maximum = histogram[i]

    return max_i

def find_solution(input_file):
    records = sorted(input_file.readlines())

    schedule = parse_records(records)

    guard = find_guard_with_most_sleep(schedule)
    most_asleep = find_guards_most_asleep_min(guard, schedule)

    return guard, most_asleep


if __name__ == "__main__":
    guard, most_asleep = find_solution(sys.stdin)

    print(f"Guard {guard} is most asleep at {most_asleep}, result \"{guard * most_asleep}\"")

