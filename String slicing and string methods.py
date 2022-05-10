mystr = 'my name is fariha tabassum eshitå. My age is {0}'

print(mystr.capitalize()) #Converts the first character to upper case
print(mystr.casefold()) #Converts string into lower case
#print(mystr.center('fariha'))
print(mystr.count('a')) #Returns the number of times a specified value occurs in a string

'''Encode errors types'''
print(mystr.encode(encoding='ascii', errors='backslashreplace'))
print(mystr.encode(encoding='ascii', errors='ignore'))
print(mystr.encode(encoding='ascii', errors='namereplace'))
print(mystr.encode(encoding='ascii', errors='replace'))
print(mystr.encode(encoding="ascii", errors="xmlcharrefreplace"))

print(mystr.endswith('eshi')) #Returns true if the string ends with the specified value
print('H\te\tl\tl\to'.expandtabs(10)) #Sets the tab size of the string
print(mystr.find('fariha')) #Searches the string for a specified value and returns the position of where it was found
print(mystr.format('25')) #Formats specified values in a string
#print(mystr.format_map(25)) Formats specified values in a string
print(mystr.index('fariha')) #Searches the string for a specified value and returns the position of where it was found
print(mystr.isalnum()) #Returns True if all characters in the string are alphanumeric
print(mystr.isalpha()) #Returns True if all characters in the string are in the alphabet
print(mystr.isascii()) #Returns True if all characters in the string are ascii characters
print(mystr.isdecimal()) #Returns True if all characters in the string are decimals
print(mystr.isdigit()) #Returns True if all characters in the string are digits
print(mystr.isidentifier()) #Returns True if the string is an identifier
print(mystr.islower()) #Returns True if all characters in the string are lower case
print(mystr.isnumeric()) #Returns True if all characters in the string are numeric
print(mystr.isprintable()) #Returns True if all characters in the string are printable
print(mystr.isspace()) #Returns True if all characters in the string are whitespaces
print(mystr.istitle()) #Returns True if the string follows the rules of a title
print(mystr.isupper()) #Returns True if all characters in the string are upper case
print('#'.join(mystr)) #Converts the elements of an iterable into a string
print('Hello!!'.ljust(20), mystr) #Returns a left justified version of the string
print(mystr.lower()) #Converts a string into lower case
print(mystr.lstrip()) #Returns a left trim version of the string
print(mystr.translate(mystr.maketrans('a', 'A'))) #Returns a translated string, Returns a translation table to be used in translations
print(mystr.partition('fariha')) #Returns a tuple where the string is parted into three parts
print(mystr.replace('eshitå', 'eshi'))
print(mystr.rfind('fariha')) #Searches the string for a specified value and returns the last position of where it was found
print(mystr.rindex('fariha')) #Searches the string for a specified value and returns the last position of where it was found
print('Hello!!'.rjust(20), mystr) #Returns a right justified version of the string
print(mystr.rpartition('fariha')) #Returns a tuple where the string is parted into three parts
print(mystr.rsplit(', ')) #Splits the string at the specified separator, and returns a list
print('Hello!!',mystr.rstrip(), 'bye!!') #Returns a right trim version of the string
print(mystr.split()) #Splits the string at the specified separator, and returns a list
print(mystr.splitlines()) #Splits the string at line breaks and returns a list
print(mystr.startswith('my')) #Returns true if the string starts with the specified value
print(mystr.strip()) #Returns a trimmed version of the string
print(mystr.swapcase()) #Swaps cases, lower case becomes upper case and vice versa
print(mystr.title()) #Converts the first character of each word to upper case
print(mystr.upper()) #Converts a string into upper case
print('20'.zfill(3)) #Fills the string with a specified number of 0 values at the beginning
