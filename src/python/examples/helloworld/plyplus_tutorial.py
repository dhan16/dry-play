import os
from typing import List

from plyplus import Grammar
from plyplus.strees import STree

parser1 = Grammar(r"start: name ('\s*,' name)* ; name: '\w+' ;")
r = parser1.parse('cat ,milk,dog')


def __token(stree: STree):
    assert stree.head in ['section_token', 'keyword_token']
    assert len(stree.tail) == 1
    return str(stree.tail[0])


def __split(stree: STree):
    subsections = stree.tail
    return __token(subsections[0]), subsections[1:]


def __keyword_data(keyword_datas: List[STree]):
    if len(keyword_datas) == 0:
        return None
    lines = []
    for keyword_data in keyword_datas:
        assert keyword_data.head == 'keyword_data'
        assert len(keyword_data.tail) == 1
        data = str(keyword_data.tail[0])
        lines.append(data)
    return '\n'.join(lines)


parser2 = Grammar("""
    start: (section)+ 'END' ;
    section: section_token section_data ;
    section_token: 'RUNSPEC' | 'SCHEDULE' ;
    @section_data: (keyword)+ ;
    keyword: keyword_token (keyword_data)*;
    keyword_token: 'OIL' | 'WATER' | 'DIMENS' | 'GRIDOPTS' | 'DRSDT' ;
    keyword_data: '.+' ;
    NEWLINE: '[\n]+' (%ignore) ;
    """)


def parse_datafile(filename):
    with open(filename, "r") as f:
        content = f.read()
        r2 = parser2.parse(content)
        sections = r2.tail
        print('Found {} sections'.format(len(sections)))
        for section in sections:
            section_token, keywords = __split(section)
            print('Section {} has {} keywords'.format(section_token, len(keywords)))
            for keyword in keywords:
                keyword_token, keyword_datas = __split(keyword)
                print('Keyword {} has {} datas:{}'.format(keyword_token, len(keyword_datas),
                                                          __keyword_data(keyword_datas)))


if __name__ == '__main__':
    parse_datafile(os.path.join(os.path.dirname(__file__), 'plyplus_data1'))
