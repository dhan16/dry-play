import os
from plyplus import Grammar

parser1 = Grammar(r"start: name ('\s*,' name)* ; name: '\w+' ;")
r=parser1.parse('cat ,milk,dog')

parser2 = Grammar("""
    start: (section)+ 'END' ;
    section: section_keyword section_data ;
    section_keyword: 'RUNSPEC' | 'SCHEDULE' ;
    @section_data: (keyword_rule)+ ;
    @keyword_rule: nodata_keyword | data_keyword_rule ;
    nodata_keyword: 'OIL' | 'WATER' ;
    data_keyword_rule: data_keyword (data)+;
    data_keyword: 'DIMENS' | 'GRIDOPTS' | 'DRSDT' ;
    data: '.+' ;
    NEWLINE: '[\n]+' (%ignore) ;
    """)
filename = os.path.join(os.path.dirname(__file__), 'plyplus_data1')
with open(filename, "r") as f:
    content = f.read()
    r2 = parser2.parse(content)
    r2_list =  [x.tail for x in r2.tail]
    print(len(r2_list))
    for e in r2_list:
        print(e)
