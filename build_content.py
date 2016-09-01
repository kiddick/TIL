import os
import re

md_name = re.compile('\d{2}-\d{2}-\d{4}.md')

with open('README.md', 'a') as readme:
    for fname in os.listdir('.'):
        if md_name.match(fname):
            with open(fname, 'r') as _:
                content = [i.rstrip() for i in _.readlines()]
                for i, el in enumerate(content):
                    border = set(el)
                    if len(border) == 1 and '-' in border:
                        anchor = content[i-1].lower().replace(' ', '-').replace('\'', '').replace('/', '')
                        readme.write('* [{}]({}#{})\n'.format(
                            content[i-1], fname, anchor))


