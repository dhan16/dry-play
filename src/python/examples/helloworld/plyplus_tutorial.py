from plyplus import Grammar

parser1 = Grammar(r"start: name ('\s*,' name)* ; name: '\w+' ;")
r=parser1.parse('cat ,milk,dog')


# parser1 = Grammar(r"start: section_rule (section_rule)* ;"
#                   r"section_rule: SECTION_KEYWORD section_data ;"
#                   r"SECTION_KEYWORD: RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE | OPTIMIZE ;"
#                   r"section_data: (keyword_rule)+ ;"
#                   r"keyword_rule: KEYWORD_KEYWORD keyword_data ;"
#                   r"KEYWORD_KEYWORD: DIMENS | GRIDOPTS | START | SATNUM | RPTSCHED ;"
#                   r"keyword_data: (word)* ;"
#                   r"word: \w+' ;")

print(r)