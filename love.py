f = open('high.txt', 'r')
x = open('newhigh.txt', 'a')

for line in f :
    z = line[0:-8] + ",\n"
    x.write(z)

x.close()
