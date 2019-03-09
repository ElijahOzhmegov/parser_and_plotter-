str_path = "path"

def search_for_path(file):
    for line in file.readlines():
        words = line.split("=")

        for word in words:
            uncluttered_word = word.replace(" ", "")

            if uncluttered_word == str_path:
                path = words[1].split("\"")
                return path[1]


def main():
    file = open("csv_config.config")

    path = search_for_path(file)

    with open(path) as csv_file:
        print(csv_file.readline())
    print(path)

    file.close()

if __name__ == "__main__":
    main()