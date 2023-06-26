<<<<<<< HEAD
from pymarc import map_xml

file_path = 'data/ucla.xml'

database = ['B12', 'B45', 'B97', 'B70', 'INT', 'MBK-PL-OPO',  ]

def print_record(r):
    for field in r.get_fields('964'):
        if field['a'] not in database:
            print(field['a'])
            database.append(field['a'])

=======
from pymarc import map_xml

file_path = 'data/ucla.xml'

def print_record(r):
    print(r)

>>>>>>> origin/main
map_xml(print_record, file_path)