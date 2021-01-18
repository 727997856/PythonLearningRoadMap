# !/usr/bin/python3
# encoding: utf-8

import re


def pattern_hello():
    dist_str = 'hello world!'

    # 下面两行代码 等效于 match = re.match(r'hello', dist_str)
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r'hello')
    # 使用Pattern匹配文本，或得匹配结果，无法匹配则返回None
    match = pattern.match(dist_str)

    if match:
        print(match.group())
    # output：
    # hello


def show_match_properties():
    match = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!!!')

    print('match.string:', match.string)
    print('match.re:', match.re)
    print('match.pos:', match.pos)
    print('match.endpos:', match.endpos)
    print('match.lastindex:', match.lastindex)
    print('match.lastgroup:', match.lastgroup)

    print('match.group():', match.group())
    print('match.group(1, 2):', match.group(1, 2))
    print('match.groups():', match.groups())
    print('match.groupdict():', match.groupdict())
    print('match.start(2):', match.start(2))
    print('match.end(2):', match.end(2))
    print('match.span(2):', match.span(2))
    print(r"match.expand(r'\3\2 \1'):", match.expand(r'\3\2 \1'))

    # output:
    # match.string: hello world!
    # match.re: <_sre.SRE_Pattern object at 0x016E1A38>
    # match.pos: 0
    # match.endpos: 12
    # match.lastindex: 3
    # match.lastgroup: sign
    # match.group(): 'hello world!'
    # match.group(1,2): ('hello', 'world')
    # match.groups(): ('hello', 'world', '!')
    # match.groupdict(): {'sign': '!'}
    # match.start(2): 6
    # match.end(2): 11
    # match.span(2): (6, 11)
    # match.expand(r'\2 \1\3'): world hello!


def show_pattern_properties():
    pat = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

    print('pat.pattern:', pat.pattern)
    print('pat.flags:', pat.flags)
    print('pat.groups:', pat.groups)
    print('pat.groupindex:', pat.groupindex)

    # output:
    # pat.pattern: (\w+)(\w +)(?P < sign >.*)
    # pat.flags: 48
    # pat.groups: 3
    # pat.groupindex: {'sign': 3}


def pattern_match():
    pass


def pattern_search():
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r'world')

    # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
    # 这个例子中使用match()无法成功匹配
    match = pattern.search('hello world!')
    if match:
        # 使用Match获得分组信息
        print(match.group())

    # output:
    # world


def pattern_split():
    """
    按照能够匹配的子串将string分割后返回列表
    maxsplit用于指定最大分割次数，不指定将全部分割
    """
    p = re.compile(r'\d+')
    print(p.split('one1two2three3four4'))

    # output:
    # ['one', 'two', 'three', 'four', '']


def pattern_findall():
    """
    搜索string，以列表形式返回全部能匹配的子串
    """
    p = re.compile(r'\d+')
    print(p.findall('one1two2three3four4'))

    # output
    # ['1', '2', '3', '4']


def pattern_finditer():
    """
    搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器
    """
    p = re.compile(r'\d+')
    for m in p.finditer('one1two2three3four4'):
        print(m.group())

    # output
    # 1 2 3 4


def pattern_sub():
    p = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world!'

    print(p.sub(r'\2 \1', s))
    print(p.sub(lambda m: m.group(1).title() + ' ' + m.group(2).title(), s))

    # output
    # say I, world hello!
    # I Say, Hello World!


def pattern_subn():
    """
    返回 (sub(repl, string[, count]), 替换次数)
    """
    p = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world!'

    print(p.subn(r'\2 \1', s))
    print(p.subn(lambda m: m.group(1).title() + ' ' + m.group(2).title(), s))

    # output
    # ('say i, world hello!', 2)
    # ('I Say, Hello World!', 2)


if __name__ == '__main__':
    # show_match_properties()
    # show_pattern_properties()
    pattern_match()
    pattern_search()
    pattern_split()
    pattern_findall()
    pattern_finditer()
    pattern_sub()
    pattern_subn()
