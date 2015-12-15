from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from itertools import chain
from datetime import date
from datetime import datetime

categories = {
    'A': 'Arithmetic Routines',
    'B': 'Elementary Functions',
    'C': 'Equations and Special Functions',
    'D': 'Integration, Minimization, Non-linear Fitting',
    'E': 'Interpolation, Approximations, Linear Fitting',
    'F': 'Matrices, Vectors and Linear Equations',
    'G': 'Statistical Analysis and Probability',
    'H': 'Operation Research Techniques and Management Science',
    'I': 'Input/Output',
    'J': 'Output and Graphical Data Presentation',
    'K': 'Internal Information Transfer',
    'L': 'Executive Routines',
    'M': 'Data Handling',
    'N': 'Debugging, Error Handlng',
    'Q': 'Service or Housekeeping Programming Aids',
    'R': 'Logical and Symbolic',
    'T': 'Magnet and Beam Design, Electronics',
    'U': 'Quantum Mechanics, Particle Physics',
    'V': 'Random Numbers and General Purpose Utilities',
    'W': 'High Energy Physics Simulation, Kinematics, Phase Space',
    'X': 'Particle Detection, Measurement, Reconstruction',
    'Y': 'Statistical Data Analysis and Presentation',
    'Z': 'Miscellaneous System-Dependent Facilities',
}

class CategoryError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class WriteUp:


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

            # lookup heading for the Write-Up ID
            try:
                self.category = categories.get(self.ID[0])
                if not self.category:
                    raise
            except:
                raise CategoryError('unknown write-up category')


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
