# Below are questions I've come across during this project so far.

* Should I be using a virtual environment?
* How to read XML files with a declaration?
	- SOLUTION:	`with open(xml_to_parse, 'rb') as f:
					open_xml = f.read()`
* Should I use `openpyxl` or `csv` or...?
* What is the best way to iterate over files in directory, eg. `os.listdir()`, `os.scandir()`, or `os.walk()`?
* How should I handle errors?
* How to implement tests?
* How to write cleaner code?
* How to utilize `lxml` better?
* How to get attributes of an XML element?
	- SOLUTION: `.get("attribute_name")`
* How to better organize code/methods?
* How to better adhere to Python best practices?
* Am I violating any no-no's?
