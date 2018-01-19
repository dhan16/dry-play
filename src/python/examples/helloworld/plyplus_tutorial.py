import os
from plyplus import Grammar

parser1 = Grammar(r"start: name ('\s*,' name)* ; name: '\w+' ;")
r=parser1.parse('cat ,milk,dog')

parser2 = Grammar("""
    start: (section_rule)+ 'END' ;
    section_rule: section_token section_data ;
    section_token: 'RUNSPEC' | 'SCHEDULE' ;
    section_data: (keyword_rule)+ ;
    @keyword_rule: nodata_token | data_keyword_rule ;
    @nodata_token: 'OIL' | 'WATER' ;
    data_keyword_rule: data_token keyword_data '/';
    data_token: 'DIMENS' | 'GRIDOPTS' | 'DRSDT' ;
    keyword_data: ('\w+')* ;
    SPACES: '[ ]+' (%ignore) ;
    NEWLINE: '[\n]+' (%ignore) ;
    """)
filename = os.path.join(os.path.dirname(__file__), 'plyplus_data1')
with open(filename, "r") as f:
    lines = f.readlines()
    content = "\n".join(lines)
    r2 = parser2.parse(content)
    r2_list =  [x.tail for x in r2.tail]
    print(len(r2_list))
    for e in r2_list:
        print(e)
