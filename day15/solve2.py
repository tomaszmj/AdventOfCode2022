#!/usr/bin/python
from typing import Tuple, List


def main():
    sensors: List[Tuple[int, int]] = []
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
            except BaseException as e:
                print(f"error parsing line {i} ({line}): {e}")
                raise
    limit = 4000000
    noncovered_fields = set()
    for y in range(0, limit+1):  # this is a bit brutal (computation inefficient), but performance is enough
        # x_bounds is a list of pairs (min_x_in_sensor_range, max_x_in_sensor_range) for constant y
        x_bounds = []
        for s, r in zip(sensors, radius):
            dy = abs(y - s[1])
            max_abs_dx = r - dy
            if max_abs_dx <= 0:
                continue
            min_x_in_sensor_range = s[0] - max_abs_dx
            max_x_in_sensor_range = s[0] + max_abs_dx
            if max_x_in_sensor_range < 0:
                continue 
            if min_x_in_sensor_range > limit:
                continue
            min_x_in_sensor_range = max(min_x_in_sensor_range, 0)
            max_x_in_sensor_range = min(max_x_in_sensor_range, limit)
            x_bounds.append((min_x_in_sensor_range, max_x_in_sensor_range))
        if len(x_bounds) == 0:
            print(f"unexpected situation - nothing is covered by sensors at y={y}")
            return
        x_bounds.sort(key=lambda b: b[0])  # sort by min x (bounds start)
        # Go over all bounds, checking fields covered by sensors.
        begin = x_bounds[0][0]
        end = x_bounds[0][1]
        for x in range(0, begin):
            noncovered_fields.add((x, y))  # it should happen exactly once
        for b in x_bounds[1:]:
            # If the next bound has common part with the previous bound,
            # just extend range of interest (begin, end)
            if b[0] <= end:
                end = max(end, b[1])
            else:
                # If the next bound does not have common part with the previous
                # bound, check fields from the previous (begin, end)
                # and start new range at the new bound.
                for x in range(end + 1, b[0]):
                    noncovered_fields.add((x, y))  # it should happen exactly once
                begin = b[0]
                end = b[1]
        for x in range(end + 1, limit + 1):
            noncovered_fields.add((x, y))  # it should happen exactly once
    if len(noncovered_fields) != 1:
        print(f"expected exactly 1 noncovered field, got {len(noncovered_fields)}")
        return
    x, y = noncovered_fields.pop()
    print(x*4000000 + y)


if __name__ == "__main__":
    main()

