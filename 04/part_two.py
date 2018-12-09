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


def find_guard(input_file):
    records = sorted(input_file.readlines())
    schedule = parse_records(records)

    minutes_total = defaultdict(lambda: [0] * 60)
    max_minute = 0
    minute = -1
    guard_id = -1

    for s in schedule:
        for i in range(s.flom, s.to):
            minutes_total[s.guard][i] += 1

            if minutes_total[s.guard][i] >= max_minute:
                max_minute = minutes_total[s.guard][i]
                guard_id = s.guard
                minute = i


    return guard_id, minute 


if __name__ == "__main__":
    guard, most_asleep = find_guard(sys.stdin)

    print(f"Guard {guard} is most asleep at {most_asleep}, result \"{guard * most_asleep}\"")

