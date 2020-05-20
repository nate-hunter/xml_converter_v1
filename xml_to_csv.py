import lxml.etree as etree
import csv
import os


def create_ae_data_dict(xml_to_parse):
    # DATA PROVIDED BY A&E

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


def create_disney_data_dict(xml_to_parse):
    # DATA PROVIDED BY DISNEY

    with open(xml_to_parse, 'rb') as f:
        open_xml = f.read()

    root = etree.fromstring(open_xml)

    data_dict = {
        'series': '',
        'series_short_synopsis': '',
        'series_start_year': '',
        'season': '',
        'season_short_synopsis': '',
        'title': '',
        'episode_number': '',
        'runtime': '',
        'short_synopsis': '',
        'genre': '',
        'rating': '',
        'cast': '',
        'physical_release_date': ''
    }

    for key in data_dict:
        for element in root.iter(key):
            if element.tag == 'cast':
                list_actor = []
                for actor in element.getchildren():
                    actor_name = actor.get("name")
                    list_actor.append(actor_name)

                data_dict[element.tag] = '; '.join(list_actor)
            else:
                data_dict[element.tag] = element.text

    return data_dict


def create_discovery_data_dict(xml_to_parse):
    # NEXT STUDIO TO SETUP


def process_directory(directory, studio):
    """ TAKES A DIRECTORY OF XML METADATA AND OUTPUTS A LIST WHICH IS USED BY `write_to_csv()`."""

    list_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file = os.path.join(directory, filename)
            if studio == "A&E":
                ae_dict = create_ae_data_dict(file)
                list_data.append(ae_dict)
            elif studio == "Disney":
                # print("disney studio")
                disney_dict = create_disney_data_dict(file)
                # print(disney_dict)
                list_data.append(disney_dict)
            else:
                print(studio + " is not set up to convert XMLs to CSV at this time.")

    return list_data


def extract_columns(data):
    """ EXTRACTS COLUMNS TO USE IN `DictWriter()` """
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


if __name__ == '__main__':
    # test_ae_directory = '.\\xml_files'
    # ae_data = process_directory(test_ae_directory, "A&E")
    # write_to_csv('csv_output.csv', ae_data)

    thirty_for_thirty_directory = 'C:\\Users\\laway\\Box\\EST & Streampix\\Metadata By Month\\2020\\6. June\\TV\\Disney\\30 For 30'
    disney_data = process_directory(thirty_for_thirty_directory, "Disney")
    output_file_name = '\\_compiled_XMLs_' + \
        thirty_for_thirty_directory.split('\\')[-1] + '.csv'
    write_to_csv(thirty_for_thirty_directory + output_file_name, disney_data)
