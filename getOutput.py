import os
import xml.etree.ElementTree as ET
import runFile as f

sumo_home = "C:\sumo"


def get_lanechange():
    lc_file = f.laneChange_path()

    tree = ET.parse(lc_file)
    root = tree.getroot()

    lc_count = 0
    for change in root.findall("change"):
        lc_count += 1
    print("No. of Lane Change: " + str(lc_count) + " times")




def get_tripinfo():
    info_file = f.info_path()

    tree = ET.parse(info_file)
    root = tree.getroot()

    total_timeLoss = 0.00
    total_travelTime = 0.00
    total_waiting_time = 0.00
    veh_count = 0.00
    for veh in root.findall('tripinfo'):
        if veh.get('id') != 'v_1':
            timeLoss = float(veh.get('timeLoss'))
            total_timeLoss += timeLoss
            travelTime = float(veh.get('duration'))
            total_travelTime += travelTime
            waitingTime = float(veh.get('waitingTime'))
            total_waiting_time += waitingTime
            veh_count += 1
    avg_timeLoss = total_timeLoss / veh_count
    avg_travelTime = total_travelTime / veh_count
    avg_waitingTime = total_waiting_time / veh_count

    print("AVG travel time: " + str(avg_travelTime) + " s")
    print("AVG time loss: " + str(avg_timeLoss) + " s")
    print("AVG waiting time: " + str(avg_waitingTime) + " s")


def get_output():
    print("\n")
    print("OUTPUT GENERATED")
    get_lanechange()
    get_tripinfo()


def plot(x, y):
    os.system('python ' + sumo_home)


if __name__ == '__main__':
    get_output()