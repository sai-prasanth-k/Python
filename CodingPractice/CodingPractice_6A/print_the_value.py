s = input()
sLen = len(s) - 1
last = s[sLen]
n = int(s[:sLen])
if last == "T" :
    result = n * 10
elif last == "H" :
    result = n * 100
elif last == "K" :
    result = n * 1000

print(result)
