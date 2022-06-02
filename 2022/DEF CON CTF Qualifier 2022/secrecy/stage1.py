# 0xEA @gss1
from pwn import *

ticket = "ticket{SailAbeam5510n22:N2DhgOtA9LO4ktdltOdiHGOFl0xn3al_zuqx4fPg6nlyOojV}"
r = remote("secrecy-vd34kvensehem.shellweplayaga.me", 10000)
r.sendlineafter("please: ", ticket)

def input_fn(identify, code):
    r.sendlineafter("identity:\n", identify)
    r.sendlineafter("code:\n", code)
    return r.recvline()

# cipher + key
ans_code = [178, 41, 213, 230, 85, 58, 224, 25, 204, 8, 218, 26, 40, 12, 60, 101]

for i in range(2, 16):
    for l in range(0, 256):
        input_code = "00" * (16-i)
        input_code += format(l, '02x')
        for j in range(16-i+1,16):
            input_code += format(ans_code[j] ^ i, '02x')
        # print(input_code)
        output = input_fn("0xEA", input_code)
        print(output)
        if b"length" in output:
            ans_code[16-i] = i ^ l
            print(ans_code)
            break
