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

    print(root.tag)

    for child in root:
        for child in child:
            print(child.tag, child.text)


    tree.write('filtered_spontal.xml')


if __name__ == "__main__":
    main()