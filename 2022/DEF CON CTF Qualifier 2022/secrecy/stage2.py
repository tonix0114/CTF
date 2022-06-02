import struct
import binascii
up16 = lambda x : struct.unpack("<H", x)[0]

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

KEY_OFFSET = 0x48
value = ''

xor_len = 0
cur = 0
inst_count = 0

ctx = b'\x00' * KEY_OFFSET # stack
ctx += b'\xe8$\xbe\x95\xf8>l\x1b\xa4;}3\xc6\n\x8b\xcc\xc6\xa8@7X\x0b\xc2v\xbd\xdc\x82\xe2U\xf4\xff\xcf' # key
ctx += b'\x00' * 0x8 # dummy
ctx = list(ctx)
ctx_identity = b'0xEA' + b'\x00' * 12
ctx_decrypt = b']\xee\x17\x8b\x87+l\x87K\xaf\xb1:\xe9\xef'

def get_code(cost):
	global code, inst_count, value
	try:
		inst_count += cost
		v = code.pop(0)
		fmt = "{0:0%db}" % cost
		value += str(fmt.format(v))
		return v
	except:
		print("empty"); exit()

def op_xor_ctx(length):
	global cur, xor_len
	v4 = cur - xor_len
	for i in range(length):
		ctx[v4 + i + KEY_OFFSET] ^= ctx_identity[i]
	xor_len += length + 1

def op_set_cur(offset):
	global cur
	if(offset >= 8):
		offset = -(16 - offset)
	cur = cur + offset

def op_array_rol(shift, length):
	global cur, ctx
	shift = shift + 1
	length = length + 1
	start = cur + KEY_OFFSET
	end = start + length
	val = ROL(int.from_bytes(bytes(ctx[start:end]), "big"), shift, length*8)
	ctx = ctx[:start] + list((val).to_bytes(length, byteorder='big')) + ctx[end:]

# stack[cur] += (x+1)
def op_add(x):
	global cur
	ctx[cur + KEY_OFFSET] = (ctx[cur + KEY_OFFSET] + (x + 1)) & 0xFF

def op_and(x):
	global cur
	ctx[cur + KEY_OFFSET] &= x

# stack[cur] -= (x+1)
def op_sub(x):
	global cur
	ctx[cur + KEY_OFFSET] = (ctx[cur + KEY_OFFSET] + ((~x) & 0xFF)) & 0xFF

def op_not():
	global cur
	ctx[cur + KEY_OFFSET] = (~ctx[cur + KEY_OFFSET]) & 0xFF

OP_CHECK = 0
OP_XOR = 1
OP_SET_CUR = 2
OP_ARRAY_ROL = 3
OP_ADD = 4
OP_AND = 5
OP_SUB = 6
OP_NOT = 7

code = []
code += [OP_XOR, 0xF]
for i in range(3):
	code += [OP_AND, 0]
	code += [OP_SET_CUR, 1]
code += [OP_SET_CUR, 0xD]
code += [OP_ADD, 0x7]
code += [OP_ADD, 0x7]
code += [OP_ADD, 0x7]
code += [OP_ADD, 0x7]
code += [OP_ADD, 0x4]
for i in range(1):
	code += [OP_SET_CUR, 1]
	code += [OP_SET_CUR, 0xF]
code += [OP_SET_CUR, 1]
code += [OP_CHECK]

while True:
	if(not code):
		break
	op = get_code(3)
	if(op == 0):
		if(xor_len == 16 and inst_count > 103):
                    print(inst_count, sum(ctx[KEY_OFFSET:KEY_OFFSET+32]) & 0x1FF)
                    if(sum(ctx[KEY_OFFSET:KEY_OFFSET+32]) & 0x1FF == 0):
                        print("success", sum(ctx[KEY_OFFSET:KEY_OFFSET+32]) & 0x1FF) # verification success
	elif(op == 1):
		length = get_code(4)
		op_xor_ctx(length)
	elif(op == 2):
		offset = get_code(4)
		op_set_cur(offset)
	elif(op == 3):
		shift = get_code(3)
		length = get_code(4)
		op_array_rol(shift, length)
	elif(op == 4):
		op_add(get_code(3))
	elif(op == 5):
		op_and(get_code(4))
	elif(op == 6):
		op_sub(get_code(3))
	elif(op == 7):
		op_not()

#stage1
ans_code = [178, 41, 213, 230, 85, 58, 224, 25, 204, 8, 218, 26, 40, 12, 60, 101]
stage2 = int('0b' + value.ljust(14*8, '0'), 2)
#sum(decrypt_message[:15]) & 0xFF
stage2 = stage2 << 8 | 0xD1
#padding check
stage2 = stage2 << 8 | 1
print(hex(stage2))

flag = list(binascii.unhexlify('%x' % stage2))
assert(len(flag) == len(ans_code))
for i in range(0, len(ans_code)):
    flag[i] ^= ans_code[i]
print("flag:", ''.join(list(map(lambda x: hex(x)[2:], flag))))
