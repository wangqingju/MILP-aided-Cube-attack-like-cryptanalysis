from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',128),Block('v',960)],globals())


def theta(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(64):
			tempstate[i].append(state[i][j])
			for k in range(5):
				tempstate[i][j]+=state[(i%5+5-1)%5+5*k][j]+state[(i%5+1+5)%5+5*k][(j-1+64)%64]

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]



def rio(state):
	rot=[0,1,62,28,27,36,44,6,55,20,3,10,43,25,39,41,45,15,21,8,18,2,61,56,14]
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(64):
			tempstate[i].append(state[i][(j-rot[i]+64)%64])

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

def pi(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		y=floor(i/5)
		x=i%5
		x1=y
		y1=(2*x+3*y)%5
		temp=5*y1+x1
		for j in range(64):
			tempstate[temp].append(state[i][j])
	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

def chi(state):
	tempstate=[[] for i in range(25)]
	for i in range(5):
		for j in range(5):
			for k in range(64):
				tempstate[5*i+j].append(state[5*i+j][k]+(state[5*i+(j+1)%5][k]+1)*state[5*i+(j+2)%5][k])

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

state=[[] for i in range(25)]
for i in range(25):
	for j in range(64):
		state[i].append(Keccak(0))


state[0][11]=Keccak(k(0))
state[0][12]=Keccak(k(1))
state[0][23]=Keccak(k(2))
state[0][24]=Keccak(k(3))
state[0][35]=Keccak(k(4))
state[0][36]=Keccak(k(5))
state[0][47]=Keccak(k(6))
state[0][48]=Keccak(k(7))
state[0][60]=Keccak(k(8))
state[0][63]=Keccak(k(9))
state[1][8]=Keccak(k(10))
state[1][9]=Keccak(k(11))
state[1][10]=Keccak(k(12))
state[1][11]=Keccak(k(13))
state[1][12]=Keccak(k(14))
state[1][20]=Keccak(k(15))
state[1][21]=Keccak(k(16))
state[1][22]=Keccak(k(17))
state[1][23]=Keccak(k(18))
state[1][24]=Keccak(k(19))
state[1][33]=Keccak(k(20))
state[1][34]=Keccak(k(21))
state[1][35]=Keccak(k(22))
state[1][36]=Keccak(k(23))
state[1][37]=Keccak(k(24))
state[1][47]=Keccak(k(25))
state[1][48]=Keccak(k(26))
state[1][49]=Keccak(k(27))
state[1][50]=Keccak(k(28))
state[1][60]=Keccak(k(29))
state[1][61]=Keccak(k(30))
state[1][62]=Keccak(k(31))
state[1][63]=Keccak(k(32))




state[2][1]=Keccak(v(0))
state[7][1]=Keccak(v(0))
state[2][2]=Keccak(v(1))
state[7][2]=Keccak(v(1))
state[2][8]=Keccak(v(2))
state[7][8]=Keccak(v(2))
state[2][9]=Keccak(v(3))
state[7][9]=Keccak(v(3))
state[2][10]=Keccak(v(4))
state[7][10]=Keccak(v(4))
state[2][11]=Keccak(v(5))
state[7][11]=Keccak(v(5))
state[2][12]=Keccak(v(6))
state[7][12]=Keccak(v(6))
state[2][13]=Keccak(v(7))
state[7][13]=Keccak(v(7))
state[2][14]=Keccak(v(8))
state[7][14]=Keccak(v(8))
state[2][20]=Keccak(v(9))
state[7][20]=Keccak(v(9))
state[2][21]=Keccak(v(10))
state[7][21]=Keccak(v(10))
state[2][22]=Keccak(v(11))
state[7][22]=Keccak(v(11))
state[2][23]=Keccak(v(12))
state[7][23]=Keccak(v(12))
state[2][24]=Keccak(v(13))
state[7][24]=Keccak(v(13))
state[2][25]=Keccak(v(14))
state[7][25]=Keccak(v(14))
state[2][26]=Keccak(v(15))
state[7][26]=Keccak(v(15))
state[2][33]=Keccak(v(16))
state[7][33]=Keccak(v(16))
state[2][34]=Keccak(v(17))
state[7][34]=Keccak(v(17))
state[2][35]=Keccak(v(18))
state[7][35]=Keccak(v(18))
state[2][36]=Keccak(v(19))
state[7][36]=Keccak(v(19))
state[2][37]=Keccak(v(20))
state[7][37]=Keccak(v(20))
state[2][38]=Keccak(v(21))
state[7][38]=Keccak(v(21))
state[2][41]=Keccak(v(22))
state[7][41]=Keccak(v(22))
state[2][46]=Keccak(v(23))
state[7][46]=Keccak(v(23))
state[2][47]=Keccak(v(24))
state[7][47]=Keccak(v(24))
state[2][48]=Keccak(v(25))
state[7][48]=Keccak(v(25))
state[2][49]=Keccak(v(26))
state[7][49]=Keccak(v(26))
state[2][50]=Keccak(v(27))
state[7][50]=Keccak(v(27))
state[2][53]=Keccak(v(28))
state[7][53]=Keccak(v(28))
state[2][54]=Keccak(v(29))
state[7][54]=Keccak(v(29))
state[2][59]=Keccak(v(30))
state[7][59]=Keccak(v(30))
state[2][60]=Keccak(v(31))
state[7][60]=Keccak(v(31))
state[2][61]=Keccak(v(32))
state[7][61]=Keccak(v(32))
state[2][62]=Keccak(v(33))
state[7][62]=Keccak(v(33))
state[2][63]=Keccak(v(34))
state[7][63]=Keccak(v(34))
state[3][0]=Keccak(v(35))
state[8][0]=Keccak(v(35))
state[3][1]=Keccak(v(36))
state[8][1]=Keccak(v(36))
state[3][7]=Keccak(v(37))
state[8][7]=Keccak(v(37))
state[3][10]=Keccak(v(38))
state[8][10]=Keccak(v(38))
state[3][11]=Keccak(v(39))
state[8][11]=Keccak(v(39))
state[3][12]=Keccak(v(40))
state[8][12]=Keccak(v(40))
state[3][13]=Keccak(v(41))
state[8][13]=Keccak(v(41))
state[3][14]=Keccak(v(42))
state[8][14]=Keccak(v(42))
state[3][22]=Keccak(v(43))
state[8][22]=Keccak(v(43))
state[3][23]=Keccak(v(44))
state[8][23]=Keccak(v(44))
state[3][24]=Keccak(v(45))
state[8][24]=Keccak(v(45))
state[3][25]=Keccak(v(46))
state[8][25]=Keccak(v(46))
state[3][26]=Keccak(v(47))
state[8][26]=Keccak(v(47))
state[3][34]=Keccak(v(48))
state[8][34]=Keccak(v(48))
state[3][35]=Keccak(v(49))
state[8][35]=Keccak(v(49))
state[3][36]=Keccak(v(50))
state[8][36]=Keccak(v(50))
state[3][37]=Keccak(v(51))
state[8][37]=Keccak(v(51))
state[3][38]=Keccak(v(52))
state[8][38]=Keccak(v(52))
state[3][39]=Keccak(v(53))
state[8][39]=Keccak(v(53))
state[3][46]=Keccak(v(54))
state[8][46]=Keccak(v(54))
state[3][47]=Keccak(v(55))
state[8][47]=Keccak(v(55))
state[3][49]=Keccak(v(56))
state[8][49]=Keccak(v(56))
state[3][50]=Keccak(v(57))
state[8][50]=Keccak(v(57))
state[3][51]=Keccak(v(58))
state[8][51]=Keccak(v(58))
state[3][52]=Keccak(v(59))
state[8][52]=Keccak(v(59))
state[3][58]=Keccak(v(60))
state[8][58]=Keccak(v(60))
state[3][59]=Keccak(v(61))
state[8][59]=Keccak(v(61))
state[3][62]=Keccak(v(62))
state[8][62]=Keccak(v(62))
state[3][63]=Keccak(v(63))
state[8][63]=Keccak(v(63))


theta(state)
rio(state)
pi(state)
chi(state)

n=0
for i in range(33):
	for j in range(64):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)











