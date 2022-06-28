from ctypes import *
import struct
import random
libc = CDLL("libc.so.6")
#linux srand/ rand
def srand(seed):
	return libc.srand(seed)
def rand():
	return libc.rand()

p32 = lambda x:struct.pack("<I", x)
up32 = lambda x:struct.unpack("<I",x)[0]

def ROL(data, shift, size=32):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)
    
def ROR(data, shift, size=32):
    shift %= size
    body = data >> shift
    remains = (data << (size - shift)) - (body << size)
    return (body + remains)

def setup(k):
	P = 0xb7e15163
	Q = 0x9e3779b9
	L = k[:]
	S = [0 for i in range(44)]
	S[0] = P
	for i in range(1, len(S)):
		S[i] = (S[i - 1] + Q) & 0xFFFFFFFF

	A = B = i = j = 0
	for _ in range(3 * len(S)):
		A = S[i] = ROL( (S[i] + (A + B)) & 0xFFFFFFFF , 3)
		B = L[j] = ROL((L[j] + (A + B)) & 0xFFFFFFFF, (A + B) & 0xFF)
		i = (i+1) % len(S)
		j = (j+1) % len(L)
	return S

def encrypt(S, pt):
	A = pt[0]
	B = pt[1]
	C = pt[2]
	D = pt[3]
	modulo = 2**32
	lgw = 5
	r = 20
	B = (B + S[0])%modulo
	D = (D + S[1])%modulo 
	for i in range(1, r+1):
		t_temp = (B*(2*B + 1))%modulo 
		t = ROL(t_temp,lgw,32)
		u_temp = (D*(2*D + 1))%modulo
		u = ROL(u_temp,lgw,32)
		tmod=t%32
		umod=u%32
		A = (ROL(A^t,umod,32) + S[2*i])%modulo 
		C = (ROL(C^u,tmod,32) + S[2*i+ 1])%modulo
		(A, B, C, D)  =  (B, C, D, A)
	A = (A + S[2*r + 2])%modulo 
	C = (C + S[2*r + 3])%modulo
	cipher = []
	cipher.append(A)
	cipher.append(B)
	cipher.append(C)
	cipher.append(D)
	return cipher

def __umodti3(x, mod):
	v = (x % mod)
	return v

def generate_random(known,R_0x10, R4_0xC):
	mod = 0x462E17E9D5AB3B00A46ADBFF9D35F73D
	v15 = 0
	while True:
		if (R_0x10 & 1):
			calc_val = (known + v15)
			if((calc_val) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF != calc_val):
				calc_val = (calc_val & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) +  1
			v15 =  __umodti3(calc_val, mod)
		known = __umodti3((known << 1) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, mod)
		R_0x10 = R_0x10 >> 1
		if(R_0x10 == 0):
			break
	val = __umodti3(R4_0xC + v15, mod)
	print(hex(val))
	return val, list((val).to_bytes(16, byteorder='little'))


known = 0x0FAD829AF8E325D772B596A26B714129
unk_R_0x10 = 0x19C6E97BE1F03883002E9D9A771BFCD3
unk_R4_0xC = 0x0F232C3FC4BB276A65B68D010

#custom-random-1 -> known value (파일 0x10 바이트)
known, rand_bytes = generate_random(known, unk_R_0x10, unk_R4_0xC)
xor_key = bytes(rand_bytes)
xor_key = [up32(xor_key[i*4:i*4+4]) for i in range(4)]

#custom-random-2
known, rand_bytes = generate_random(known, unk_R_0x10, unk_R4_0xC)
key = bytes(rand_bytes)
key = [up32(key[i*4:i*4+4]) for i in range(4)]
S = setup(key)


pt = b'B'*0x10
pt += b"A" * 0x10
print(pt)

blocks = []
for i in range(len(pt)//16):
	block = pt[i*16:i*16+16]
	enc = []
	for j in range(4):
		enc.append(up32(block[i*4:i*4+4]))
	blocks.append(enc)


for i in range(0, len(blocks)):
	block = blocks[i]
	for j in range(0, len(block)):
		block[j] ^= xor_key[j]
	cipher = encrypt(S, block)
	blocks[i] = cipher[:]
	xor_key = cipher[:]

cipher_bytes = []
for i in range(0, len(blocks)):
	for j in range(0,len(blocks[i])):
		cipher_bytes +=  list(p32(blocks[i][j])) 

#custom-random-3
known, rand_bytes = generate_random(known, unk_R_0x10, unk_R4_0xC)
seed = known & 0xFFFFFFFF
swap_table = [i for i in range(0x100)]
srand(seed)
if(rand() & 0xFF):
	c = 0
	while True:
		x = rand() & 0xFF
		y = rand() & 0xFF
		swap_table[x], swap_table[y] = swap_table[y], swap_table[x]
		c += 1
		if(c >= (rand() & 0xFF)):
			break

#custom-random-4
known, rand_bytes = generate_random(known, unk_R_0x10, unk_R4_0xC)
randfk = bytes(rand_bytes)
assert(len(randfk) == 16)

v50 = 0
for idx in range(0, 256, 2):
	v51 = swap_table[idx]
	v52 = (v51 + v50 + randfk[idx & 14]) & 0xFF
	swap_table[idx], swap_table[v52] = swap_table[v52], swap_table[idx]
	v53 = swap_table[idx + 1]
	v50 = (v52 + v53 + randfk[(idx + 1) & 15]) & 0xFF
	swap_table[idx + 1], swap_table[v50] = swap_table[v50], swap_table[idx + 1]

v56 = 0
for idx in range(0, len(cipher_bytes)):
	v57 = swap_table[idx + 1]
	v56 = (v56 + v57) & 0xFF
	swap_table[(idx + 1)] = swap_table[v56];
	swap_table[v56] = v57;


	lid = swap_table[(v56 + swap_table[(idx + 1)]) & 0xFF]
	lid += swap_table[(swap_table[(idx + 1)] + v57) & 0xFF]
	lid += swap_table[((swap_table[ ((v56 >> 3) | (32 * (idx + 1))) & 0xFF] + swap_table[(((idx+ 1) >> 3) | (32 * v56)) & 0xFF]) & 0xFF) ^ 0xAA]
	cipher_bytes[idx] ^= lid
	cipher_bytes[idx] &= 0xFF

print(list(map(hex,cipher_bytes)))
	


# generate_random 값 유추 하는 방법을 몰라서 못 풀었음 ㅜ
# 풀이: https://gist.github.com/G0RiyA/8dbe9537350a9a11b75ab22c1a3cdfbc
