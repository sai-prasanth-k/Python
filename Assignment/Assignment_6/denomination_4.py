a = int(input())
h = int(a / 100)
ah = a - (h * 100)
f = int(ah / 50)
af = ah - (f * 50)
tw = int(af / 20)
at = af - (tw * 20)
t = int(at / 10)
print("100 Notes:",h)
print("50 Notes:",f)
print("20 Notes:",tw)
print("10 Notes:",t)