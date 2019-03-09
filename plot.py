import csv_parser as csv_pr
import grapher as gr

TMP_req_heads = ["ts", "Vx", "Depth", "Pitch"]
TMP_file_name = 'LD600.csv'

def main():
    line_of_Parameters = csv_pr.fill_in_data(TMP_file_name, TMP_req_heads)

    gr.draw(line_of_Parameters[0], line_of_Parameters[2])
    gr.draw(line_of_Parameters[0], line_of_Parameters[3])

    print("Success!")

if __name__ == "__main__":
    main()