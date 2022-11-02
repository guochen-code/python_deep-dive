a = 0.1
format(a,'.20f')

from datetime import datetime
now = datetime.utcnow()
format(now, '%a %Y-%m-%d %I:%M %p') -> Sun 2019-06-09 04:23 PM

***********************************************************************************
def __repr__(self):
  return f'Person(name={self.name}, dob={self.dob.isoformat()})'

def __str__(self):
  return f'Person({self.name})'

def __format__(self, date_format_spec):
  dob=format(self.dob, date_format_spec)
  return f'Person(name={self.name},dob={dob})'

from datetime import date

p = Person('Alex', date(1980,10,20))

str(p) -> 'Person(Alex)'

repr(p) -> 'Person(Alex, dob=1900-10-20)'

format(p, '%B %d, %Y') -> 'Person(name=Alex, dob=October 26, 1980)'
