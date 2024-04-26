import xml.etree.ElementTree as ET
import runFile as f
import updateXML

net_file = f.net_path()

tree = ET.parse(net_file)
root = tree.getroot()


def get_route():
    route = []
    i = 0

    for edge in root.findall('edge'):
        if edge.get('priority') == "-1":
            edge_id = edge.get('id')
            route.insert(i, edge_id)
            i += 1

    return route


def modify_speed(speed):
    for edge in root.findall('edge'):
        for lane in edge.findall('lane'):
            lane.set('speed', str(speed))
    tree.write('updatedNetwork.net.xml')


if __name__ == '__main__':
    modify_speed(20)