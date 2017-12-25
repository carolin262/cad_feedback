
import pandas as pd

class Json_parser:

    def se_file(self):
        csv_dataframe = pd.read_csv('se_feedback.csv')
        print("Done reading the se-csv file")
        return csv_dataframe

    def nx_file(self):
        csv_dataframe = pd.read_csv('nx_feedback.csv')
        print("Done reading the nx-csv file")
        return csv_dataframe

if __name__ == '__main__':
    json_parser_obj = Json_parser()
