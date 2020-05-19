import lxml.etree as etree
import csv
import os


def create_ae_data_dict(xml_to_parse):  # DATA PROVIDED BY A&E

    with open(xml_to_parse, encoding='utf-8') as f:
        open_xml = f.read()

    root = etree.fromstring(open_xml)

    data_dict = {
        'Series': '',
        'Season': '',
        'Title': '',
        'EpisodeNumber': '',
        'Description': '',
        'SeasonDescription': '',
        'Actor1': '',
        'Actor2': '',
        'Rating': '',
        'Genre': '',
        'Duration': '',
        'ReleaseYear': ''
    }

    for child in root.getchildren():
        if not child.text == 'N/A':
            if child.tag in data_dict:
                data_dict[child.tag] = child.text
    return data_dict


# TAKES A DIRECTORY OF XML METADATA AND OUTPUTS A LIST WHICH IS USED BY
# `write_to_csv()`.
def process_directory(directory):
    list_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file = os.path.join(directory, filename)
            ae_dict = create_ae_data_dict(file)
            list_data.append(ae_dict)
    return list_data


def extract_columns(data):  # EXTRACTS COLUMNS TO USE IN `DictWriter()`
    columns = []

    column_headers = data[0]

    for key in column_headers:
        columns.append(key)

    return columns


def write_to_csv(filename, data):
    columns = extract_columns(data)

    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


xml_to_parse = '.\\xml_files\\S10 E9 - AETN-222628PAR_THC_AXMN_S010-CONTENT_HD-SnappinTrees-v202004242259.xml'

''' RESOLVE THE ERROR BELOW TO READ XML FILES WITH A DECLARATION:
        ValueError: Unicode strings with encoding declaration are not supported. Please use bytes input or XML fragments without declaration.
'''

directory = '.\\xml_files'

if __name__ == '__main__':
    ae_data = process_directory(directory)
    write_to_csv('csv_output.csv', ae_data)
