import lxml.etree as etree


def create_data_dict(xml_to_parse):
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


xml_to_parse = '.\\xml_files\\test_xml_episode1.xml'


if __name__ == '__main__':
    data = create_data_dict(xml_to_parse)
    print(data)
