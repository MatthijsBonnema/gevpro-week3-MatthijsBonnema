#!/usr/bin/python3
# File: language.py.py
# Author: Matthijs Bonnema
# Date: 2/24/15
# Info:

import sys
import json
from collections import namedtuple

def main():

    file = 'blood-die.json'
    out_file = open("blood-die_result.json", "w")
    json_data = open(file)
    data = json.load(json_data)

    namedlan = namedtuple('namedlan', ["language", "classf", "blood", "die"])

    for language in data:

        languagenamed = namedlan(language[0], language[1], language[2], language[3])

        language_blood = languagenamed.blood.split(", ")
        language_die = languagenamed.die.split(", ")
        language_blood[-1] = language_blood[-1].strip()
        language_die[-1] = language_die[-1].strip()

        [json.dump(language, out_file, indent=4) for blood in language_blood if blood in language_die]

    json_data.close()


if __name__ == "__main__":
    main()