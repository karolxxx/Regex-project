import re
import time


print('Welcome, you have won 1 million dollars! Please verify your phone number!')
time.sleep(2) #sleep
content = input('Please enter your number:')
# content = "111-111-1111"
numberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = numberRegex.search(content)
if result is not None:
    time.sleep(3) #sleep
    if result.group() == content:
        print('thank you')

    if result.group() != content:
        print('try again')
else:
    print('try again')
