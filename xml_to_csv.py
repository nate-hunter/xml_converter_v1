import lxml.etree as etree


file_to_parse = '.\\xml_files\\test_xml_episode1.xml'
xml_file = file_to_parse
# print(xml_file)


open_xml = open(xml_file).read()
# print(open_xml)


root = etree.fromstring(open_xml)
# print(root.tag)


data_dict = {}

# FUNCTION TO PRINT XML TAGS


def print_xml_tags(root):
    for child in root.getchildren():
        if not child.text == 'N/A':
            data_dict[child.tag] = child.text
        # if child.tag == 'Description' or child.tag == 'SeasonDescription':
        #     print(child.tag + ':  (Character Length: ' +
        #           str(len(child.text)) + ')')
        #     print('\t' + child.text)
        # else:
        #     print(child.tag + ':')
        #     print('\t' + child.text)
    print(data_dict)

if __name__ == '__main__':
    print_xml_tags(root)
