import os

def dec(x, data):
    res = b''
    ebx = x
    for i in range(len(data)):
        edx = ((ebx >> 0xf) ^ (ebx >> 0xa) ^ (ebx >> 0x8) ^ (ebx >> 0x3)) & 1
        ebx = (ebx << 1 | edx)  &0xFFFFFFFF
        res += bytes([enc[i] ^ (ebx & 0xFF)])
    return res

with open("flag.lzma.enc", "rb") as f:
    enc = f.read()

lzma_sig = b"\x5d\x00\x00\x80\x00"
for ebx in range(0,100000):
    if(dec(ebx, enc[:5])  == lzma_sig):
        fname = "flag-%d.lzma" % ebx
        with open(fname, "wb") as f:
            f.write(dec(ebx, enc))
        os.system("7z x %s" % fname)
            
