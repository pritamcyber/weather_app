from time import gmtime, strftime
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

from datetime import datetime

print(datetime.now().strftime( '%H:%M:%S'))