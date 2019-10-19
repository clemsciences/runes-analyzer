
import os
import codecs
import csv

from runesanalyzer import PACKDIR


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]

data_directory = os.path.join(PACKDIR, "data_runes")


def load_rundata():
    with codecs.open(os.path.join(data_directory, "RUNTEXTX"), "r", encoding="utf-8") as f:
        for line in f:
            yield line


def read_rundata():
    inscriptions = []
    with codecs.open(os.path.join(data_directory, "RUNTEXT"), "r", encoding="utf-8") as f:
        for line in f:
            # print(line)
            if line[0] != "!":
                l_line = line.strip().split(" ")
                if len(l_line) > 2:
                    inscriptions.append({"location": l_line[0], "period": l_line[1], "content": " ".join(l_line[2:])})
    return inscriptions


def load_urnodisk():
    i = 0
    for line in load_rundata():
        if line[0] != "!":
            l_line = line.strip().split(" ")
            if len(l_line) > 2 and l_line[2] == "U":
                print(" ".join(l_line[3:]))
                i += 1
    print(i)


def load_metadata():
    with codecs.open(os.path.join(data_directory, "RUNDATA.csv"), encoding="utf-8") as f:
        rundata_reader = csv.DictReader(f, dialect="excel-tab")
        print(rundata_reader.fieldnames)
        for line in rundata_reader:
            yield line


def get_urnordisk_inskritfter_datum():
    signa = []
    for line in load_metadata():
        if line["Period/Datering"].startswith("U"):
            signa.append(line["Signum"])
    for line in load_rundata():
        if line[0] != "!":
            l_line = line.strip().split(" ")
            if l_line[0] in signa:
                if len(l_line) > 2:
                    print(" ".join(l_line[3:]))


if __name__ == "__main__":
    # load_urnodisk()
    get_urnordisk_inskritfter_datum()
