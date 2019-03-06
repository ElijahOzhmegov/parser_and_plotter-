class Column:

    def __init__(self, name, index):
        self.name  = name
        self.index = index
        self.data = []

    def expand_data(self, number):
        self.data.append(number)


TMP_req_heads = ["ts", "Depth"]
TMP_file_name = 'LD600.csv'

def get_headers_indexes(input_headers, requered_headers):
    headers = input_headers.split(";")

    headers_indexes = {}

    i = 0
    for header in headers:
        if header in requered_headers:
            headers_indexes[header] = i
        i += 1

    return headers_indexes

def fill_in_data(file_name, wanted_heads):
    with open(file_name, "r") as file:
        all_headers = file.readline()
        headers_indexes = get_headers_indexes(all_headers, wanted_heads)

        array_of_Columns = []

        for head in headers_indexes:
            bubble = Column(head, headers_indexes[head])
            array_of_Columns.append(bubble)

        for line in file.readlines():
            words = line.split(";")
            if len(words) > 1:  # fix me
                for one_Column in array_of_Columns:
                    i = one_Column.index
                    one_Column.expand_data(words[i])

        return array_of_Columns



def main():
    line_of_Parameters = fill_in_data(TMP_file_name, TMP_req_heads)

    print(42)

        # for line in file.readlines():
            # for word in line.split(";"):
                # print(word)



if __name__ == "__main__":
    main()