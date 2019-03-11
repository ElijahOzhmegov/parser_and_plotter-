import csv_parser    as csv_pr
import config_parser as cnf_pr
import grapher       as gr

TMP_req_heads = ["ts", "Vx", "Depth", "Pitch"]
TMP_file_name = 'LD600.csv'
TMP_cnf_file = "csv_config.config"

def main():
    path, array_of_graphs = cnf_pr.parse_file(TMP_cnf_file)
    line_of_Parameters = csv_pr.fill_in_data(path, TMP_req_heads)

    gr.draw(line_of_Parameters[0], line_of_Parameters[2])
    gr.draw(line_of_Parameters[0], line_of_Parameters[3])

    print("Success!")

if __name__ == "__main__":
    main()