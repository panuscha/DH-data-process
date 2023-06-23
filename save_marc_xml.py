from pymarc import map_xml
import csv


file_path = 'data/ucla.xml'

out = 'data/b45.csv'
out_description = 'data/description.csv'
out_years = 'data/years.csv'

databaze = ['B45', 'B12']

types = {}
years = {}


csvfile = open('data/b45_dict.csv', 'w', encoding='utf-8')
writer = csv.DictWriter(csvfile, fieldnames = ['title', 'author', 'author code', 'year', 'figures', 'description', 'genre'], delimiter=';')
writer.writeheader()
def save_B45(r):
    global df
    if 'B45' in r['964']['a']:
        #try:
            y = str(r['008']) [13:17]
            if not y in years:
                years[y] = 1
            else:
                years[y] = +1  
        
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
                
            dict = {'title': r.title, 
                'author': None,
                'author code': None,
                'year': str(y),
                'figures' : None,
                'description' : None,
                'genre' : None }    
                
            
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
        # except Exception as error:
        #         print("Exception: " + type(error).__name__)         
try:  
    map_xml(save_B45, file_path)
except Exception as error:
     print("Exception: " + type(error).__name__)      
finally:
    csvfile.close()




          
     

