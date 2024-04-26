def cal_tau_2(speed):
    distance = notice_distance(speed)
    tau = distance / speed

    return tau


def notice_distance(design_speed):
    design_speed = design_speed * 3.6
    maneuver_time = 12.1
    dsd = (0.278*design_speed*maneuver_time)

    return dsd


if __name__ == '__main__':
    print(notice_distance(50/3.6))
    print(cal_tau_2(50/3.6))
