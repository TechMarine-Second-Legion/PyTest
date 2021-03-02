import pytest

def test_1():
	assert type({'1':1})==type({})
	
@pytest.mark.parametrize("test_input,expected", [(3,{2:8, 3:27, 4:64}),(-10,{}),(0,{}),(1,{0:0})])
def test_create_dict(test_input, expected):
    assert {x: x**3 for x in range(test_input-1,test_input*2-1)}==expected

def test_take_non_existent_element(d = {'1':1}):
	try:
		assert d['2']==2
	except KeyError:
		pass




