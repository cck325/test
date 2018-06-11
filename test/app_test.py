#from products_app.app import *  # this will import all the functions
from products_app.app import enlarge
#from products_app.app import auto_incremented_id

def test_enlarge():
    result = enlarge(40)
    assert result == 4000


#def test_auto_incr_id():
#    products = [
#        {"id": 45, "name":"testing", "aisle":"testing", "department":"test"}
#    ]
#    result = auto_incremented_id(prudcts)
#    assert result == 50
