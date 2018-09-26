# here i import the module that implements regular expressions
import re
# here is my function to check for valid email address
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    # here is an example list of email to check it at the end
    emails = ["john@example.com", "python-list@python.org", "@wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

# my pattern that is passed as argument in my function is here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"   
# here i test my function passing my pattern
test_email(pattern)

pattern = r"\"?([a-zA-Z] || .[a-zA-Z])\"?"
pattern_1 = re.compile(pattern)
string = str(input('Enter the string for name '))
result = bool (re.match(pattern_1,string))
if re.match(pattern_1,string):
    print('matched')
else:
    print('unMatched')

print('result ',result)

