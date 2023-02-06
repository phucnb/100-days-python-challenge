from main import find_highest_bidders
import random

bidders = {
'Jessica Wilson' : 5,
'Jessica Moore' : 1,
'Sophia Brown' : 4,
'Jim Jones' : 3,
'Jane Taylor' : 5,
'Jessica Taylor' : 9,
'Jim Smith' : 3,
'John Johnson' : 2,
'Ethan Taylor' : 2,
'Jessica Smith' : 9,
'Ethan Wilson ' : 0,
'Jacob Wilson' : 5,
'Jane Wilson' : 9,
'Emily Moore' : 1,
'Ethan Jones' : 5,
'Sophia Moore' : 5,
'Jane Jones' : 8,
'Jim Johnson' : 4,
'Emily Williams' : 2,
'Jane Davis' : 8,
'Jim Miller' : 2,
'Michael Jones' : 2
}
    
def test_find_highest_bidders():
    assert find_highest_bidders(bidders) == {'Jessica Taylor' : 9, 'Jessica Smith': 9, 'Jane Wilson': 9}