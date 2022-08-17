def InsertL(c,e,n): 
	a=convert(c)
	a=31*len(c)*a
	a=a%n
	while d[a] != None:
		a=ColisaoL(a)
	d[a]=(e, c)
	
def BuscaL(e,c,n):
	a=convert(e)
	a=31*len(e)*a
	a=a%n
	return d[a]
def ColisaoL(a):
	if(a>n):
		a=0
	a=a+1
	return a
	
def ReHashL(d,q):
	d=[None]*q
	return d
	
def convert(v):
    x = 0
    for c in v:
        x *= 256
        x += ord(c)
    return x
fcarga=0.7
n=10
ocupa=1
d=[None]*n
a=open("entrada.txt","r") #le o arquivo
r=a.readlines() 
for i in range(len(r)):
	r[i]=r[i].rstrip()
i=0
while i<((len(r))):
	InsertL(r[i],r[i+1],n)
	ocupa=ocupa+1
	i=i+2
	if ocupa>n*fcarga:
		n=n*2
		d=ReHashL(d,n)
		ocupa=0
		i=0
print d
