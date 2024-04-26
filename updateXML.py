# importing the module.
import xml.etree.ElementTree as ET
import runFile as f

route_file = f.route_path()

tree = ET.parse(route_file)
root = tree.getroot()


def remove_all_vehicle():
    for vehicle in root.findall('vehicle'):
        root.remove(vehicle)
        # for route in vehicle.findall('route'):
        #     edges = route.get('edges')
        #     print(edges)


def gen_vehicle(edge, lane, start_time, end_time, v_id, vtype):
    stop_lane = edge + '_' + lane
    veh_edges = ''
    for route in root.findall('route'):
        veh_edges = route.get('edges')
        # print(veh_edges)

    for routes in root.iter('routes'):
        vehicle = ET.SubElement(routes, 'vehicle')
        # vehicle.text = "Vehicle_1"
        vehicle.set('id', v_id)
        vehicle.set('type', vtype)
        vehicle.set('depart', str(start_time))
        vehicle.set('departSpeed', 'speedLimit')

        route = ET.SubElement(vehicle, 'route')
        route.set('edges', veh_edges)

        if vtype == 'type1':
            stop = ET.SubElement(vehicle, 'stop')
            stop.set('lane', str(stop_lane))
            stop.set('endPos', '0')
            stop.set('until', str(end_time))
        elif vtype == 'type3':
            vehicle.set('departLane', str(lane))
            vehicle.set('arrivalLane', str(lane))


def mod_flow(density, edge, lane, start_time, end_time, v_id, vtype):
    if density == 0:
        gen_vehicle(edge, lane, start_time + 50, end_time, v_id, vtype)

    if density == 0:
        flow = root.find('flow')
        flow.set('number', '0')
        # flow.set('vehsPerHour', '2000')
    else:
        flow = root.find('flow')
        flow.set('number', '150') # adjust number of car spawn
        flow.set('vehsPerHour', str(density))


def mod_tau(tau):
    for vType in root.findall('vType'):
        vType.set('tau', str(tau))
        # vType.set('minGap', str(tau))


def modify(edge, lane, start, end, density, tau):
    remove_all_vehicle()
    gen_vehicle(edge, lane, start, end, 'v_1', 'type1')
    mod_flow(density, edge, lane, start, end, 'v_2', 'type3')
    mod_tau(tau)
    tree.write('updatedRoute.rou.xml')


def get_edges():
    for edge in root.findall('edge'):
        edges = edge.attrib
        print(edges)


if __name__ == '__main__':
    accident_location = input("Input location: ")
    accident_lane = input("Input lane: ")
    time_start = input("Input start time: ")
    time_end = input("Input end time: ")
    traffic_dens = input("Input density: ")
    modify(accident_location, accident_lane, time_start, time_end, traffic_dens)