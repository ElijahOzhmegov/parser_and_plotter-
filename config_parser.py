import os


class Graph:
    def __init__(self):
        self.name = ''

        self.Xname = ''
        self.Ynames = []


def extracting_meaning(sentence):
    words = sentence.split("\"")
    return words[1]


def extracting_data(file_lines):
    array_of_graphs = []
    path = "Empty"

    for line in file_lines:
        words = line.split("=")

        clear_word = words[0].replace(" ", "")

        if clear_word == "Graph":
            bubble = Graph()
            array_of_graphs.append(bubble)
            bubble.name = extracting_meaning(words[1])

        elif clear_word == "Xaxis":
            bubble.Xname = extracting_meaning(words[1])

        elif clear_word == "Yaxis":
            bubble.Ynames.append(extracting_meaning(words[1]))

        elif clear_word == "path":
            path = extracting_meaning(words[1])

    return path, array_of_graphs


def going_via_file(file_lines):
    path, array_of_graphs = extracting_data(file_lines)

    if path == "Empty":
        print("Unfortunately variable \"path\" was not defined!")
        print("Make sure that variable \"path\" was written correct.")
    else:
        if not os.path.isfile(path):
            print("Unfortunately defined path: \"" + path + "\" does not exist!")
        else:
            return path, array_of_graphs

    return 0, 0

def parse_file(file_name):
    with open(file_name) as file:
        file_lines = file.readlines()
        path, array_of_graphs = going_via_file(file_lines)

        return path, array_of_graphs


def extract_headers(array_of_graphs):
    required_headers = []

    for graph in array_of_graphs:

        if graph.Xname not in required_headers:
            required_headers.append(graph.Xname)

        for Yname in graph.Ynames:
            if Yname not in required_headers:
                required_headers.append(Yname)

    return required_headers


def main():
    TMP_file_name = "csv_config.config"
    path, array_of_graphs = parse_file(TMP_file_name)

    required_heads = extract_headers(array_of_graphs)
    print(required_heads)


if __name__ == "__main__":
    main()