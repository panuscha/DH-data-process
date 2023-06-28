from pymarc import MARCReader
import pandas as pd
import json


in_B = 'data/ucla/ucla_B.mrc'
in_ret = 'data/ucla/ucla_ret.mrc'
in_smz = 'data/ucla/ucla_smz.mrc'
in_int = 'data/ucla/ucla_int.mrc'
in_cle = 'data/ucla/ucla_cle.mrc'
in_trl = 'data/ucla/ucla_trl.mrc'

out_B = 'data/csv/ucla_B.csv'
out_ret = 'data/csv/ucla_ret.csv'
out_smz = 'data/csv/ucla_smz.csv'
out_int = 'data/csv/ucla_int.csv'
out_cle = 'data/csv/ucla_cle.csv'
out_trl = 'data/csv/ucla_trl.csv'

databases_B = ['B12', 'B45', 'B97', 'B70', 'B80']  
database_ret = 'RET'
database_smz = 'SMZ'
database_int = 'INT'
database_cle = 'CLE'
database_trl = 'TRL'


def save_to_dict(r, database, dict):
    if not r is None:
        for field in r.get_fields('964'):
            if field['a'] in database:
                try:
                    tags = [] 
                    topics = []
                    description = []
                    genre = []   
                    for field in r.get_fields('600'):
                        topics.append(field['a'])

                    for field in r.get_fields('650'):
                        t = str(field['a'])
                        description.append(field['a'])
                    for field in r.get_fields('655'):
                        genre.append(field['a'])
                             
                    for field in r.get_fields():
                        tags.append(field.tag)    
                        
                    for field in r.get_fields('008'):
                        try:
                            dict['year'].append(str(field) [13:17])
                        except:
                            print("Year missing")    
                            dict['year'].append(None)

                    if '245' in tags:
                        dict['title'].append(r.title)
                    
                    if '100' in tags:
                        for field in r.get_fields('100'):
                            if '$a'in str(r['100']) :
                                dict['author'].append(str(r['100']['a']))
                            if '$7'in str(r['100']) :
                                dict['author code'].append(str(r['100']['7']))
                            else:
                                dict['author code'].append(None)    
                    else:    
                        dict['author code'].append(None)    
                        dict['author'].append(None)              

                    dict['figures'].append(topics)   
                    dict['description'].append(description)  
                    dict['genre'].append(genre)     
        
                except Exception as error:
                    print("Exception: " + type(error).__name__)  
                    print("964 Field: " + str(r.get_fields('964')))  
                    print("LDR: " + str(r.leader))   
    return dict            



with open(in_int, 'rb') as data:
    reader = MARCReader(data)
    dict = {'title': [], 
                    'author': [],
                    'author code': [],
                    'year': [],
                    'figures' : [],
                    'description' : [],
                    'genre' : [] } 
    for record in reader:
        dict = save_to_dict(record, database_int, dict)
    df = pd.DataFrame.from_dict(dict)
    df['figures'] = df['figures'].apply(lambda x: ';'.join(x))
    df['description'] = df['description'].apply(lambda x: ';'.join(x))
    df['genre'] = df['genre'].apply(lambda x: ';'.join(x))
    df.to_csv(out_int, encoding = 'utf8', sep = ",")    

# with open(in_B, 'rb') as data:
#     reader = MARCReader(data)
#     dict = {'title': [], 
#                     'author': [],
#                     'author code': [],
#                     'year': [],
#                     'figures' : [],
#                     'description' : [],
#                     'genre' : [] } 
#     for record in reader:
#         dict = save_to_dict(record, databases_B, dict)
#     df = pd.DataFrame.from_dict(dict)
#     df.to_csv(out_B, encoding = 'utf8' )           

# with open(in_cle, 'rb') as data:
#     reader = MARCReader(data)
#     dict = {'title': [], 
#                     'author': [],
#                     'author code': [],
#                     'year': [],
#                     'figures' : [],
#                     'description' : [],
#                     'genre' : [] } 
#     for record in reader:
#         dict = save_to_dict(record, database_cle, dict)
#     df = pd.DataFrame.from_dict(dict)
#     df.to_csv(out_cle, encoding = 'utf8' )         
    
# with open(in_ret, 'rb') as data:
#     reader = MARCReader(data)
#     dict = {'title': [], 
#                     'author': [],
#                     'author code': [],
#                     'year': [],
#                     'figures' : [],
#                     'description' : [],
#                     'genre' : [] } 
#     for record in reader:
#         dict = save_to_dict(record, database_ret, dict)
#     df = pd.DataFrame.from_dict(dict)
#     df.to_csv(out_ret, encoding = 'utf8' )    
    
# with open(in_smz, 'rb') as data:
#     reader = MARCReader(data)
#     dict = {'title': [], 
#                     'author': [],
#                     'author code': [],
#                     'year': [],
#                     'figures' : [],
#                     'description' : [],
#                     'genre' : [] } 
#     for record in reader:
#         dict = save_to_dict(record, database_smz, dict)
#     df = pd.DataFrame.from_dict(dict)
#     df.to_csv(out_smz, encoding = 'utf8' )              