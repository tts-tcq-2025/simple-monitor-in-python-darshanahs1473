def is_in_range(name, value, min_val, max_val):
    if value < min_val:
        print(f"{name} is LOW!")
        return False
    if value > max_val:
        print(f"{name} is HIGH!")
        return False
    return True


def battery_is_ok(temperature, soc, charge_rate, reporter=print):
    status = True

    if not is_in_range("Temperature", temperature, 0, 45):
        status = False
    if not is_in_range("State of Charge", soc, 20, 80):
        status = False
    if not is_in_range("Charge Rate", charge_rate, 0, 0.8):
        status = False

    return status


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
