#!/usr/bin/python
from typing import Tuple, List, Set


def main():
    sensors: List[Tuple[int, int]] = []
    beacons: Set[Tuple[int, int]] = set()
    radius: List[int] = []
    with open("data.txt", "r") as f:
        for i, line in enumerate(f):
            try:
                line = line.rstrip()
                if not line:
                    continue
                _, _, s = line.partition("Sensor at x=")
                xs, _, s = s.partition(",")
                _, _, s = s.partition(" y=")
                ys, _, s = s.partition(":")
                _, _, s = s.partition(" closest beacon is at x=")
                xb, _, s = s.partition(",")
                _, _, yb = s.partition(" y=")
                sensor = (int(xs), int(ys))
                beacon = (int(xb), int(yb))
                radius.append(abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1]))
                sensors.append(sensor)
                beacons.add(beacon)
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    y = 2000000
    # x_bounds is a list of pairs (min_x_in_sensor_range, max_x_in_sensor_range) for constant y
    x_bounds = []
    for s, r in zip(sensors, radius):
        dy = abs(y - s[1])
        max_abs_dx = r - dy
        if max_abs_dx <= 0:
            continue
        min_x_in_sensor_range = s[0] - max_abs_dx
        max_x_in_sensor_range = s[0] + max_abs_dx
        x_bounds.append((min_x_in_sensor_range, max_x_in_sensor_range))
    if len(x_bounds) == 0:
        print(f"unexpected situation - nothing is covered by sensors at y={y}")
        return
    x_bounds.sort(key=lambda b: b[0])  # sort by min x (bounds start)
    # Go over all bounds, counting number of fields covered by sensors.
    begin = x_bounds[0][0]
    end = x_bounds[0][1]
    result = 0
    for b in x_bounds[1:]:
        # If the next bound has common part with the previous bound,
        # just extend range of interest (begin, end)
        if b[0] <= end:
            end = max(end, b[1])
        else:
            # If the next bound does not have common part with the previous
            # bound, add number of fields from the previous (begin, end)
            # and start new range at the new bound.
            result += end - begin + 1
            begin = b[0]
            end = b[1]
    result += end - begin + 1  # the last range was not counted above - include it here
    for b in beacons:
        if b[1] == y:
            result -= 1
    print(result)


if __name__ == "__main__":
    main()

