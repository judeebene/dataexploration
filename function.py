
def arr(lower,upper ):

	evenList =[]

	if(upper > lower):
		for i in range(lower,upper +1):

			if (i % 2 == 0):
				evenList.append(i)




		return evenList
		


def combine_and_sort(listA,listB):

	
	listA.extend(listB)

	sortedlist =sorted(listA)

	return sortedlist




def create_dictionary(lower,upper):
	evenList =[]
	oddList = []
	number_dict ={}
	if(upper > lower):
		for i in range(lower,upper +1):

			if (i % 2 == 0):
				#dict with even key
				evenList.append(i)
				number_dict['even'] = evenList;
			else:
				#dict with odd key
				oddList.append(i)
				number_dict['odd'] = oddList


		return number_dict







def string_reverse(text):
    new_string = []
    index = len(text)
    while (index > 0):
        new_string.append(text[index-1])
        index -= 1
    return ''.join(new_string)



#create_dictionary(7,12)

string_reverse('jude')



def check_anagram(wordA,wordB):

    if len(wordA) == len(wordB):
        if set(wordA) == set(wordB):

            return sorted(list(wordA))== sorted(list(wordB))
    return False




def  to_roman(number):
	if (0 < number < 5000):
		result = ""
		romanMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

		result =''
		for numeral, integer in romanMap:
			while number >= integer:
				result += numeral
			
				number -= integer
			print result
					
			
			

		
	else:
		print "number out of range (must be 1-5000)"
	



def from_roman(roman_string):
	romanMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))
	result = 0
	index = 0
	for numeral, integer in romanMap:
		while roman_string[index:index+len(numeral)] == numeral:
			result += integer
			index += len(numeral)
   	print result
	







from_roman('CCC')