import os

print(os.path.join('usr', 'bin', 'spam'))

myFile = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFile:
    print(os.path.join('.\\', filename))
    