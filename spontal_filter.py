#!/usr/bin/python3
# File: spontal_filter.py.py
# Author: Matthijs Bonnema
# Date: 2/23/15
# Info: 

import sys
import xml.etree.ElementTree as ET

def main(argv):
    file = argv[1]
    output = argv[2]

    tree = ET.parse(file)
    root = tree.getroot()

    for child in root:
        BOTTOM_HZ = int(child.find('BOTTOM_HZ').text)
        TOP_HZ = int(child.find('TOP_HZ').text)
        F0_START = float(child.find('F0_START').text)
        F0_END = float(child.find('F0_END').text)


        if BOTTOM_HZ <= F0_START <= TOP_HZ and BOTTOM_HZ <= F0_END <= TOP_HZ:
            continue
        else:
            root.remove(child)

    tree.write(output)


if __name__ == "__main__":
    main(sys.argv)