from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from itertools import chain
from datetime import date
from datetime import datetime

class WriteUp:

    author = ''
    ID = ''

    def __init__(self, fileName):
        self._fileName = fileName
        with open(self._fileName, 'r') as file:
            content = file.read()

            # parse Author field from tex
            self.title = re.search(r'.*\\Cernhead{(.*?)}', content).group(1).strip()

            # parse Author field from tex
            self.author = re.search(r'.*\\Author{(.*?)}', content).group(1).strip()

            # parse submitter from tex
            self.submitter = re.search(r'.*\\Submitter{(.*?)}', content).group(1).strip()

            # parse Routine ID from tex
            self.ID = re.search(r'.*\\Routid{(.*?)}', content).group(1).strip()

            # parse keyword fields from tex
            self.keywords = re.findall(r'\\Keywords{(.*?)}', content)
            self.keywords = list(map(lambda s: s.split(), self.keywords))
            self.keywords = list(chain.from_iterable(self.keywords))
            self.keywords = list(map(lambda s: s.lower(), self.keywords))

            # parse keyword fields from tex
            self.routines = re.findall(r'\\Rdef{(.*?)}', content)
            self.routines = list(map(lambda s: s.split(), self.routines))
            self.routines = list(chain.from_iterable(self.routines))
            self.routines = list(map(lambda s: s.lower(), self.routines))

            # parse programming language from tex
            self.language = re.search(r'.*\\Language{(.*?)}', content).group(1).lower().strip()

            # parse library from tex
            self.library = re.search(r'.*\\Library{(.*?)}', content).group(1).lower().strip()

            # parse submission date from tex
            bdt = datetime.strptime(re.search(r'.*\\Submitted{(.*?)}', content).group(1),"%d.%m.%Y")
            self.submitted = date(bdt.year,bdt.month,bdt.day)

            # parse revision date from tex
            bdt = datetime.strptime(re.search(r'.*\\Revised{(.*?)}', content).group(1),"%d.%m.%Y")
            self.revised = date(bdt.year,bdt.month,bdt.day)
