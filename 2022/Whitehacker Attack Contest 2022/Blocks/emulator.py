import struct

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

flag = b"0000111122223333"
flag += (b"*"* 16) * 15
flag = list(flag)
data = [0 for i in range(0x1000)] + list(open("blocks/data", "rb").read())
data += [0 for i in range(0x2000 - len(data))]
reg = [0 for i in range(10)]; reg[-1] = 1
block = list(open("blocks/740664bbc7d31ede7e9627d3e65a6fa04f3732788081bc77034e7c7c37b8267a", "rb").read())
inscount = 0
print_bak = print
print = lambda x:x

while True:
  inscount += 1
  op = block.pop(0)
  print("#" + hex(inscount))
  #print(hex(op), data[:20], list(map(hex,reg )))
  # instructions
  '''
  if(inscount >=0x1620):
    print=print_bak
  '''
  if(inscount == 0x8931):
    reg[1] = 0x37
    print(hex(reg[0]))
    print(hex(reg[1]))
    print(hex(reg[2]))
    print(hex(reg[3]))
    print=print_bak
  if(inscount == 0x8944):
    reg[1] = 0xDD

  if(op <= 16):
    arg1 = block.pop(0)
    if(op not in [13, 15, 16]):
      arg2 = block.pop(0)
    if(op in [4, 5, 6, 7, 8, 9, 10, 11, 12]):
      arg3 = block.pop(0)
  if(op == 0): # mov reg (byte)
    #print("reg[%d] = data[%d]" % (arg2, reg[arg1]))
    print("reg[%d] = 0x%x" % (arg2, data[reg[arg1]] & 0xFF))
    reg[arg2] = data[reg[arg1]] & 0xFF
  elif(op == 1): # mov reg (dword)
    #print("reg[%d] = (dword*)data[%d]" % (arg2, reg[arg1]))
    val = 0
    for i in range(3, -1, -1):
      val = val << 8
      val |= data[reg[arg1] + i]
    reg[arg2] = val & 0xFFFFFFFF
    print("reg[%d] = 0x%x" % (arg2, val & 0xFFFFFFFF))
  elif(op == 2): # mov data (byte)
    print("data[%d] = reg[%d]"%  (reg[arg1], arg2))
    data[reg[arg1]] = reg[arg2] & 0xFF
  elif(op == 3): # mov data (dword)

    print("data[%d] = (dword*)reg[%d]"% (reg[arg1], arg2))
    for i in range(3, -1, -1):
      data[reg[arg1] + i] = (reg[arg2] & (0xFF << i * 8)) >> (i * 8)
    '''
    if(reg[arg1] == 272):
      for i in range(16):
        print(list(map(hex , data[260+(i*16):260+(i*16)+16])))
      exit()
    '''
  elif(op == 4): # add reg
    print("reg[%d] = reg[%d] + reg[%d]" %(arg3, arg2, arg1))
    reg[arg3] = reg[arg2] + reg[arg1]
  elif(op == 5): # sub reg
    print("reg[%d] = reg[%d] - reg[%d]" % (arg3, arg1, arg2))
    reg[arg3] = reg[arg1] - reg[arg2]
  elif(op == 6): # and reg
    print("reg[%d] = reg[%d] & reg[%d]" %(arg3, arg2, arg1))
    reg[arg3] = reg[arg2] & reg[arg1]
  elif(op == 7): # or reg
    print("reg[%d] = reg[%d] | reg[%d]" %(arg3, arg2, arg1))
    reg[arg3] = reg[arg2] | reg[arg1]
  elif(op == 8): # xor reg
    print("reg[%d] = reg[%d] ^ reg[%d]" %(arg3, arg2, arg1))
    reg[arg3] = reg[arg2] ^ reg[arg1]
  elif(op == 9): # ror4 reg
    print("reg[%d] = ROR(reg[%d], reg[%d])" %(arg1, arg1, arg2))
    print("reg[%d] = reg[%d]" %(arg3, arg1))
    reg[arg1] = ROR(reg[arg1], reg[arg2])
    reg[arg3] = reg[arg1]
  elif(op == 10): # rol4 reg
    print("reg[%d] = ROL(reg[%d], reg[%d])" %(arg1, arg1, arg2))
    print("reg[%d] = reg[%d]" %(arg3, arg1))
    reg[arg1] = ROL(reg[arg1], reg[arg2])
    reg[arg3] = reg[arg1]
  elif(op == 11): # reg left shift
    print("reg[%d] = reg[%d] << reg[%d]" %(arg3, arg1, arg2))
    reg[arg3] = reg[arg1] << reg[arg2]
  elif(op == 12): # reg right shift
    print("reg[%d] = reg[%d] >> reg[%d]" %(arg3, arg1, arg2))
    reg[arg3] = reg[arg1] >> reg[arg2]
  elif(op == 13): # set reg dword
    val = up32(bytes(block[:4]))
    block = block[4:]
    reg[arg1] = val
    print("reg[%d] = 0x%x" % (arg1, val))
  elif(op == 14): # not reg
    reg[arg2] = ~reg[arg1] & 0xFFFFFFFF
    print("reg[%d] = ~reg[%d] & 0xFFFFFFFF" %(arg2, arg1))
  elif(op == 15): # return
    print(arg1, inscount)
    for i in range(16):
      print(list(map(hex , data[260+(i*16):260+(i*16)+16])))
    exit()
  elif(op == 16): # read
    reg[arg1] = flag.pop(0)
    print("reg[%d] = flag(%c)" % (arg1, reg[arg1]))
  else:
    #print("END = %d" % block[0])
    pass
  for i in range(10):
    reg[i] &= 0xFFFFFFFF

  end = block.pop(0)
  if(reg[end]):
    fname =''.join( map(chr,block[64:]))
  else:
    fname =''.join( map(chr,block[:64]))
  block = list(open("blocks/" + fname, "rb").read())
  '''
  for r in range(10):
    print("\t\treg[%d] = %x" % (r, reg[r]))
  '''
