import pandas as pd
from pymarc import MARCReader

path = "data/uclo/uclo_"

out_1945 = '1945'
out_alkaro = 'alkaro'
out_ret = 'ret'
out_smz = 'smz'
out_int = 'int'
out_cle_I = 'cle_I'
out_cle_II = 'cle_II'
out_trl = 'trl'


databases = [out_1945, out_alkaro, out_ret, out_smz, out_int, out_cle_I, out_cle_II, out_trl]


def number_of_records(database):
    
    with open(database, 'rb') as data:
        # Nacteni marcu
        reader = MARCReader(data)
        
        counter = 0
        
        newest = 0000
        
        oldest = 2024
        
        for record in reader:
            for field in record.get_fields('008'):
                
                year = field.data[slice(7,11, None)]
                
                if year.isnumeric():
                    
                    year = int(year)
                    
                    if year < oldest:
                        oldest = year
                
                    if newest < year:
                        newest = year    
            
            counter += 1
       
    return (counter, oldest, newest) 


res = {}
for database in databases:
    path_to_database = path + database + ".mrc"
    (counter, oldest, newest) = number_of_records(path_to_database)
    print("Database " + database + " has " + str(counter) + " records. Newest: " + str(newest) + "; Oldest: " + str(oldest))
    res[database] = (counter, oldest, newest)
    
df = pd.DataFrame.from_dict(res)

out_csv = 'data/csv/out_cle.csv'

# DataFrame ulozime do formatu CSV
df.to_csv(out_csv, encoding = 'utf8', sep = ",", index=False)       
    
    