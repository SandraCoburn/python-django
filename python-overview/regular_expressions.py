import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other.'

for pattern in patterns:
  print('Im searching for: ' + pattern)

  if re.search(pattern,text):
    print("MATCH")
  else:
    print("no match")

match = re.search('term1', text)
print("match",match.start()) # match 22 -> finds the match at line 22

split_term = '@'
email = 'user@gmail.com'

print(re.split(split_term, email))

# sample of regular expressions

def multi_re_find(patterns, phrase):

  for pat in patterns:
    print(f'Searching for pattern {pat}')
    print(re.findall(pat,phrase))
    print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sdddd'
test_phrase2 = 'This is a string! But it has punctuation. How can we remove it?'
test_phrase3 = 'This is a string with numbers 12312 and a symbol #hashtag'


test_patterns = ['sd*']
test_patterns2 = ['sd+'] #looks for s followed by one or more ds
test_patterns3 = ['sd{3}']
test_patterns4 = ['sd{1,3}'] #one or 3 ds
test_patterns5 = ['sd[sd]+'] #s followed by either s (one or more) or d (one or more)

test_patterns6 = ['[^!.?]+'] # to exclude anything after ^
test_patterns7 = ['[a-z]+'] # look for a sequence of lower case characters
test_patterns8 = ['[A-Z]+'] # look for a sequence of upper case characters
test_patterns9 = [r'\d+'] # excape character -> will return a sequence of all digits in phrase
test_patterns10 = [r'\s+'] # a list of all white spaces
test_patterns11 = [r'\w+'] # will return a list of all alpha numeric characters: letters and numbers
test_patterns12 = [r'\D+'] # will return all the non digit characters
test_patterns13 = [r'\S+'] # will return a list of all non white space characters
test_patterns14 = [r'\W+'] # will return all the non alpha numeric characters

multi_re_find(test_patterns,test_phrase) #['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 'sdddd']
multi_re_find(test_patterns2,test_phrase) #['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sdddd']
multi_re_find(test_patterns3,test_phrase) #['sddd', 'sddd', 'sddd', 'sddd']
multi_re_find(test_patterns4,test_phrase) #['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']
multi_re_find(test_patterns5,test_phrase) #['sdsd', 'sddd', 'sdddsddd', 'sds', 'sdddd']
multi_re_find(test_patterns6,test_phrase2) #['This is a string', ' But it has punctuation', ' How can we remove it']
multi_re_find(test_patterns7,test_phrase2) #['his', 'is', 'a', 'string', 'ut', 'it', 'has', 'punctuation', 'ow', 'can', 'we', 'remove', 'it']
multi_re_find(test_patterns8,test_phrase2) #['T', 'B', 'H']
multi_re_find(test_patterns9,test_phrase3) #['12312']