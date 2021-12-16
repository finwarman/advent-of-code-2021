#! /usr/bin/env python3
import re
import math
from operator import mul
from functools import reduce

# ==== INPUT ====
data = ""
f = '16.txt'
#f = 'demo.txt'
with open(f, 'r') as file:
    data = file.read()

hexIn = list(data.strip())

# ==== SOLUTION ====


def hexToBin(x):
    return bin(int(x, 16))[2:].zfill(4)


binString = ""
for x in hexIn:
    binString += (hexToBin(x))


operators = {
    0: "sum",
    1: "product",
    2: "min",
    3: "max",
    5: "gt",
    6: "lt",
    7: "eq"
}


class Packet:
    def __init__(self, v, t, typ="unknown", children=[], value=None):
        self.v = v
        self.t = t
        self.value = value
        self.type = typ
        self.children = children

    # pretty printing
    def __str__(self, indent=""):
        childString = ""
        if self.children:
            for c in self.children:
                childString += "\n{} - {}".format(indent,
                                                  c.__str__(indent + "  "))
        return "v: {1}, t: {2} ({3}: {4}) {5}".format(
            indent, self.v, self.t, self.type, self.value, childString)


def parsePackets(binString, ptr=0, packetsToFind=-1, maxPtrLength=-1):
    packets = []

    foundPackets = 0
    while (ptr < len(binString) - 7) and (ptr < maxPtrLength or maxPtrLength < 0) and (foundPackets < packetsToFind or packetsToFind < 1):
        v = int(binString[ptr:ptr+3], 2)
        t = int(binString[ptr+3:ptr+6], 2)
        ptr += 6

        packet = Packet(v, t)

        if t == 4:
            packet.type = "val"
            literal = ""
            last = binString[ptr]
            if last == "0":
                literal = binString[ptr+1:ptr+5]
                ptr += 5
            else:
                while last == "1":
                    literal += binString[ptr+1:ptr+5]
                    last = binString[ptr]
                    ptr += 5
            literal = int(literal, 2)
            packet.value = literal
        else:
            packet.type = "op"
            packet.value = operators[t]
            i = binString[ptr]
            ptr += 1
            if i == "0":
                subpacketLen = int(binString[ptr:ptr+15], 2)
                ptr += 15
                children, _ = parsePackets(
                    binString[ptr:ptr+subpacketLen], 0,  maxPtrLength=subpacketLen)
                packet.children = (children)
                ptr += subpacketLen
            elif i == "1":
                subpacketCount = int(binString[ptr:ptr+11], 2)
                ptr += 11
                children, ptrInc = parsePackets(
                    binString[ptr:], 0, packetsToFind=subpacketCount)
                packet.children = (children)
                ptr += ptrInc
            else:
                raise Exception("Unknown I-Value", i)

        foundPackets += 1
        packets.append(packet)
    return packets, ptr


def packetEval(packet: Packet):
    if packet.type == "val":
        return packet.value
    else:
        op = packet.value
        a = [packetEval(x) for x in packet.children]
        if op == "sum":
            return sum(a)
        elif op == "product":
            return reduce(mul, a, 1)
        elif op == "min":
            return min(a)
        elif op == "max":
            return max(a)
        elif op == "lt":
            return 1 if a[0] < a[1] else 0
        elif op == "gt":
            return 1 if a[0] > a[1] else 0
        elif op == "eq":
            return 1 if a[0] == a[1] else 0
        else:
            raise Exception("Unknown Operator", packet.value)


packets, ptr = parsePackets(
    binString, 0, packetsToFind=1, maxPtrLength=len(binString))


if packets:
    print(packets[0])
    print(packetEval(packets[0]))
else:
    print("Parsing Error")
