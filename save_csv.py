import pandas as pd
import re 
from pymarc import MARCReader

def save_to_dict(record, dict, field_list):
    if not record is None:
        try:
            # Iterace skrz tuples v seznamu field_list
            for field_tags in field_list:
                # Nazev klice ve slovniku
                dict_key_name =  field_tags[0]

                # Tag pole
                tag =  field_tags[1]

                # Tag podpole
                subfield_tag =  field_tags[2]
                
                # Seznam do ktereho pridame hodnoty a nasledne pridame do slovniku
                dict_add_list = []
                
                # Iterace pres vsechna pole s tagem 'tag'
                for field in record.get_fields(tag):
                    
                    # Pokud pole nema zadna podpole, pridame cele pole do listu dict_add_list
                    if subfield_tag is None:
                        dict_add_list.append(field.data)
                    
                    # Pokud subtag je instance slice, tedy to znamena, ze chceme jen nejakou cast pole, ktera neni definovana subpolem,
                    # pridame cast pole do slovniku dict_add_list    
                    elif isinstance(subfield_tag, slice):
                        dict_add_list.append(field.data [subfield_tag])     
                    
                    # Pokud pole obsahuje podpole, pridame do slovniku dict_add_list jen podpole
                    elif '$'+subfield_tag in str(field):  
                        dict_add_list.append(str(field[subfield_tag]))

                # Do klice z tuplu pridame cely seznam dict_add_list         
                dict[dict_key_name].append(dict_add_list)
        except Exception as error:
            print("Exception: " + type(error).__name__)  
            print("LDR: " + str(record.leader))   
    return dict 

# 'data/ucla/ucla_B.mrc'
# 'data/ucla/ucla_ret.mrc'
# 'data/ucla/ucla_smz.mrc'
# 'data/ucla/ucla_int.mrc'
# 'data/ucla/ucla_cle.mrc'

# Cesta k marcovemu dokumentu
database = 'data/ucla/ucla_ret.mrc'

out = 'data/csv/out_ret.csv'

with open(database, 'rb') as data:
    reader = MARCReader(data)
    # List poli, ktere si chceme ulozit
    field_list = [('title', '245', 'a'),
                ('author', '100', 'a'),
                ('author code', '100', '7'),
                # Rok je schovany v poli 008 na 8. az 11. miste, proto vyuzijeme funkci slice
                ('year', '008', slice(7,11, None)), #7-11
                ('figures', '600', 'a'),
                ('description', '650', 'a'),
                ('genre', '655', 'a'),
                ('magazine', '773', 't')]
    dict = {}
    for t in field_list:
        dict_key_name = t[0]
        dict[dict_key_name] = []
    for record in reader:
        dict = save_to_dict(record, dict, field_list)
    df = pd.DataFrame.from_dict(dict)

    # U jmen si chceme ulozit jmeno a prijmeni bez koncove carky ',', ktera je na konci stringu
    df['figures'] = df['figures'].apply(lambda x: [y.strip(' ,') if len(y) > 0  else y for y in x])  
    df['author'] = df['author'].apply(lambda x: [y.strip(' ,') if len(y) > 0 else y for y in x]) 

    # Nazev si chceme ulozit bez lomitka '/', ktere je na konci stringu
    df['title'] = df['title'].apply(lambda x: [y.strip(' /') if len(y) > 0 else y for y in x])  


    # Aby se nam list hodnot lepe ukladal, vytvorime z listu jeden string a jednotlive elementy spojime strednikem ';' 
    for column in df.columns:
        df[column] = df[column].apply(lambda x: ';'.join(x))
    df.to_csv(out, encoding = 'utf8', sep = ",") 