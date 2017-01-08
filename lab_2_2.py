import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
k = ' la'
for i in range(0,x-1):
	k = k + '-la '
k = k * y
if z == 1:
	k = 'Everybody sing a song:' + k[:-1] +'!'
else:
	k = 'Everybody sing a song:' + k[:-1] + '.'
print k



