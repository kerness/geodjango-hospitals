"""Load sample data to database"""


from boundaries import load as bl
from hospitals import load as hl


bl.run()
hl.run()