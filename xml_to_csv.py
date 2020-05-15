import lxml.etree as etree
import csv


def create_data_dict(xml_to_parse):
    '''DATA PROVIDED BY A & E'''
    with open(xml_to_parse) as f:
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


def write_to_csv(filename, data):
    columns = []

    for k in data:
        columns.append(k)

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerow(data)


xml_to_parse = '.\\xml_files\\test_xml_episode1.xml'


if __name__ == '__main__':
    data = create_data_dict(xml_to_parse)
    write_to_csv('csv_output.csv', data)
