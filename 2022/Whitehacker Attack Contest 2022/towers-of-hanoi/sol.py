from pwn import *

r = remote("175.123.252.156", 9999)
for level in range(1,4):
    print(r.recvuntil("# Level %d: " % level))
    prob = r.recvuntil("\n")[:-1]
    print("prob", prob)

    p1, p2, p3 = map(lambda x: list(map(int, x)) if len(x) else [] , prob.split(","))
    sol = ""
    sol += "BA" * len(p2)
    for i in range(len(p2)):
        p1.insert(0, p2.pop(0))
    sol += "CA" * len(p3)
    for i in range(len(p3)):
        p1.insert(0, p3.pop(0))
    print(p1,p2,p3)
    fdisc = [3,5,9][level - 1]
    if(level == 3):
        skip = int(input(">"))
    else:
        skip = 0
    while fdisc != 0:
        if(fdisc == skip):
            fdisc -= 1

        if(p1[0] == fdisc):
            sol += "AC"
            p3.insert(0, p1.pop(0))
            sol += "BA" * len(p2)
            for i in range(len(p2)):
                p1.insert(0, p2.pop(0))
            fdisc -= 1
            print(fdisc, p1,p2,p3)
        else:
            sol += "AB"
            p2.insert(0, p1.pop(0))
    print(sol)
    print(p1, p2, p3)
    r.sendline(sol)
else:
    r.interactive()
