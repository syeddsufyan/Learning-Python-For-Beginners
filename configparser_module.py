import configparser
config = configparser.ConfigParser()
config.read('C:\\Users\\LENOVO\\.spyder-py3\\config\\spyder.ini')
config.sections()
[option for option in config['help']]

parser = configparser.ConfigParser()
parser.read_dict(
	{'section1' :
		{'tag1': '1', 'tag2' : '2', 'tag3' : '3'},
	 'section2':
	 	{'tagA' : 'bar', 'tagB' : 'B', 'tagC' : 'C'},
	 'section3':
	 	{'foo' : 'x', 'bar' : 'y', 'baz' : 'z'} })
parser.sections()
[option for option in parser['section1']]