def cal_tau_2(speed):
    distance = notice_distance(speed)
    tau = distance / speed

    return tau


def notice_distance(design_speed):
    # default value
    design_speed = design_speed * 3.6
    maneuver_speed = -0.0007*design_speed**2+0.6601*design_speed+4.5679
    # maneuver_time = -0.0069*design_speed + 4.6105
    maneuver_time = 12.1
    # avg_deceleration = -0.0103*design_speed + 4.8738
    avg_deceleration = 4.5
    # dsd = (5.5*design_speed/3.6)+((design_speed**2-maneuver_speed**2)/(2*avg_deceleration*3.6**2))+(maneuver_time*maneuver_speed/3.6)
    dsd = (0.278*design_speed*maneuver_time)
    # print (minDistance)

    return dsd


if __name__ == '__main__':
    print(notice_distance(50/3.6))
    print(cal_tau_2(50/3.6))
