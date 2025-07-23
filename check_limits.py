from typing import Callable, List

class Vital:
    def __init__(self, name, value, min_val, max_val):
        self.name = name
        self.value = value
        self.min_val = min_val
        self.max_val = max_val

    def is_within_range(self):
        return self.min_val <= self.value <= self.max_val

    def breach_type(self):
        if self.value < self.min_val:
            return 'LOW'
        elif self.value > self.max_val:
            return 'HIGH'
        return 'NORMAL'


class Reporter:
    def report(self, vital: Vital):
        breach = vital.breach_type()
        if breach != 'NORMAL':
            print(f'{vital.name} is {breach}!')


def battery_is_ok(vitals: List[Vital], reporter: Callable[[Vital], None]) -> bool:
    status = True
    for vital in vitals:
        if not vital.is_within_range():
            reporter(vital)
            status = False
    return status


def default_reporter(vital: Vital):
    print(f"{vital.name} is {vital.breach_type()}!")


if __name__ == '__main__':
    vitals = [
        Vital("Temperature", 25, 0, 45),
        Vital("State of Charge", 70, 20, 80),
        Vital("Charge Rate", 0.7, 0, 0.8)
    ]
    assert(battery_is_ok(vitals, default_reporter) is True)

    vitals = [
        Vital("Temperature", 50, 0, 45),
        Vital("State of Charge", 85, 20, 80),
        Vital("Charge Rate", 0.0, 0, 0.8)
    ]
    assert(battery_is_ok(vitals, default_reporter) is False)
