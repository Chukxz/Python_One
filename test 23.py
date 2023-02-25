import re

# pattern = r"spam"

# if re.match(pattern, "spamspamspam"):
#     print("Match")
# else:
#     print("No match")

# if re.match(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")

# if re.search(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")

# print(re.findall(pattern,"eggspamsausagespam"))
# print(len(re.findall(pattern,"eggspamsausagespam")))

# match = re.search(pattern, "eggspamsausagespam")
# if match:
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print(match.span())


# str = "My name is David. Hi David"
# pattern = r"David"
# newstr = re.sub(pattern, "Amy", str, 1)
# print(newstr)

# pattern=r"David"
# newstr=re.sub(pattern,"Jackson",str, 1)
# print(newstr)

# str = "My name is Amy. Hi Amy"
# pattern = r"Amy"
# newstr = re.sub(pattern, "Jackson", str,1)
# print(newstr)


# Metacharacters:
#. ^ $ * + ? { } [ ] \ | ( ) 

# well_pattern = r"gr.y"
# if re.match(well_pattern,"grey"):
#     print("Match 1")

# if re.match(well_pattern,"gray"):
#     print("Match 2")

# if re.match(well_pattern,"blue"):
#     print("Match 3")

# well_pattern = r"^gr.y$"
# if re.match(well_pattern,"grey"):
#     print("Matches 1")

# if re.match(well_pattern,"gray"):
#     print("Matches 2")

# if re.match(well_pattern,"stingray"):
#     print("Matches 3")

# well_pattern = r"[aeiou]"
# if re.search(well_pattern,"grey"):
#     print("Matched 1")

# if re.search(well_pattern,"qwertyuiop"):
#     print("Matched 2")

# if re.search(well_pattern,"rhythm myths"):
#     print("Matched 3")

# well_patterns = r"gr.y"
# if re.search(well_patterns,"grey"):
#     print("Matching 1")

# if re.search(well_patterns,"gray"):
#     print("Matching 2")

# if re.search(well_patterns,"griy"):
#     print("Matching 3")

# well_pattern = r"[ae]"
# if re.search(well_pattern,"grey"):
#     print("Will match 1")

# if re.search(well_pattern,"gray"):
#     print("Will match 2")

# if re.search(well_pattern,"griy"):
#     print("Will match 3")

#pattern = r"[A-Z][A-Z][0-9]"

# if re.search(pattern,"LS8"):
#     print("Match 1")

# if re.search(pattern, "E3"):
#     print("Match 2")

# if re.search(pattern,"1ab"):
#     print("Match 3")

# search1 = re.search(pattern, "LS8")
# if search1:
#     print("Match 1", search1.group())

# search2 = re.search(pattern, "E2")
# if search2:
#     print("Match 2", search2.group())

# search3 = re.search(pattern, "AC130")
# if search3:
#     print("Match 3", search3.group())

#not that other characters apart from '^' have no meaning within character classes ' [] '. Also '^' only has a meaning(to invert) if it it is the first character in the class.

# pattern = r"[^A-Z]"

# if re.search(pattern, "this is all quiet"):
#     print("Match 1")

# if re.search(pattern, "AbCdEfG123"):
#     print("Match 2")

# if re.search(pattern, "THISISALLSHOUTING"):
#     print("Match 3")

# pattern = r"egg(spam)*"

# if re.match(pattern, "egg"):
#     print("Match 1")

# if re.match(pattern,"eggspamspamegg"):
#     print("Match 2")

# if re.match(pattern, "spam"):
#     print("Match 3")


# pattern = r"g+"

# if re.match(pattern, "g"):
#     print("Match 1")

# if re.match(pattern, "gggggggg"):
#     print("Match 2")

# if re.match(pattern, "abc"):
#     print("Match 3")

# pattern = r"ice(-)?cream"

# if re.match(pattern, "ice-cream"):
#     print("Match 1")

# if re.match(pattern, "icecream"):
#     print("Match 2")

# if re.match(pattern, "sausages"):
#     print("Match 3")

# if re.match(pattern, "ice--ice"):
#     print("Match 4")

# pattern = r"9{1,3}$"

# if re.match(pattern,"9"):
#     print("Match 1")

# if re.match(pattern, "999"):
#     print("Match 2")

# if re.match(pattern, "9999"):
#     print("Match 3")

# pattern = r"a(bc)(de)(f(g)h)i"

# match = re.match(pattern,"abcdefghijklmnop")

# if match:
#     print(match.group())
#     print(match.group(1))
#     print(match.group(2))
#     print(match.groups())

# pattern = r"(?P<first>abc)(?:def)(ghi)"

# match = re.match(pattern, "abcdefghi")
# if match:
#     print(match.group("first"))
#     print(match.groups())

# pattern = r"(a)(b(?:c)(d)(?:e))"

# match = re.match(pattern, "abcde")
# if match:
#     print(len(match.groups()))

# pattern = r"(a)(b(c)(d)(e))"

# match = re.match(pattern, "abcde")
# if match:
#     print(len(match.groups()))

# pattern = r"gr(a|e)y"

# match = re.match(pattern, "gray")
# if match:
#     print("Match 1")

# match = re.match(pattern, "grey")
# if match:
#     print("Match 2")

# match = re.match(pattern, "griy")
# if match:
#     print("Match 3")


# pattern = r"(.+) \1"

# match = re.match(pattern, "word word")
# if match:
#     print("Match 1")

# match = re.match(pattern, "?! ?!")
# if match:
#     print("Match 2")

# match = re.match(pattern, "abc cde")
# if match:
#     print("Match 3")    

# pattern = r"(\D+\d)"

# match = re.match(pattern, "Hi 999!")
# if match:
#     print("Match 1")

# match = re.match(pattern, "1,23, 456!")
# if match:
#     print("Match 2")

# match = re.match(pattern, " ! $?")
# if match:
#     print("Match 3")

# pattern = r"\b(cat)\b"
# match = re.match(pattern, "The cat sat")  
# if match:
#     print("Match 1")

# match=re.match(pattern, "We s>cattered?")
# if match:
#     print("Match 2")

# match = re.match(pattern, "We scattered.")
# if match:
#     print("Match 3")



#valid email verifier
str = "Please contact info@sololearn.com for assistance at info@google.com and gov.ng@co.uk.com or"

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

matching=re.search(pattern,str)
match = re.findall(pattern, str)# findall is used in the case of more than one emails.dfs

if matching and match:
    print(match)#in the case of more than one emails
    print(matching.group())


#valid phone number verifier 
number=(input())

pattern = r"(^[1,8,9][\d]{7,7}$)"

matches = re.search(pattern, number)
matched = re.findall(pattern, number)

if matches and matched:
    print(matches.group())
    print(matched)
    print("Valid")

else: print("Invalid")