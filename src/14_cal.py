

import sys
import calendar
from datetime import datetime

args = sys.argv

if len(args) == 1:
    year = datetime.now().year
    month = datetime.now().month

print(args)


