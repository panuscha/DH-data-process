from pymarc import map_xml, MARCWriter
import re

file_path = 'data/uclo.xml'


out_1945 = 'data/uclo/uclo_1945.mrc'
out_alkaro = 'data/uclo/uclo_alkaro.mrc'
out_ret = 'data/uclo/uclo_ret.mrc'
out_smz = 'data/uclo/uclo_smz.mrc'
out_int = 'data/uclo/uclo_int.mrc'
out_cle_I = 'data/uclo/uclo_cle_I.mrc'
out_cle_II = 'data/uclo/uclo_cle_II.mrc'
out_trl = 'data/uclo/uclo_trl.mrc'

databases_1945 = ['B12', 'B45', 'B70', 'B80', 'B97', 'CLE', 'SMZ', 'INT' ]  
database_ret = 'RET'
database_smz = 'SMZ'
database_int = 'INT'
database_cle = 'CLE'
database_trl = 'TRL'
database_alkaro = 'ALKARO'


writer_1945 =  MARCWriter(open(out_1945, 'wb'))
writer_alkaro =  MARCWriter(open(out_alkaro, 'wb'))
writer_ret =  MARCWriter(open(out_ret, 'wb'))
writer_smz =  MARCWriter(open(out_smz, 'wb'))
writer_int =  MARCWriter(open(out_int, 'wb'))
writer_cle_I =  MARCWriter(open(out_cle_I, 'wb'))
writer_cle_II =  MARCWriter(open(out_cle_II, 'wb'))
writer_trl =  MARCWriter(open(out_trl, 'wb'))


pattern = r'\)(.*)'

def save_databases(r):
    try:
        for clb in r.get_fields('599'):
            if 'CLB-CPK' in clb.value():
                for field in r.get_fields('964'):
                    r.remove_fields('LDR')
                    r.remove_fields('FMT')
                    
                    if field['a'] in databases_1945:
                        try:
                            writer_1945.write(r)   
                        except Exception as error:
                            print("Exception: " + type(error).__name__) 
                            
                    if field['a'] in database_alkaro:
                        try:
                            writer_alkaro.write(r)   
                        except Exception as error:
                            print("Exception: " + type(error).__name__) 

                    if field['a'] in database_ret:
                        try:
                            writer_ret.write(r)   
                        except Exception as error:
                            print("Exception: " + type(error).__name__) 
                            
                    if field['a'] in database_smz:
                        try:
                            writer_smz.write(r)   
                        except Exception as error:
                            print("Exception: " + type(error).__name__) 
                            
                    if field['a'] in database_int:
                        try:
                            writer_int.write(r)   
                        except Exception as error:
                            print("Exception: " + type(error).__name__)  

                    if field['a'] in database_trl:
                        try:
                            writer_trl.write(r)   
                        except Exception as error:
                            print("Exception: " + type(error).__name__) 

                    if field['a'] in database_cle:
                        try:
                            for cle in r.get_fields('035'): 
                                match = re.search(pattern, str(cle.value()))
                                if match: 
                                    res = match.group(1)
                                    if res[0] == '1' or (len(res[0])> 2 and  res[0] == '001'):   
                                        writer_cle_I.write(r)  
                                    if res[0] == '2' or (len(res[0])> 2 and  res[0] == '002'):   
                                        writer_cle_II.write(r)       
                        except Exception as error:
                            print(r)
                            print("Exception: " + type(error).__name__)         
    except Exception as error:
                            print("CLB")
                            print(r)
                            print("Exception: " + type(error).__name__)                         
                                                                 
try:  
    map_xml(save_databases, file_path)
    
except Exception as error:
     print("CLB ERROR")
     print("Exception: " + type(error).__name__)      
finally:
    writer_1945.close()
    writer_alkaro.close()
    writer_int.close()
    writer_ret.close()
    writer_smz.close()
    writer_trl.close()
    writer_cle_I.close()
    writer_cle_II.close() 

