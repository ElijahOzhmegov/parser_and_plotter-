import csv_parser    as csv_pr
import config_parser as cnf_pr
import grapher       as gr

TMP_cnf_file = "csv_config.config"

def main():
    path, array_of_graphs = cnf_pr.parse_file(TMP_cnf_file)

    required_heads = cnf_pr.extract_headers(array_of_graphs)

    line_of_Parameters = csv_pr.fill_in_data(path, required_heads)

    gr.draw(array_of_graphs, line_of_Parameters)

    print("Success!")

if __name__ == "__main__":
    main()