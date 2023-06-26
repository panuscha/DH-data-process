from pymarc import map_xml
import csv


file_path = 'data/ucla.xml'

out = 'data/b_only_subset.csv'
out_description = 'data/description.csv'
out_years = 'data/years.csv'

database = ['B12', 'B45', 'B97', 'B70', 'B80' ] #, 'INT','SMZ', 'CLE'

types = {}


counter = 0
csvfile = open(out, 'w', encoding='utf-8')
writer = csv.DictWriter(csvfile, fieldnames = ['title', 'author', 'author code', 'year', 'figures', 'description', 'genre'], delimiter=';')
writer.writeheader()
def save_B45(r):
    global df, counter
    for field in r.get_fields('964'):
        if field['a'] in database:
            counter += 1
            try:
                figures = ""
                description = ""
                genre = ""   
                for field in r.get_fields('600'):
                    #figures.append(field['a'])
                    figures +=  str(field['a']) + "$"
                for field in r.get_fields('650'):
                    t = str(field['a'])
                    description += t + "$"
                    if not t in types.keys():
                        types[t] = 1
                    else:
                        types[t] = +1 
                for field in r.get_fields('655'):
                    genre += str(field['a']) + "$"     
                    
                dict = {'title': None, 
                    'author': None,
                    'author code': None,
                    'year': None,
                    'figures' : None,
                    'description' : None,
                    'genre' : None }   
                
                for field in r.get_fields('008'):
                    try:
                        dict['year'] = str(field) [13:17]
                    except:
                        print("Year missing")    
                        
                for field in r.get_fields('245'):
                    dict['title'] = field['a']
                
                for field in r.get_fields('100'):
                    if '$a'in str(r['100']) :
                        dict['author'] = str(r['100']['a'])   
                    if '$7'in str(r['100']) :
                        dict['author code'] = str(r['100']['7'])    
                        
                if figures != "":
                    dict['figures'] = figures   
                
                if description != "":
                    dict['description'] = description  
                
                if genre != "":
                    dict['genre'] = genre     
                    
                writer.writerow(dict)      
            except Exception as error:
                print("Exception: " + type(error).__name__)  
                print("964 Field: " + str(r.get_fields('964')))  
                print("LDR: " + str(r.get_fields('LDR')))      
try:  
    map_xml(save_B45, file_path)
    
except Exception as error:
     print("Exception: " + type(error).__name__)      
finally:
    csvfile.close()
    print(counter)



          
     

