from z3 import *

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

s = Solver()
reg = [BitVec("reg%d" % i, 64) for i in range(10)]
flag = [BitVec("flag%d" % i, 64) for i in range(4)]

for i in range(4):
    s.add(flag[i] == (flag[i] & 0xFFFFFFFF))

reg[0] = flag[0]
reg[1] = flag[1]
reg[2] = flag[2]
reg[3] = flag[3]



reg[6] &= 0xFFFFFFFF
#0x1621
reg[6] = 0xa1eaed32
reg[6] &= 0xFFFFFFFF
#0x1622
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1623
reg[6] = 0x1008
reg[6] &= 0xFFFFFFFF
#0x1624
reg[6] = 0x595695ed
reg[6] &= 0xFFFFFFFF
#0x1625
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1626
reg[6] = 0x1004
reg[6] &= 0xFFFFFFFF
#0x1627
reg[6] = 0x3f4586c3
reg[6] &= 0xFFFFFFFF
#0x1628
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1629
reg[6] = 0x1000
reg[6] &= 0xFFFFFFFF
#0x162a
reg[6] = 0x7b7594cd
reg[6] &= 0xFFFFFFFF
#0x162b
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x162c
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x162d
reg[4] = reg[6] + reg[3]
reg[4] &= 0xFFFFFFFF
#0x162e
reg[3] = reg[0] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x162f
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1630
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1631
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x1632
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1633
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1634
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1635
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1636
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1637
reg[4] = reg[0] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1638
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1639
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x163a
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x163b
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x163c
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x163d
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x163e
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x163f
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1640
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1641
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1642
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1643
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1644
reg[4] = reg[2] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1645
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1646
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1647
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1648
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1649
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x164a
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x164b
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x164c
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x164d
reg[4] = reg[6] + reg[1]
reg[4] &= 0xFFFFFFFF
#0x164e
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x164f
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1650
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1651
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1652
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1653
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1654
reg[6] = 0x101c
reg[6] &= 0xFFFFFFFF
#0x1655
reg[6] = 0xf6bc3406
reg[6] &= 0xFFFFFFFF
#0x1656
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1657
reg[6] = 0x1014
reg[6] &= 0xFFFFFFFF
#0x1658
reg[6] = 0x4454ee90
reg[6] &= 0xFFFFFFFF
#0x1659
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x165a
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x165b
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x165c
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x165d
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x165e
reg[6] = 0x1010
reg[6] &= 0xFFFFFFFF
#0x165f
reg[6] = 0xf07982ab
reg[6] &= 0xFFFFFFFF
#0x1660
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1661
reg[6] = 0x1018
reg[6] &= 0xFFFFFFFF
#0x1662
reg[6] = 0x58daabb6
reg[6] &= 0xFFFFFFFF
#0x1663
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1664
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1665
reg[4] = reg[6] + reg[1]
reg[4] &= 0xFFFFFFFF
#0x1666
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1667
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1668
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1669
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x166a
reg[2] = reg[1] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x166b
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x166c
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x166d
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x166e
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x166f
reg[1] = reg[4] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1670
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1671
reg[3] = reg[2] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1672
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1673
reg[1] = reg[2] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1674
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x1675
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1676
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1677
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1678
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1679
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x167a
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x167b
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x167c
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x167d
reg[1] = reg[4] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x167e
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x167f
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1680
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1681
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1682
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1683
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1684
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1685
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1686
reg[1] = reg[6] + reg[3]
reg[1] &= 0xFFFFFFFF
#0x1687
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1688
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1689
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x168a
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x168b
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x168c
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x168d
reg[6] = 0x102c
reg[6] &= 0xFFFFFFFF
#0x168e
reg[6] = 0xb83a3474
reg[6] &= 0xFFFFFFFF
#0x168f
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1690
reg[6] = 0x1024
reg[6] &= 0xFFFFFFFF
#0x1691
reg[6] = 0xaa10ea18
reg[6] &= 0xFFFFFFFF
#0x1692
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1693
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1694
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1695
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1696
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1697
reg[6] = 0x1020
reg[6] &= 0xFFFFFFFF
#0x1698
reg[6] = 0xede6b092
reg[6] &= 0xFFFFFFFF
#0x1699
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x169a
reg[6] = 0x1028
reg[6] &= 0xFFFFFFFF
#0x169b
reg[6] = 0x23574c10
reg[6] &= 0xFFFFFFFF
#0x169c
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x169d
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x169e
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x169f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x16a0
reg[1] = reg[6] + reg[4]
reg[1] &= 0xFFFFFFFF
#0x16a1
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x16a2
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16a3
reg[2] = reg[1] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x16a4
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x16a5
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16a6
reg[3] = reg[4] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x16a7
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16a8
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x16a9
reg[2] = reg[3] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x16aa
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x16ab
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16ac
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16ad
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16ae
reg[3] = reg[0] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x16af
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x16b0
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x16b1
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x16b2
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x16b3
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16b4
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x16b5
reg[0] = reg[1] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x16b6
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16b7
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16b8
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x16b9
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x16ba
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16bb
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x16bc
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x16bd
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x16be
reg[0] = reg[6] + reg[3]
reg[0] &= 0xFFFFFFFF
#0x16bf
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16c0
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x16c1
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x16c2
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16c3
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16c4
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16c5
reg[6] = 0x103c
reg[6] &= 0xFFFFFFFF
#0x16c6
reg[6] = 0x94b69db1
reg[6] &= 0xFFFFFFFF
#0x16c7
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16c8
reg[6] = 0x1034
reg[6] &= 0xFFFFFFFF
#0x16c9
reg[6] = 0x4f7e66f9
reg[6] &= 0xFFFFFFFF
#0x16ca
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16cb
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x16cc
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x16cd
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x16ce
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x16cf
reg[6] = 0x1030
reg[6] &= 0xFFFFFFFF
#0x16d0
reg[6] = 0xb2b2b64b
reg[6] &= 0xFFFFFFFF
#0x16d1
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16d2
reg[6] = 0x1038
reg[6] &= 0xFFFFFFFF
#0x16d3
reg[6] = 0x62a561dd
reg[6] &= 0xFFFFFFFF
#0x16d4
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16d5
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x16d6
reg[0] = reg[6] + reg[3]
reg[0] &= 0xFFFFFFFF
#0x16d7
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16d8
reg[2] = reg[1] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x16d9
reg[0] = reg[1] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x16da
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16db
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16dc
reg[3] = reg[2] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x16dd
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x16de
reg[1] = reg[0] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x16df
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x16e0
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16e1
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x16e2
reg[2] = reg[0] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x16e3
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16e4
reg[0] = reg[3] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x16e5
reg[4] = reg[3] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x16e6
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x16e7
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16e8
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16e9
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x16ea
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x16eb
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x16ec
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x16ed
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x16ee
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x16ef
reg[4] = reg[2] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x16f0
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16f1
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x16f2
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x16f3
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x16f4
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x16f5
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x16f6
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x16f7
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x16f8
reg[4] = reg[6] + reg[0]
reg[4] &= 0xFFFFFFFF
#0x16f9
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16fa
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x16fb
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x16fc
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16fd
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x16fe
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x16ff
reg[6] = 0x104c
reg[6] &= 0xFFFFFFFF
#0x1700
reg[6] = 0x1ef7e3d
reg[6] &= 0xFFFFFFFF
#0x1701
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1702
reg[6] = 0x1044
reg[6] &= 0xFFFFFFFF
#0x1703
reg[6] = 0x813b4a0
reg[6] &= 0xFFFFFFFF
#0x1704
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1705
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1706
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1707
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1708
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1709
reg[6] = 0x1040
reg[6] &= 0xFFFFFFFF
#0x170a
reg[6] = 0x73183e3e
reg[6] &= 0xFFFFFFFF
#0x170b
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x170c
reg[6] = 0x1048
reg[6] &= 0xFFFFFFFF
#0x170d
reg[6] = 0xaa70fab1
reg[6] &= 0xFFFFFFFF
#0x170e
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x170f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1710
reg[4] = reg[6] + reg[1]
reg[4] &= 0xFFFFFFFF
#0x1711
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1712
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1713
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1714
reg[3] = reg[4] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1715
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1716
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1717
reg[3] = reg[2] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1718
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1719
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x171a
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x171b
reg[4] = reg[3] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x171c
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x171d
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x171e
reg[1] = reg[0] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x171f
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1720
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1721
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1722
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1723
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1724
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1725
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1726
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1727
reg[2] = reg[0] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1728
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1729
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x172a
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x172b
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x172c
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x172d
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x172e
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x172f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1730
reg[2] = reg[6] + reg[3]
reg[2] &= 0xFFFFFFFF
#0x1731
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1732
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1733
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1734
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1735
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1736
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1737
reg[6] = 0x105c
reg[6] &= 0xFFFFFFFF
#0x1738
reg[6] = 0x6ef1e1c4
reg[6] &= 0xFFFFFFFF
#0x1739
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x173a
reg[6] = 0x1054
reg[6] &= 0xFFFFFFFF
#0x173b
reg[6] = 0x1eee137
reg[6] &= 0xFFFFFFFF
#0x173c
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x173d
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x173e
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x173f
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1740
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1741
reg[6] = 0x1050
reg[6] &= 0xFFFFFFFF
#0x1742
reg[6] = 0x5482f051
reg[6] &= 0xFFFFFFFF
#0x1743
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1744
reg[6] = 0x1058
reg[6] &= 0xFFFFFFFF
#0x1745
reg[6] = 0xa8afdd32
reg[6] &= 0xFFFFFFFF
#0x1746
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1747
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1748
reg[2] = reg[6] + reg[3]
reg[2] &= 0xFFFFFFFF
#0x1749
reg[3] = reg[0] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x174a
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x174b
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x174c
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x174d
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x174e
reg[3] = reg[2] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x174f
reg[2] = reg[4] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x1750
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1751
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1752
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1753
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1754
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1755
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1756
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1757
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1758
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1759
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x175a
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x175b
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x175c
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x175d
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x175e
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x175f
reg[1] = reg[2] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1760
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1761
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1762
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1763
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1764
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1765
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1766
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1767
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1768
reg[1] = reg[6] + reg[0]
reg[1] &= 0xFFFFFFFF
#0x1769
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x176a
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x176b
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x176c
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x176d
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x176e
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x176f
reg[6] = 0x106c
reg[6] &= 0xFFFFFFFF
#0x1770
reg[6] = 0x8182c73d
reg[6] &= 0xFFFFFFFF
#0x1771
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1772
reg[6] = 0x1064
reg[6] &= 0xFFFFFFFF
#0x1773
reg[6] = 0x95849892
reg[6] &= 0xFFFFFFFF
#0x1774
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1775
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1776
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1777
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1778
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1779
reg[6] = 0x1060
reg[6] &= 0xFFFFFFFF
#0x177a
reg[6] = 0x24be3102
reg[6] &= 0xFFFFFFFF
#0x177b
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x177c
reg[6] = 0x1068
reg[6] &= 0xFFFFFFFF
#0x177d
reg[6] = 0x95eb2bf4
reg[6] &= 0xFFFFFFFF
#0x177e
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x177f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1780
reg[1] = reg[6] + reg[0]
reg[1] &= 0xFFFFFFFF
#0x1781
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1782
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1783
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1784
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1785
reg[0] = reg[4] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1786
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x1787
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1788
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1789
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x178a
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x178b
reg[3] = reg[2] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x178c
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x178d
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x178e
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x178f
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1790
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1791
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1792
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1793
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1794
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1795
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1796
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1797
reg[2] = reg[3] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1798
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1799
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x179a
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x179b
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x179c
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x179d
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x179e
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x179f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x17a0
reg[2] = reg[6] + reg[1]
reg[2] &= 0xFFFFFFFF
#0x17a1
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17a2
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x17a3
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x17a4
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17a5
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17a6
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17a7
reg[6] = 0x107c
reg[6] &= 0xFFFFFFFF
#0x17a8
reg[6] = 0x7e447bcb
reg[6] &= 0xFFFFFFFF
#0x17a9
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17aa
reg[6] = 0x1074
reg[6] &= 0xFFFFFFFF
#0x17ab
reg[6] = 0x6b6373cc
reg[6] &= 0xFFFFFFFF
#0x17ac
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x17ad
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x17ae
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x17af
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x17b0
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x17b1
reg[6] = 0x1070
reg[6] &= 0xFFFFFFFF
#0x17b2
reg[6] = 0xf057cffa
reg[6] &= 0xFFFFFFFF
#0x17b3
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17b4
reg[6] = 0x1078
reg[6] &= 0xFFFFFFFF
#0x17b5
reg[6] = 0x80732aaa
reg[6] &= 0xFFFFFFFF
#0x17b6
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17b7
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x17b8
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x17b9
reg[2] = reg[6] + reg[1]
reg[2] &= 0xFFFFFFFF
#0x17ba
reg[3] = ~reg[3] & 0xFFFFFFFF
reg[3] &= 0xFFFFFFFF
#0x17bb
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x17bc
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x17bd
reg[4] = reg[2] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x17be
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17bf
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17c0
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17c1
reg[3] = reg[1] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x17c2
reg[0] = reg[3] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x17c3
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17c4
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17c5
reg[4] = reg[3] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x17c6
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17c7
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17c8
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17c9
reg[2] = reg[3] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x17ca
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17cb
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x17cc
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x17cd
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x17ce
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x17cf
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17d0
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x17d1
reg[1] = reg[2] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x17d2
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17d3
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17d4
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x17d5
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x17d6
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17d7
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x17d8
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x17d9
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x17da
reg[1] = reg[6] + reg[0]
reg[1] &= 0xFFFFFFFF
#0x17db
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17dc
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x17dd
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x17de
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17df
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17e0
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17e1
reg[6] = 0x108c
reg[6] &= 0xFFFFFFFF
#0x17e2
reg[6] = 0xe37c991a
reg[6] &= 0xFFFFFFFF
#0x17e3
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17e4
reg[6] = 0x1084
reg[6] &= 0xFFFFFFFF
#0x17e5
reg[6] = 0x6f8ff074
reg[6] &= 0xFFFFFFFF
#0x17e6
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17e7
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x17e8
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x17e9
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x17ea
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x17eb
reg[6] = 0x1080
reg[6] &= 0xFFFFFFFF
#0x17ec
reg[6] = 0x3c96412a
reg[6] &= 0xFFFFFFFF
#0x17ed
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17ee
reg[6] = 0x1088
reg[6] &= 0xFFFFFFFF
#0x17ef
reg[6] = 0xddad2c4b
reg[6] &= 0xFFFFFFFF
#0x17f0
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17f1
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x17f2
reg[1] = reg[6] + reg[3]
reg[1] &= 0xFFFFFFFF
#0x17f3
reg[3] = reg[2] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x17f4
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17f5
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x17f6
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x17f7
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x17f8
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x17f9
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x17fa
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x17fb
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17fc
reg[1] = reg[2] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x17fd
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x17fe
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x17ff
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1800
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1801
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1802
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1803
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1804
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1805
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1806
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1807
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1808
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1809
reg[1] = reg[4] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x180a
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x180b
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x180c
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x180d
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x180e
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x180f
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1810
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1811
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1812
reg[1] = reg[6] + reg[0]
reg[1] &= 0xFFFFFFFF
#0x1813
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1814
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1815
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1816
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1817
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1818
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1819
reg[6] = 0x109c
reg[6] &= 0xFFFFFFFF
#0x181a
reg[6] = 0x8d022275
reg[6] &= 0xFFFFFFFF
#0x181b
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x181c
reg[6] = 0x1094
reg[6] &= 0xFFFFFFFF
#0x181d
reg[6] = 0x347e7c79
reg[6] &= 0xFFFFFFFF
#0x181e
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x181f
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1820
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1821
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1822
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1823
reg[6] = 0x1090
reg[6] &= 0xFFFFFFFF
#0x1824
reg[6] = 0x26270080
reg[6] &= 0xFFFFFFFF
#0x1825
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1826
reg[6] = 0x1098
reg[6] &= 0xFFFFFFFF
#0x1827
reg[6] = 0xce5449c9
reg[6] &= 0xFFFFFFFF
#0x1828
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1829
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x182a
reg[1] = reg[6] + reg[0]
reg[1] &= 0xFFFFFFFF
#0x182b
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x182c
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x182d
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x182e
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x182f
reg[4] = reg[0] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1830
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1831
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1832
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1833
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1834
reg[0] = reg[1] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1835
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1836
reg[3] = reg[4] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1837
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1838
reg[0] = reg[4] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1839
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x183a
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x183b
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x183c
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x183d
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x183e
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x183f
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1840
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1841
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1842
reg[0] = reg[1] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1843
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1844
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1845
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1846
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1847
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1848
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1849
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x184a
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x184b
reg[0] = reg[6] + reg[3]
reg[0] &= 0xFFFFFFFF
#0x184c
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x184d
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x184e
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x184f
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1850
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1851
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1852
reg[6] = 0x10ac
reg[6] &= 0xFFFFFFFF
#0x1853
reg[6] = 0x2557e2d5
reg[6] &= 0xFFFFFFFF
#0x1854
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1855
reg[6] = 0x10a4
reg[6] &= 0xFFFFFFFF
#0x1856
reg[6] = 0x46ba57f5
reg[6] &= 0xFFFFFFFF
#0x1857
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1858
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1859
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x185a
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x185b
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x185c
reg[6] = 0x10a0
reg[6] &= 0xFFFFFFFF
#0x185d
reg[6] = 0xcd13a639
reg[6] &= 0xFFFFFFFF
#0x185e
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x185f
reg[6] = 0x10a8
reg[6] &= 0xFFFFFFFF
#0x1860
reg[6] = 0x2e3eb69a
reg[6] &= 0xFFFFFFFF
#0x1861
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1862
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x1863
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1864
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1865
reg[0] = reg[6] + reg[1]
reg[0] &= 0xFFFFFFFF
#0x1866
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1867
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1868
reg[4] = reg[0] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1869
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x186a
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x186b
reg[3] = reg[1] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x186c
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x186d
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x186e
reg[4] = reg[3] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x186f
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x1870
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1871
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1872
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1873
reg[3] = reg[2] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1874
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1875
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1876
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1877
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1878
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1879
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x187a
reg[2] = reg[0] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x187b
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x187c
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x187d
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x187e
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x187f
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1880
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1881
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1882
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1883
reg[2] = reg[6] + reg[3]
reg[2] &= 0xFFFFFFFF
#0x1884
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1885
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1886
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1887
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1888
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1889
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x188a
reg[6] = 0x10bc
reg[6] &= 0xFFFFFFFF
#0x188b
reg[6] = 0x46f131f5
reg[6] &= 0xFFFFFFFF
#0x188c
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x188d
reg[6] = 0x10b4
reg[6] &= 0xFFFFFFFF
#0x188e
reg[6] = 0xbfb31e7
reg[6] &= 0xFFFFFFFF
#0x188f
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1890
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1891
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1892
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1893
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1894
reg[6] = 0x10b0
reg[6] &= 0xFFFFFFFF
#0x1895
reg[6] = 0xb72eb4d1
reg[6] &= 0xFFFFFFFF
#0x1896
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1897
reg[6] = 0x10b8
reg[6] &= 0xFFFFFFFF
#0x1898
reg[6] = 0x8884631d
reg[6] &= 0xFFFFFFFF
#0x1899
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x189a
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x189b
reg[2] = reg[6] + reg[3]
reg[2] &= 0xFFFFFFFF
#0x189c
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x189d
reg[4] = reg[0] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x189e
reg[2] = reg[0] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x189f
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18a0
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18a1
reg[3] = reg[4] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x18a2
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18a3
reg[0] = reg[2] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x18a4
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18a5
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18a6
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x18a7
reg[4] = reg[2] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x18a8
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18a9
reg[2] = reg[3] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x18aa
reg[1] = reg[3] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x18ab
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18ac
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18ad
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18ae
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x18af
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x18b0
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x18b1
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x18b2
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18b3
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x18b4
reg[1] = reg[4] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x18b5
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18b6
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18b7
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x18b8
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x18b9
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18ba
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x18bb
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x18bc
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x18bd
reg[1] = reg[6] + reg[2]
reg[1] &= 0xFFFFFFFF
#0x18be
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18bf
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x18c0
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x18c1
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18c2
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18c3
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18c4
reg[6] = 0x10cc
reg[6] &= 0xFFFFFFFF
#0x18c5
reg[6] = 0x36e610d5
reg[6] &= 0xFFFFFFFF
#0x18c6
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18c7
reg[6] = 0x10c4
reg[6] &= 0xFFFFFFFF
#0x18c8
reg[6] = 0x7bdc2af9
reg[6] &= 0xFFFFFFFF
#0x18c9
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18ca
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x18cb
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x18cc
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x18cd
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x18ce
reg[6] = 0x10c0
reg[6] &= 0xFFFFFFFF
#0x18cf
reg[6] = 0x768e314e
reg[6] &= 0xFFFFFFFF
#0x18d0
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18d1
reg[6] = 0x10c8
reg[6] &= 0xFFFFFFFF
#0x18d2
reg[6] = 0x8e28e22e
reg[6] &= 0xFFFFFFFF
#0x18d3
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18d4
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x18d5
reg[1] = reg[6] + reg[0]
reg[1] &= 0xFFFFFFFF
#0x18d6
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x18d7
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18d8
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18d9
reg[3] = reg[1] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x18da
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x18db
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18dc
reg[3] = reg[4] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x18dd
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18de
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x18df
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18e0
reg[1] = reg[3] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x18e1
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18e2
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18e3
reg[0] = reg[2] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x18e4
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x18e5
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18e6
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x18e7
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x18e8
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x18e9
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x18ea
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18eb
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x18ec
reg[4] = reg[2] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x18ed
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18ee
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x18ef
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x18f0
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x18f1
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18f2
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x18f3
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x18f4
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x18f5
reg[4] = reg[6] + reg[3]
reg[4] &= 0xFFFFFFFF
#0x18f6
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18f7
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x18f8
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x18f9
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18fa
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x18fb
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x18fc
reg[6] = 0x10dc
reg[6] &= 0xFFFFFFFF
#0x18fd
reg[6] = 0xbdc3d085
reg[6] &= 0xFFFFFFFF
#0x18fe
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x18ff
reg[6] = 0x10d4
reg[6] &= 0xFFFFFFFF
#0x1900
reg[6] = 0x41e77301
reg[6] &= 0xFFFFFFFF
#0x1901
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1902
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1903
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1904
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1905
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1906
reg[6] = 0x10d0
reg[6] &= 0xFFFFFFFF
#0x1907
reg[6] = 0x1cace4e2
reg[6] &= 0xFFFFFFFF
#0x1908
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1909
reg[6] = 0x10d8
reg[6] &= 0xFFFFFFFF
#0x190a
reg[6] = 0x9f25bb05
reg[6] &= 0xFFFFFFFF
#0x190b
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x190c
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x190d
reg[4] = reg[6] + reg[3]
reg[4] &= 0xFFFFFFFF
#0x190e
reg[3] = reg[2] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x190f
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1910
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x1911
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1912
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1913
reg[3] = reg[4] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1914
reg[4] = reg[1] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1915
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1916
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1917
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1918
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1919
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x191a
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x191b
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x191c
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x191d
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x191e
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x191f
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1920
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1921
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1922
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1923
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1924
reg[0] = reg[4] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1925
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1926
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1927
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1928
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1929
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x192a
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x192b
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x192c
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x192d
reg[0] = reg[6] + reg[2]
reg[0] &= 0xFFFFFFFF
#0x192e
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x192f
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1930
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1931
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1932
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1933
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1934
reg[6] = 0x10ec
reg[6] &= 0xFFFFFFFF
#0x1935
reg[6] = 0xa624d6a5
reg[6] &= 0xFFFFFFFF
#0x1936
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1937
reg[6] = 0x10e4
reg[6] &= 0xFFFFFFFF
#0x1938
reg[6] = 0x79588917
reg[6] &= 0xFFFFFFFF
#0x1939
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x193a
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x193b
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x193c
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x193d
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x193e
reg[6] = 0x10e0
reg[6] &= 0xFFFFFFFF
#0x193f
reg[6] = 0x3b968e0c
reg[6] &= 0xFFFFFFFF
#0x1940
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1941
reg[6] = 0x10e8
reg[6] &= 0xFFFFFFFF
#0x1942
reg[6] = 0x77c4ff75
reg[6] &= 0xFFFFFFFF
#0x1943
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1944
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1945
reg[0] = reg[6] + reg[2]
reg[0] &= 0xFFFFFFFF
#0x1946
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1947
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1948
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1949
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x194a
reg[2] = reg[1] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x194b
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x194c
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x194d
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x194e
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x194f
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1950
reg[3] = reg[4] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1951
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1952
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1953
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1954
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1955
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1956
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1957
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1958
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1959
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x195a
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x195b
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x195c
reg[4] = reg[3] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x195d
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x195e
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x195f
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1960
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1961
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1962
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1963
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1964
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1965
reg[4] = reg[6] + reg[0]
reg[4] &= 0xFFFFFFFF
#0x1966
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1967
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1968
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1969
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x196a
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x196b
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x196c
reg[6] = 0x10fc
reg[6] &= 0xFFFFFFFF
#0x196d
reg[6] = 0xef6f58c8
reg[6] &= 0xFFFFFFFF
#0x196e
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x196f
reg[6] = 0x10f4
reg[6] &= 0xFFFFFFFF
#0x1970
reg[6] = 0x5b843c5c
reg[6] &= 0xFFFFFFFF
#0x1971
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1972
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1973
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1974
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1975
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1976
reg[6] = 0x10f0
reg[6] &= 0xFFFFFFFF
#0x1977
reg[6] = 0xd4533b25
reg[6] &= 0xFFFFFFFF
#0x1978
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1979
reg[6] = 0x10f8
reg[6] &= 0xFFFFFFFF
#0x197a
reg[6] = 0x169e44bb
reg[6] &= 0xFFFFFFFF
#0x197b
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x197c
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x197d
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x197e
reg[4] = reg[6] + reg[0]
reg[4] &= 0xFFFFFFFF
#0x197f
reg[3] = ~reg[3] & 0xFFFFFFFF
reg[3] &= 0xFFFFFFFF
#0x1980
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1981
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1982
reg[1] = reg[4] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1983
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1984
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1985
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1986
reg[3] = reg[0] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1987
reg[2] = reg[3] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1988
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1989
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x198a
reg[1] = reg[3] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x198b
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x198c
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x198d
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x198e
reg[4] = reg[3] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x198f
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1990
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1991
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1992
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1993
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1994
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1995
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1996
reg[0] = reg[4] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1997
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1998
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1999
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x199a
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x199b
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x199c
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x199d
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x199e
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x199f
reg[0] = reg[6] + reg[2]
reg[0] &= 0xFFFFFFFF
#0x19a0
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19a1
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x19a2
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x19a3
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19a4
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19a5
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19a6
reg[6] = 0x110c
reg[6] &= 0xFFFFFFFF
#0x19a7
reg[6] = 0x1de931d3
reg[6] &= 0xFFFFFFFF
#0x19a8
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19a9
reg[6] = 0x1104
reg[6] &= 0xFFFFFFFF
#0x19aa
reg[6] = 0x59a74786
reg[6] &= 0xFFFFFFFF
#0x19ab
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19ac
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x19ad
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x19ae
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x19af
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x19b0
reg[6] = 0x1100
reg[6] &= 0xFFFFFFFF
#0x19b1
reg[6] = 0xa74e0a0b
reg[6] &= 0xFFFFFFFF
#0x19b2
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19b3
reg[6] = 0x1108
reg[6] &= 0xFFFFFFFF
#0x19b4
reg[6] = 0x9e915503
reg[6] &= 0xFFFFFFFF
#0x19b5
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19b6
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x19b7
reg[0] = reg[6] + reg[3]
reg[0] &= 0xFFFFFFFF
#0x19b8
reg[3] = reg[4] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x19b9
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19ba
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x19bb
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x19bc
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19bd
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x19be
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19bf
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19c0
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19c1
reg[0] = reg[4] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x19c2
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19c3
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x19c4
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19c5
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x19c6
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19c7
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19c8
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x19c9
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x19ca
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x19cb
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x19cc
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19cd
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x19ce
reg[0] = reg[1] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x19cf
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19d0
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19d1
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x19d2
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x19d3
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19d4
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x19d5
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x19d6
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x19d7
reg[0] = reg[6] + reg[2]
reg[0] &= 0xFFFFFFFF
#0x19d8
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19d9
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x19da
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x19db
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19dc
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19dd
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19de
reg[6] = 0x111c
reg[6] &= 0xFFFFFFFF
#0x19df
reg[6] = 0x27cb82c5
reg[6] &= 0xFFFFFFFF
#0x19e0
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19e1
reg[6] = 0x1114
reg[6] &= 0xFFFFFFFF
#0x19e2
reg[6] = 0xad6c1225
reg[6] &= 0xFFFFFFFF
#0x19e3
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19e4
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x19e5
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x19e6
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x19e7
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x19e8
reg[6] = 0x1110
reg[6] &= 0xFFFFFFFF
#0x19e9
reg[6] = 0x4f3d653e
reg[6] &= 0xFFFFFFFF
#0x19ea
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19eb
reg[6] = 0x1118
reg[6] &= 0xFFFFFFFF
#0x19ec
reg[6] = 0x4780e661
reg[6] &= 0xFFFFFFFF
#0x19ed
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19ee
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x19ef
reg[0] = reg[6] + reg[2]
reg[0] &= 0xFFFFFFFF
#0x19f0
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19f1
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19f2
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x19f3
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x19f4
reg[1] = reg[2] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x19f5
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19f6
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x19f7
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x19f8
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x19f9
reg[2] = reg[0] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x19fa
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x19fb
reg[3] = reg[1] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x19fc
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x19fd
reg[2] = reg[1] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x19fe
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x19ff
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a00
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a01
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1a02
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a03
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1a04
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a05
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a06
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1a07
reg[2] = reg[0] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1a08
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a09
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a0a
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1a0b
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a0c
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a0d
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1a0e
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a0f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1a10
reg[2] = reg[6] + reg[3]
reg[2] &= 0xFFFFFFFF
#0x1a11
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a12
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1a13
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1a14
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a15
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a16
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a17
reg[6] = 0x112c
reg[6] &= 0xFFFFFFFF
#0x1a18
reg[6] = 0x8750c34f
reg[6] &= 0xFFFFFFFF
#0x1a19
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a1a
reg[6] = 0x1124
reg[6] &= 0xFFFFFFFF
#0x1a1b
reg[6] = 0xbf671847
reg[6] &= 0xFFFFFFFF
#0x1a1c
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a1d
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1a1e
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a1f
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1a20
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a21
reg[6] = 0x1120
reg[6] &= 0xFFFFFFFF
#0x1a22
reg[6] = 0xea5cb485
reg[6] &= 0xFFFFFFFF
#0x1a23
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a24
reg[6] = 0x1128
reg[6] &= 0xFFFFFFFF
#0x1a25
reg[6] = 0x95f1eab7
reg[6] &= 0xFFFFFFFF
#0x1a26
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a27
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x1a28
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a29
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1a2a
reg[2] = reg[6] + reg[0]
reg[2] &= 0xFFFFFFFF
#0x1a2b
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a2c
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a2d
reg[1] = reg[2] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a2e
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a2f
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a30
reg[3] = reg[0] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a31
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a32
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a33
reg[1] = reg[3] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a34
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1a35
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a36
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a37
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a38
reg[3] = reg[4] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a39
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1a3a
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a3b
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1a3c
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a3d
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a3e
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1a3f
reg[4] = reg[2] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1a40
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a41
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a42
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1a43
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a44
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a45
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1a46
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a47
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1a48
reg[4] = reg[6] + reg[3]
reg[4] &= 0xFFFFFFFF
#0x1a49
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a4a
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1a4b
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1a4c
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a4d
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a4e
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a4f
reg[6] = 0x113c
reg[6] &= 0xFFFFFFFF
#0x1a50
reg[6] = 0xa5e4701
reg[6] &= 0xFFFFFFFF
#0x1a51
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a52
reg[6] = 0x1134
reg[6] &= 0xFFFFFFFF
#0x1a53
reg[6] = 0xb224527b
reg[6] &= 0xFFFFFFFF
#0x1a54
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a55
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1a56
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a57
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1a58
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a59
reg[6] = 0x1130
reg[6] &= 0xFFFFFFFF
#0x1a5a
reg[6] = 0xd2ae1926
reg[6] &= 0xFFFFFFFF
#0x1a5b
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a5c
reg[6] = 0x1138
reg[6] &= 0xFFFFFFFF
#0x1a5d
reg[6] = 0x260e583a
reg[6] &= 0xFFFFFFFF
#0x1a5e
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a5f
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1a60
reg[4] = reg[6] + reg[3]
reg[4] &= 0xFFFFFFFF
#0x1a61
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a62
reg[1] = reg[2] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a63
reg[4] = reg[2] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a64
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a65
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a66
reg[3] = reg[1] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a67
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a68
reg[2] = reg[4] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a69
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a6a
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a6b
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a6c
reg[1] = reg[4] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a6d
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a6e
reg[4] = reg[3] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a6f
reg[0] = reg[3] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1a70
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a71
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a72
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a73
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1a74
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a75
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1a76
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a77
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a78
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1a79
reg[0] = reg[1] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1a7a
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a7b
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a7c
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1a7d
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a7e
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a7f
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1a80
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a81
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1a82
reg[0] = reg[6] + reg[4]
reg[0] &= 0xFFFFFFFF
#0x1a83
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a84
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1a85
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1a86
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a87
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a88
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a89
reg[6] = 0x114c
reg[6] &= 0xFFFFFFFF
#0x1a8a
reg[6] = 0xea73214a
reg[6] &= 0xFFFFFFFF
#0x1a8b
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a8c
reg[6] = 0x1144
reg[6] &= 0xFFFFFFFF
#0x1a8d
reg[6] = 0x8cdf8a35
reg[6] &= 0xFFFFFFFF
#0x1a8e
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1a8f
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1a90
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a91
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1a92
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a93
reg[6] = 0x1140
reg[6] &= 0xFFFFFFFF
#0x1a94
reg[6] = 0xd73f30d3
reg[6] &= 0xFFFFFFFF
#0x1a95
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a96
reg[6] = 0x1148
reg[6] &= 0xFFFFFFFF
#0x1a97
reg[6] = 0x13a76c9d
reg[6] &= 0xFFFFFFFF
#0x1a98
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a99
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1a9a
reg[0] = reg[6] + reg[2]
reg[0] &= 0xFFFFFFFF
#0x1a9b
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a9c
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1a9d
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1a9e
reg[3] = reg[0] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1a9f
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1aa0
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1aa1
reg[3] = reg[1] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1aa2
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1aa3
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1aa4
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1aa5
reg[0] = reg[3] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1aa6
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1aa7
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1aa8
reg[2] = reg[4] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x1aa9
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x1aaa
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1aab
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1aac
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1aad
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1aae
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1aaf
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ab0
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1ab1
reg[1] = reg[4] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1ab2
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ab3
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ab4
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1ab5
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ab6
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ab7
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1ab8
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ab9
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1aba
reg[1] = reg[6] + reg[3]
reg[1] &= 0xFFFFFFFF
#0x1abb
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1abc
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1abd
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1abe
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1abf
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ac0
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ac1
reg[6] = 0x115c
reg[6] &= 0xFFFFFFFF
#0x1ac2
reg[6] = 0xc1bf8c8
reg[6] &= 0xFFFFFFFF
#0x1ac3
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ac4
reg[6] = 0x1154
reg[6] &= 0xFFFFFFFF
#0x1ac5
reg[6] = 0x7c710f13
reg[6] &= 0xFFFFFFFF
#0x1ac6
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ac7
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1ac8
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ac9
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1aca
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1acb
reg[6] = 0x1150
reg[6] &= 0xFFFFFFFF
#0x1acc
reg[6] = 0x4d504d0
reg[6] &= 0xFFFFFFFF
#0x1acd
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ace
reg[6] = 0x1158
reg[6] &= 0xFFFFFFFF
#0x1acf
reg[6] = 0xbb2fe640
reg[6] &= 0xFFFFFFFF
#0x1ad0
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ad1
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1ad2
reg[1] = reg[6] + reg[3]
reg[1] &= 0xFFFFFFFF
#0x1ad3
reg[3] = reg[4] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ad4
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ad5
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1ad6
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ad7
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ad8
reg[3] = reg[1] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ad9
reg[1] = reg[0] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ada
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1adb
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1adc
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1add
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ade
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1adf
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ae0
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ae1
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ae2
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ae3
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1ae4
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ae5
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1ae6
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ae7
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ae8
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1ae9
reg[2] = reg[1] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1aea
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1aeb
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1aec
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1aed
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1aee
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1aef
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1af0
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1af1
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1af2
reg[2] = reg[6] + reg[4]
reg[2] &= 0xFFFFFFFF
#0x1af3
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1af4
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1af5
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1af6
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1af7
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1af8
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1af9
reg[6] = 0x116c
reg[6] &= 0xFFFFFFFF
#0x1afa
reg[6] = 0xaf5862a0
reg[6] &= 0xFFFFFFFF
#0x1afb
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1afc
reg[6] = 0x1164
reg[6] &= 0xFFFFFFFF
#0x1afd
reg[6] = 0x5c4e1673
reg[6] &= 0xFFFFFFFF
#0x1afe
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1aff
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1b00
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b01
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1b02
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b03
reg[6] = 0x1160
reg[6] &= 0xFFFFFFFF
#0x1b04
reg[6] = 0x46cf343b
reg[6] &= 0xFFFFFFFF
#0x1b05
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b06
reg[6] = 0x1168
reg[6] &= 0xFFFFFFFF
#0x1b07
reg[6] = 0x3290d38
reg[6] &= 0xFFFFFFFF
#0x1b08
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b09
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1b0a
reg[2] = reg[6] + reg[4]
reg[2] &= 0xFFFFFFFF
#0x1b0b
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b0c
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b0d
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b0e
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b0f
reg[4] = reg[0] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b10
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x1b11
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b12
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b13
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b14
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b15
reg[3] = reg[1] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b16
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b17
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b18
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b19
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b1a
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b1b
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1b1c
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b1d
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1b1e
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b1f
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b20
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1b21
reg[1] = reg[3] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1b22
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b23
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b24
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1b25
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b26
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b27
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1b28
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b29
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1b2a
reg[1] = reg[6] + reg[2]
reg[1] &= 0xFFFFFFFF
#0x1b2b
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b2c
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1b2d
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1b2e
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b2f
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b30
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b31
reg[6] = 0x117c
reg[6] &= 0xFFFFFFFF
#0x1b32
reg[6] = 0x51a716de
reg[6] &= 0xFFFFFFFF
#0x1b33
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b34
reg[6] = 0x1174
reg[6] &= 0xFFFFFFFF
#0x1b35
reg[6] = 0x874dc117
reg[6] &= 0xFFFFFFFF
#0x1b36
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b37
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1b38
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b39
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1b3a
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b3b
reg[6] = 0x1170
reg[6] &= 0xFFFFFFFF
#0x1b3c
reg[6] = 0xbb024120
reg[6] &= 0xFFFFFFFF
#0x1b3d
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b3e
reg[6] = 0x1178
reg[6] &= 0xFFFFFFFF
#0x1b3f
reg[6] = 0xac9675e9
reg[6] &= 0xFFFFFFFF
#0x1b40
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b41
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x1b42
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1b43
reg[1] = reg[6] + reg[2]
reg[1] &= 0xFFFFFFFF
#0x1b44
reg[3] = ~reg[3] & 0xFFFFFFFF
reg[3] &= 0xFFFFFFFF
#0x1b45
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b46
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b47
reg[0] = reg[1] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b48
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b49
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b4a
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b4b
reg[3] = reg[2] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b4c
reg[4] = reg[3] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b4d
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b4e
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b4f
reg[0] = reg[3] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b50
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b51
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b52
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b53
reg[1] = reg[3] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b54
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b55
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1b56
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b57
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1b58
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b59
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b5a
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1b5b
reg[2] = reg[1] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1b5c
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b5d
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b5e
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1b5f
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b60
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b61
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1b62
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b63
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1b64
reg[2] = reg[6] + reg[4]
reg[2] &= 0xFFFFFFFF
#0x1b65
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b66
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1b67
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1b68
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b69
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b6a
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b6b
reg[6] = 0x118c
reg[6] &= 0xFFFFFFFF
#0x1b6c
reg[6] = 0x27ccc753
reg[6] &= 0xFFFFFFFF
#0x1b6d
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b6e
reg[6] = 0x1184
reg[6] &= 0xFFFFFFFF
#0x1b6f
reg[6] = 0x33a7b040
reg[6] &= 0xFFFFFFFF
#0x1b70
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b71
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1b72
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b73
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1b74
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b75
reg[6] = 0x1180
reg[6] &= 0xFFFFFFFF
#0x1b76
reg[6] = 0x98b3656f
reg[6] &= 0xFFFFFFFF
#0x1b77
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b78
reg[6] = 0x1188
reg[6] &= 0xFFFFFFFF
#0x1b79
reg[6] = 0x5f97504f
reg[6] &= 0xFFFFFFFF
#0x1b7a
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b7b
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1b7c
reg[2] = reg[6] + reg[3]
reg[2] &= 0xFFFFFFFF
#0x1b7d
reg[3] = reg[1] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b7e
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b7f
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b80
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x1b81
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b82
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b83
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b84
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b85
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b86
reg[2] = reg[1] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x1b87
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b88
reg[0] = reg[4] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b89
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b8a
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x1b8b
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b8c
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b8d
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1b8e
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b8f
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1b90
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1b91
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b92
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1b93
reg[2] = reg[0] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1b94
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b95
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b96
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1b97
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1b98
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b99
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1b9a
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1b9b
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1b9c
reg[2] = reg[6] + reg[4]
reg[2] &= 0xFFFFFFFF
#0x1b9d
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1b9e
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1b9f
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1ba0
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ba1
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ba2
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ba3
reg[6] = 0x119c
reg[6] &= 0xFFFFFFFF
#0x1ba4
reg[6] = 0x4d3f812a
reg[6] &= 0xFFFFFFFF
#0x1ba5
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ba6
reg[6] = 0x1194
reg[6] &= 0xFFFFFFFF
#0x1ba7
reg[6] = 0x5fb8df77
reg[6] &= 0xFFFFFFFF
#0x1ba8
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ba9
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1baa
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bab
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1bac
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bad
reg[6] = 0x1190
reg[6] &= 0xFFFFFFFF
#0x1bae
reg[6] = 0x3193031d
reg[6] &= 0xFFFFFFFF
#0x1baf
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bb0
reg[6] = 0x1198
reg[6] &= 0xFFFFFFFF
#0x1bb1
reg[6] = 0x55ac60dc
reg[6] &= 0xFFFFFFFF
#0x1bb2
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bb3
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1bb4
reg[2] = reg[6] + reg[4]
reg[2] &= 0xFFFFFFFF
#0x1bb5
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1bb6
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bb7
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x1bb8
reg[2] = reg[4] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bb9
reg[0] = reg[4] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bba
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bbb
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bbc
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1bbd
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bbe
reg[4] = reg[2] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1bbf
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bc0
reg[3] = reg[0] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bc1
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bc2
reg[4] = reg[0] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1bc3
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1bc4
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bc5
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bc6
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1bc7
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bc8
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1bc9
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bca
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bcb
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1bcc
reg[4] = reg[2] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1bcd
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bce
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bcf
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1bd0
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bd1
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bd2
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1bd3
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bd4
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1bd5
reg[4] = reg[6] + reg[3]
reg[4] &= 0xFFFFFFFF
#0x1bd6
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bd7
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1bd8
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1bd9
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bda
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bdb
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bdc
reg[6] = 0x11ac
reg[6] &= 0xFFFFFFFF
#0x1bdd
reg[6] = 0x90b50110
reg[6] &= 0xFFFFFFFF
#0x1bde
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bdf
reg[6] = 0x11a4
reg[6] &= 0xFFFFFFFF
#0x1be0
reg[6] = 0xbe53dc63
reg[6] &= 0xFFFFFFFF
#0x1be1
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1be2
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1be3
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1be4
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1be5
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1be6
reg[6] = 0x11a0
reg[6] &= 0xFFFFFFFF
#0x1be7
reg[6] = 0x39d1b7e4
reg[6] &= 0xFFFFFFFF
#0x1be8
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1be9
reg[6] = 0x11a8
reg[6] &= 0xFFFFFFFF
#0x1bea
reg[6] = 0x37ece0fc
reg[6] &= 0xFFFFFFFF
#0x1beb
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bec
reg[0] = ~reg[0] & 0xFFFFFFFF
reg[0] &= 0xFFFFFFFF
#0x1bed
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bee
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1bef
reg[4] = reg[6] + reg[2]
reg[4] &= 0xFFFFFFFF
#0x1bf0
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bf1
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bf2
reg[0] = reg[4] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bf3
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bf4
reg[0] = reg[3] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bf5
reg[3] = reg[2] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bf6
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bf7
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1bf8
reg[0] = reg[3] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bf9
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x1bfa
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1bfb
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1bfc
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1bfd
reg[3] = reg[1] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1bfe
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1bff
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c00
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1c01
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c02
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c03
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1c04
reg[1] = reg[4] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1c05
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c06
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c07
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1c08
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c09
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c0a
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1c0b
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c0c
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1c0d
reg[1] = reg[6] + reg[3]
reg[1] &= 0xFFFFFFFF
#0x1c0e
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c0f
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1c10
reg[1] = reg[1] << reg[6]
reg[1] &= 0xFFFFFFFF
#0x1c11
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c12
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c13
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c14
reg[6] = 0x11bc
reg[6] &= 0xFFFFFFFF
#0x1c15
reg[6] = 0x144cc343
reg[6] &= 0xFFFFFFFF
#0x1c16
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c17
reg[6] = 0x11b4
reg[6] &= 0xFFFFFFFF
#0x1c18
reg[6] = 0x7ed43c9b
reg[6] &= 0xFFFFFFFF
#0x1c19
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c1a
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1c1b
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c1c
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1c1d
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c1e
reg[6] = 0x11b0
reg[6] &= 0xFFFFFFFF
#0x1c1f
reg[6] = 0x3403681b
reg[6] &= 0xFFFFFFFF
#0x1c20
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c21
reg[6] = 0x11b8
reg[6] &= 0xFFFFFFFF
#0x1c22
reg[6] = 0xc9a8c10b
reg[6] &= 0xFFFFFFFF
#0x1c23
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c24
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1c25
reg[1] = reg[6] + reg[3]
reg[1] &= 0xFFFFFFFF
#0x1c26
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c27
reg[0] = reg[4] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c28
reg[1] = reg[4] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c29
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c2a
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c2b
reg[3] = reg[0] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c2c
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c2d
reg[4] = reg[1] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c2e
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c2f
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c30
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c31
reg[0] = reg[1] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c32
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c33
reg[1] = reg[3] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c34
reg[2] = reg[3] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c35
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c36
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c37
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c38
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1c39
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c3a
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1c3b
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c3c
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c3d
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1c3e
reg[2] = reg[0] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1c3f
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c40
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c41
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1c42
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c43
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c44
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1c45
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c46
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1c47
reg[2] = reg[6] + reg[1]
reg[2] &= 0xFFFFFFFF
#0x1c48
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c49
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1c4a
reg[2] = reg[2] << reg[6]
reg[2] &= 0xFFFFFFFF
#0x1c4b
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c4c
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c4d
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c4e
reg[6] = 0x11cc
reg[6] &= 0xFFFFFFFF
#0x1c4f
reg[6] = 0x612d9b35
reg[6] &= 0xFFFFFFFF
#0x1c50
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c51
reg[6] = 0x11c4
reg[6] &= 0xFFFFFFFF
#0x1c52
reg[6] = 0xf9040145
reg[6] &= 0xFFFFFFFF
#0x1c53
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c54
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1c55
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c56
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1c57
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c58
reg[6] = 0x11c0
reg[6] &= 0xFFFFFFFF
#0x1c59
reg[6] = 0x29a745c8
reg[6] &= 0xFFFFFFFF
#0x1c5a
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c5b
reg[6] = 0x11c8
reg[6] &= 0xFFFFFFFF
#0x1c5c
reg[6] = 0xee724cd5
reg[6] &= 0xFFFFFFFF
#0x1c5d
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c5e
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1c5f
reg[2] = reg[6] + reg[4]
reg[2] &= 0xFFFFFFFF
#0x1c60
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c61
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c62
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c63
reg[3] = reg[2] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c64
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c65
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c66
reg[3] = reg[0] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c67
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c68
reg[1] = reg[0] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c69
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c6a
reg[2] = reg[3] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c6b
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c6c
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c6d
reg[4] = reg[1] | reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c6e
reg[1] = ~reg[1] & 0xFFFFFFFF
reg[1] &= 0xFFFFFFFF
#0x1c6f
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c70
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1c71
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c72
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1c73
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c74
reg[3] = reg[1] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c75
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1c76
reg[0] = reg[1] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1c77
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c78
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c79
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1c7a
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c7b
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c7c
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1c7d
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c7e
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1c7f
reg[0] = reg[6] + reg[3]
reg[0] &= 0xFFFFFFFF
#0x1c80
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c81
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1c82
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1c83
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c84
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c85
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c86
reg[6] = 0x11dc
reg[6] &= 0xFFFFFFFF
#0x1c87
reg[6] = 0xb93c2654
reg[6] &= 0xFFFFFFFF
#0x1c88
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1c89
reg[6] = 0x11d4
reg[6] &= 0xFFFFFFFF
#0x1c8a
reg[6] = 0xf3aeb17
reg[6] &= 0xFFFFFFFF
#0x1c8b
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c8c
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1c8d
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c8e
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1c8f
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c90
reg[6] = 0x11d0
reg[6] &= 0xFFFFFFFF
#0x1c91
reg[6] = 0x7895b36c
reg[6] &= 0xFFFFFFFF
#0x1c92
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c93
reg[6] = 0x11d8
reg[6] &= 0xFFFFFFFF
#0x1c94
reg[6] = 0x34e0d235
reg[6] &= 0xFFFFFFFF
#0x1c95
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c96
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1c97
reg[0] = reg[6] + reg[3]
reg[0] &= 0xFFFFFFFF
#0x1c98
reg[3] = reg[1] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c99
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1c9a
reg[2] = ~reg[2] & 0xFFFFFFFF
reg[2] &= 0xFFFFFFFF
#0x1c9b
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c9c
reg[1] = reg[4] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1c9d
reg[3] = reg[0] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1c9e
reg[0] = reg[2] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1c9f
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ca0
reg[1] = reg[2] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ca1
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ca2
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ca3
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ca4
reg[4] = reg[0] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ca5
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ca6
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ca7
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ca8
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1ca9
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1caa
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1cab
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cac
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cad
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1cae
reg[4] = reg[0] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1caf
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cb0
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cb1
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1cb2
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cb3
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cb4
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1cb5
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cb6
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1cb7
reg[4] = reg[6] + reg[1]
reg[4] &= 0xFFFFFFFF
#0x1cb8
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1cb9
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1cba
reg[4] = reg[4] << reg[6]
reg[4] &= 0xFFFFFFFF
#0x1cbb
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cbc
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1cbd
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cbe
reg[6] = 0x11ec
reg[6] &= 0xFFFFFFFF
#0x1cbf
reg[6] = 0x263bfd7b
reg[6] &= 0xFFFFFFFF
#0x1cc0
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cc1
reg[6] = 0x11e4
reg[6] &= 0xFFFFFFFF
#0x1cc2
reg[6] = 0xf4096a1
reg[6] &= 0xFFFFFFFF
#0x1cc3
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cc4
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1cc5
reg[0] = ROL(reg[0], reg[6])
reg[0] &= 0xFFFFFFFF
reg[0] = reg[0]
reg[0] &= 0xFFFFFFFF
#0x1cc6
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1cc7
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cc8
reg[6] = 0x11e0
reg[6] &= 0xFFFFFFFF
#0x1cc9
reg[6] = 0x4bc1ee86
reg[6] &= 0xFFFFFFFF
#0x1cca
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1ccb
reg[6] = 0x11e8
reg[6] &= 0xFFFFFFFF
#0x1ccc
reg[6] = 0xf846aaee
reg[6] &= 0xFFFFFFFF
#0x1ccd
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cce
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1ccf
reg[4] = reg[6] + reg[1]
reg[4] &= 0xFFFFFFFF
#0x1cd0
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cd1
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cd2
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cd3
reg[0] = reg[2] & reg[0]
reg[0] &= 0xFFFFFFFF
#0x1cd4
reg[1] = reg[2] | reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cd5
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x1cd6
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1cd7
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cd8
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cd9
reg[4] = reg[0] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1cda
reg[3] = reg[0] & reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cdb
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1cdc
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cdd
reg[2] = reg[1] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cde
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cdf
reg[1] = reg[3] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ce0
reg[6] = 0xd
reg[6] &= 0xFFFFFFFF
#0x1ce1
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1ce2
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1ce3
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1ce4
reg[4] = reg[3] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ce5
reg[6] = 0x3
reg[6] &= 0xFFFFFFFF
#0x1ce6
reg[0] = reg[3] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1ce7
reg[2] = reg[1] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1ce8
reg[4] = reg[1] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ce9
reg[6] = 0x1
reg[6] &= 0xFFFFFFFF
#0x1cea
reg[4] = ROL(reg[4], reg[6])
reg[4] &= 0xFFFFFFFF
reg[4] = reg[4]
reg[4] &= 0xFFFFFFFF
#0x1ceb
reg[2] = reg[0] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cec
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1ced
reg[2] = ROL(reg[2], reg[6])
reg[2] &= 0xFFFFFFFF
reg[2] = reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cee
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1cef
reg[0] = reg[6] + reg[4]
reg[0] &= 0xFFFFFFFF
#0x1cf0
reg[3] = reg[4] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cf1
reg[6] = 0x7
reg[6] &= 0xFFFFFFFF
#0x1cf2
reg[0] = reg[0] << reg[6]
reg[0] &= 0xFFFFFFFF
#0x1cf3
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cf4
reg[3] = reg[2] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cf5
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1cf6
reg[6] = 0x11fc
reg[6] &= 0xFFFFFFFF
#0x1cf7
reg[6] = 0xebb94610
reg[6] &= 0xFFFFFFFF
#0x1cf8
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1cf9
reg[6] = 0x11f4
reg[6] &= 0xFFFFFFFF
#0x1cfa
reg[6] = 0xb97d1dd5
reg[6] &= 0xFFFFFFFF
#0x1cfb
reg[4] = reg[6] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1cfc
reg[6] = 0x5
reg[6] &= 0xFFFFFFFF
#0x1cfd
reg[3] = ROL(reg[3], reg[6])
reg[3] &= 0xFFFFFFFF
reg[3] = reg[3]
reg[3] &= 0xFFFFFFFF
#0x1cfe
reg[6] = 0x16
reg[6] &= 0xFFFFFFFF
#0x1cff
reg[1] = ROL(reg[1], reg[6])
reg[1] &= 0xFFFFFFFF
reg[1] = reg[1]
reg[1] &= 0xFFFFFFFF
#0x1d00
reg[6] = 0x11f0
reg[6] &= 0xFFFFFFFF
#0x1d01
reg[6] = 0xc831a387
reg[6] &= 0xFFFFFFFF
#0x1d02
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1d03
reg[6] = 0x11f8
reg[6] &= 0xFFFFFFFF
#0x1d04
reg[6] = 0x5defaf9b
reg[6] &= 0xFFFFFFFF
#0x1d05
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1d06
reg[4] = ~reg[4] & 0xFFFFFFFF
reg[4] &= 0xFFFFFFFF
#0x1d07
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1d08
reg[0] = reg[6] + reg[4]
reg[0] &= 0xFFFFFFFF
#0x1d09
reg[3] = ~reg[3] & 0xFFFFFFFF
reg[3] &= 0xFFFFFFFF
#0x1d0a
reg[4] = reg[1] & reg[4]
reg[4] &= 0xFFFFFFFF
#0x1d0b
reg[4] = reg[2] ^ reg[4]
reg[4] &= 0xFFFFFFFF
#0x1d0c
reg[2] = reg[0] | reg[2]
reg[2] &= 0xFFFFFFFF
#0x1d0d
reg[0] = reg[1] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1d0e
reg[1] = reg[2] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1d0f
reg[2] = reg[3] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1d10
reg[3] = reg[4] | reg[3]
reg[3] &= 0xFFFFFFFF
#0x1d11
reg[1] = reg[3] & reg[1]
reg[1] &= 0xFFFFFFFF
#0x1d12
reg[3] = reg[0] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1d13
reg[0] = reg[2] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1d14
reg[2] = reg[3] & reg[2]
reg[2] &= 0xFFFFFFFF
#0x1d15
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1d16
reg[1] = reg[0] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1d17
reg[2] = reg[4] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1d18
reg[0] = reg[3] | reg[0]
reg[0] &= 0xFFFFFFFF
#0x1d19
reg[0] = reg[4] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1d1a
reg[6] = 0x120c
reg[6] &= 0xFFFFFFFF
#0x1d1b
reg[6] = 0x7d81ac6a
reg[6] &= 0xFFFFFFFF
#0x1d1c
reg[3] = reg[6] ^ reg[3]
reg[3] &= 0xFFFFFFFF
#0x1d1d
reg[6] = 0x1208
reg[6] &= 0xFFFFFFFF
#0x1d1e
reg[6] = 0x1295fab
reg[6] &= 0xFFFFFFFF
#0x1d1f
reg[2] = reg[6] ^ reg[2]
reg[2] &= 0xFFFFFFFF
#0x1d20
reg[6] = 0x1204
reg[6] &= 0xFFFFFFFF
#0x1d21
reg[6] = 0x316aa14c
reg[6] &= 0xFFFFFFFF
#0x1d22
reg[1] = reg[6] ^ reg[1]
reg[1] &= 0xFFFFFFFF
#0x1d23
reg[6] = 0x1200
reg[6] &= 0xFFFFFFFF
#0x1d24
reg[6] = 0x415cf190
reg[6] &= 0xFFFFFFFF
#0x1d25
reg[0] = reg[6] ^ reg[0]
reg[0] &= 0xFFFFFFFF
#0x1d26
reg[6] = 0x0
reg[6] &= 0xFFFFFFFF
#0x1d27
reg[5] = 0x0
reg[5] &= 0xFFFFFFFF
#0x1d28
reg[6] = 0x104
reg[6] &= 0xFFFFFFFF
#0x1d29
reg[5] = reg[5] + reg[6]
reg[5] &= 0xFFFFFFFF


'''
s.add(reg[0] == 0x0FC8DD37)
s.add(reg[1] == 0x6EAC8D07)
s.add(reg[2] == 0x849DC5D6)
s.add(reg[3] == 0xDAD6AA68)

s.add(reg[0] == 0xC1DD9621)
s.add(reg[1] == 0x01BCBBDA)
s.add(reg[2] == 0x71A9B868)
s.add(reg[3] == 0x4829251E)

s.add(reg[0] == 0x1162c35f)
s.add(reg[1] == 0xfe3e66ea)
s.add(reg[2] == 0xab45cdf1)
s.add(reg[3] == 0x004283fc)

s.add(reg[0] == 0x75f9ed92)
s.add(reg[1] == 0xa87df220)
s.add(reg[2] == 0x03da366f)
s.add(reg[3] == 0xe5d4e56c)

s.add(reg[0] == 0x2eed84f9)
s.add(reg[1] == 0x6dacb638)
s.add(reg[2] == 0x93511dfb)
s.add(reg[3] == 0xa920cf70)

s.add(reg[0] == 0xbb5ad95b)
s.add(reg[1] == 0x638ca71a)
s.add(reg[2] == 0x8d623ba1)
s.add(reg[3] == 0x229f913b)

'''
s.add(reg[0] == 0x1427cce6)
s.add(reg[1] == 0x64e47f56)
s.add(reg[2] == 0x05835bbd)
s.add(reg[3] == 0x84c9289b)



if(s.check() == sat):
    m = s.model()
    for i in range(4):
        print(hex(int(str(m[flag[i]]))))
