import os


def sumo_path():
    sumo = r'\Eclipse\Sumo\bin\sumo-gui.exe'
    my_path = os.path.abspath(os.path.dirname(__file__))
    final_path = my_path + sumo
    return final_path


def sumocfg_path():
    sumo = r'\simulation.sumocfg'
    my_path = os.path.abspath(os.path.dirname(__file__))
    final_path = my_path + sumo
    return final_path


def route_path():
    route = r'\route.rou.xml'
    my_path = os.path.abspath(os.path.dirname(__file__))
    final_path = my_path + route
    return final_path


def net_path():
    net = r'\network.net.xml'
    my_path = os.path.abspath(os.path.dirname(__file__))
    final_path = my_path + net
    return final_path


def laneChange_path():
    lc = r'\lanechange.xml'
    my_path = os.path.abspath(os.path.dirname(__file__))
    final_path = my_path + lc
    return final_path


def info_path():
    lc = r'\tripinfo.xml'
    my_path = os.path.abspath(os.path.dirname(__file__))
    final_path = my_path + lc
    return final_path


def open_sumo():
    path = 'sumo-gui.exe -c "' + sumocfg_path() + '" --step-length 0.1'
    print(path)
    os.system(path)


if __name__ == '__main__':
    open_sumo()