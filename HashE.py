#!/usr/bin/python
# -*- coding: utf-8 -*-
def InsertL(c,e,n): 
	a1=0
	a=convert(c)
	a=31*len(c)*a
	a=a%n
	a1=len(d[a])-1
	print a
	if d[a][0] != None:
		d[a]=ColisaoL(a,e,c)
	else:
		d[a]=(e,c)
		
def BuscaL(e,c,n):
	a=convert(e)
	a=31*len(e)*a
	a=a%n
	return d[a]
def ColisaoL(a,e,c):
	d[a]=(d[a],(e,c))
	return d[a]
def ReHashL(d,q):
	d=[None]*q
	return d
def convert(v):
    x = 0
    for c in v:
        x *= 256
        x += ord(c)
    return x
n=10
ocupa=1
d1=[]
d=[None]*n
d1=[None]*1
for i in range(n):
	d[i]=d1
a=open("entrada.txt","r") #le o arquivo
r=a.readlines()  #Colocar todo o conteudo do arquivo em 1 variavel
for i in range(len(r)): #Tirar o /N
	r[i]=r[i].rstrip()
i=0
while i<len(r):
	InsertL(r[i],r[i+1],n)
	ocupa=ocupa+1
	i=i+2
	if ocupa>n:
		n=n*2
		d=ReHashL(d,n)
		ocupa=0
		i=0
print d
