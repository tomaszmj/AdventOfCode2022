#!/usr/bin/python
from typing import Tuple, List, Set


def field_can_contain_beacon(x, y, sensors, radius) -> bool:
    for s, r in zip(sensors, radius):
        distance = abs(x - s[0]) + abs(y - s[1])
        if distance <= r:
            return False
    return True


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
    min_x, max_x = None, None
    for s, r in zip(sensors, radius):
        dy = abs(y - s[1])
        max_abs_dx = r - dy
        if max_abs_dx <= 0:
            continue
        min_x_in_sensor_range = s[0] - max_abs_dx
        max_x_in_sensor_range = s[0] + max_abs_dx
        if min_x is None or min_x_in_sensor_range < min_x:
            min_x = min_x_in_sensor_range
        if max_x is None or max_x_in_sensor_range > max_x:
            max_x = max_x_in_sensor_range
    result = 0
    for x in range(min_x, max_x+1):
        if (x, y) in beacons:
            continue
        if not field_can_contain_beacon(x, y, sensors, radius):
            result += 1
    print(result)


if __name__ == "__main__":
    main()

