from pymarc import map_xml, Record, TextWriter, MARCWriter
from copy import deepcopy

file_path = 'data/ucla.xml'

out_B = 'data/ucla/ucla_B.mrk'
out_ret = 'data/ucla/ucla_ret.mrk'
out_smz = 'data/ucla/ucla_smz.mrk'
out_int = 'data/ucla/ucla_int.mrk'
out_cle = 'data/ucla/ucla_cle.mrk'
out_trl = 'data/ucla/ucla_trl.mrk'

databases_B = ['B12', 'B45', 'B97', 'B70', 'B80']  
database_ret = 'RET'
database_smz = 'SMZ'
database_int = 'INT'
database_cle = 'CLE'
database_trl = 'TRL'

writer_B =  TextWriter(open(out_B, 'wt', encoding='utf8' ))
writer_ret =  TextWriter(open(out_ret, 'wt', encoding='utf8'))
writer_smz =  TextWriter(open(out_smz, 'wt', encoding='utf8'))
writer_int =  TextWriter(open(out_int, 'wt', encoding='utf8'))
writer_cle =  TextWriter(open(out_cle, 'wt', encoding='utf8'))
writer_trl =  TextWriter(open(out_trl, 'wt', encoding='utf8'))


def save_databases(r):
    for field in r.get_fields('964'):
        r.remove_fields('LDR')
        r.remove_fields('FMT')
        if field['a'] in databases_B:
            try:
                writer_B.write(r)   
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
         
        if field['a'] in database_cle:
            try:
                writer_cle.write(r)   
            except Exception as error:
                print("Exception: " + type(error).__name__) 
                
        if field['a'] in database_trl:
            try:
                writer_trl.write(r)   
            except Exception as error:
                print("Exception: " + type(error).__name__)                                              
try:  
    map_xml(save_databases, file_path)
    
except Exception as error:
     print("Exception: " + type(error).__name__)      
finally:
    writer_B.close()
    writer_cle.close()
    writer_int.close()
    writer_ret.close()
    writer_smz.close()
    writer_trl.close()

