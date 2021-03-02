import pytest

def test_1():
	assert '123'.isdigit()

def test_index_out(st = '123'):
	try:
		st[100] == '2'
	except IndexError:
		pass

@pytest.mark.parametrize("test_input,symbol,expected", 
[('Hello my name is Misha','m',3),
("Great, you've found an interesting secret!",'タ',0),
('','q',0)])
def test_count_symbol_in_str(test_input, symbol, expected):
    assert test_input.lower().count(symbol)==expected
