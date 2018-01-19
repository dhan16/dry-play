import os
from plyplus import Grammar

parser1 = Grammar(r"start: name ('\s*,' name)* ; name: '\w+' ;")
r=parser1.parse('cat ,milk,dog')

parser2 = Grammar("""
    start: (section_rule)+ 'END' ;
    section_rule: section_keyword section_data ;
    @section_keyword: 'RUNSPEC' | 'SCHEDULE' ;
    section_data: (keyword_rule)+ ;
    keyword_rule: nodata_keyword | data_keyword_rule ;
    @nodata_keyword: 'OIL' | 'WATER' ;
    data_keyword_rule: keyword_keyword keyword_data '/';
    @keyword_keyword: 'DIMENS' | 'GRIDOPTS' | 'DRSDT' ;
    keyword_data: (word)* ;
    word: '\w+' ;
    SPACES: '[ ]+' (%ignore) ;
    NEWLINE: '[\n]+' (%ignore) ;
    """)
filename = os.path.join(os.path.dirname(__file__), 'plyplus_data1')
with open(filename, "r") as f:
    lines = f.readlines()
    content = "\n".join(lines)
    r2 = parser2.parse(content)
    print(r2)
    r2_list =  [x.tail[0] for x in r2.tail]
    print(r2_list)
