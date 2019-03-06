class Parameter:
    def __init__(self, name, axe_type):
        self.name     = name
        self.axe_type = axe_type

class Graph:
    def __init__(self):
        self.xlabel = ""
        self.ylabel = ""

    def add_xlabel(self, xlabel):
        self.xlabel = xlabel

    def add_ylabel(self, ylabel):
        self.ylabel = ylabel


key_words = {"Xname": "Xname", "Yname": "Yname"}

def main():
    file = open("csv_config.config")

    read(file)
    file.close()

if __name__ == "__main__":
    main()