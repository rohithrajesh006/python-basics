import re #regular expression

p="H"#strings

a=re.match(p,"Hello")#match-used for checking a pattern at the begining
print(a)

b=re.match(p,"WelcomeH")
print(b)


b=re.search(p,"WelHcomH")#search-used for checking a pattern at any place(only first)
print(b)

e=re.findall(p,"HH9eelloH12")#findall-used for checking a pattern at any place(shows how may times it is present)
print(e)

K=r"[a-zA-Z0-9 @]"
f=re.sub(K,"!","abkaSGAgd123@")#sub- here replace the string with !
print(f)

R=r"\d"#for numbers

c=re.match(R,"1hii")
print(c)

d=re.search(R,"hiii1")
print(d)

#email validation check

email_pattern=r"[A-Za-z0-9]+@[a-z]+\.(com|in)"
email=input("Enter your email:")

check=re.match(email_pattern,email)
if check:
    print("Valid email")
else:
    print("Invalid email")