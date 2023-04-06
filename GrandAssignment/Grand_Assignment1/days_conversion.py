n = int(input())
year = int(n / 365)
ry = n - (year *365)
week = int(ry / 7)
rw = ry - (week * 7)
days = rw
print(year,"years",week,"weeks",days,"days")