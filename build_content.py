import datetime
import os
import re

md_name = re.compile('\d{2}-\d{2}-\d{4}.md')
md_list = []


for fname in os.listdir('.'):
    if md_name.match(fname):
        md_list.append(fname)


def todate(i):
    i = i[:-3]
    return datetime.datetime.strptime(i, '%m-%d-%Y')

md_list.sort(key=todate)

print md_list
with open('README.md', 'a') as readme:
    for fname in md_list:
        with open(fname, 'r') as _:
            content = [i.rstrip() for i in _.readlines()]
            for i, el in enumerate(content):
                border = set(el)
                if len(border) == 1 and '-' in border:
                    anchor = content[i-1].lower().replace(' ', '-').replace('\'', '').replace('/', '')
                    readme.write('* [{}]({}#{})\n'.format(
                        content[i-1], fname, anchor))
