import os

print(os.path.getsize('.\\github-recovery-codes.txt'))
print(os.listdir('.'))

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32\\', filename))
print(totalSize)
