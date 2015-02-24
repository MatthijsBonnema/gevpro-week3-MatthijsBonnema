#!/usr/bin/python3
# File: spontal_filter.py.py
# Author: Matthijs Bonnema
# Date: 2/23/15
# Info: 

import sys
import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('spontal.xml')
    root = tree.getroot()

    for child in root:
        BOTTOM_HZ = (child.find('BOTTOM_HZ').text)
        TOP_HZ = (child.find('TOP_HZ').text)
        F0_START = (child.find('F0_START').text)
        F0_END = (child.find('F0_END').text)

        if BOTTOM_HZ <= F0_START <= TOP_HZ and BOTTOM_HZ <= F0_END <= TOP_HZ:
            continue
        else:
            print("removed")
            root.remove(child)


    tree.write('filtered_spontal.xml')


if __name__ == "__main__":
    main()