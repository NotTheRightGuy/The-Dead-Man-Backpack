import sys
temp = sys.stdout
sys.stdout = open('log.txt','w')
print('Testing 123')
print('Another Line')
sys.stdout.close()
sys.stdout  = temp
print('Back to normal')
