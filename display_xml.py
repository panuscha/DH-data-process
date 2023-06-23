from pymarc import map_xml

file_path = 'data/ucla.xml'

def print_record(r):
    print(r)

map_xml(print_record, file_path)