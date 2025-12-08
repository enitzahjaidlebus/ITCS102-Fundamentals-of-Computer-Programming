#Dictionary 
programming_language = ["Java", "C#", "C++", "Python", "Perl", "Go lang", "Javascript"]
print(programming_language[-1])#-1 is last 

#{keys : value, keys : value}
rogramming_language = {"medyo mahirap":"Java","ok lang":"C#", "sobrang hirap":"C++", "ok lang":"Python", "pang matanda":"Perl", "bago lang":"Go lang", "mahirap":"Javascript"}
print(rogramming_language["ok lang"])

#adding item to a dictionary 
rogramming_language['pang beginer'] = 'html'
print(rogramming_language)

#rogramming_language.pop('keys')
rogramming_language.pop('medyo mahirap')
print(rogramming_language)