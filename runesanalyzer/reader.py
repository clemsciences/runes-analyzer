
import os
import codecs


def load_rundata():
    with codecs.open(os.path.join("data_runes", "RUNTEXTX"), "r", encoding="utf-8") as f:
        for line in f:
            yield line


def read_rundata():
    inscriptions = []
    with codecs.open(os.path.join("data_runes", "RUNTEXT"), "r", encoding="utf-8") as f:
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


if __name__ == "__main__":
    load_urnodisk()
