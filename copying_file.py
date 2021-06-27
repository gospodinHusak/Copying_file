from xml.etree.ElementTree import ElementTree
import shutil

data = []
tree = ElementTree()
tree.parse('config.xml')
root = tree.getroot()

for sub_el in root:
    for key in sub_el.attrib:
        data.append(sub_el.attrib[key])
    shutil.copy(data[0] + '\\' + data[2], data[1])
    data.clear()
