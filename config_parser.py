import os

class Graph:
    def __init__(self):
        self.name = ''

        self.Xname = ''
        self.Ynames = []


def searching_for(key, file):
    while True:
        line = file.readline()
        words = line.split("=")

        for word in words:
            uncluttered_word = word.replace(" ", "")

            if uncluttered_word == key:
                path = words[1].split("\"")
                return path[1]

    return 0


def scanning_for_graph_data(file):
    print(file.readlines())

def main():
    file = open("csv_config.config")

    path = searching_for("path", file)

    if path == 0:
        print("Unfortunately variable \"path\" was not defined!")
        print("Make sure that variable \"path\" was written correct.")
    elif os.path.isfile(path):

        scanning_for_graph_data(file)

        with open(path) as csv_file:
            print(csv_file.readline())
        print(path)
    else:
        print("Unfortunately defined path: \"" + path + "\" does not exist!")

    file.close()

if __name__ == "__main__":
    main()