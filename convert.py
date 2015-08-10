# Conversion program to convert kilos to pounds and vice-versa


ans = raw_input("kg or lb: ")
num = raw_input("weight: ")

def from_kilograms(kilos):
	return kilos * 2.2
def from_pounds(pounds):
	return pounds / 2.2
def conversion():
		if ans == "kg":
			print from_kilograms(int(num)), "pounds"
		elif ans == "lb":
			print from_pounds(inte(num)), "kilograms"
		else:
			print "bye!"
			return