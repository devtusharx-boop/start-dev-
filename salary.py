print("employee salary system")

name = input("enter employee name: ")
id = input("enter employee id: ")
basic = float(input("enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
ta = basic * 0.05
pf = basic * 0.08

gross = basic + hra + da + ta
net = gross - pf

print("\nemployee name :", name)
print("employee id :", id)
print("basic salary :", basic)
print("hra :", hra)
print("da :", da)
print("ta :", ta)
print("pf :", pf)
print("gross salary :", gross)
print("net salary :", net)

if net >= 50000:
    print("grade : a")
elif net >= 30000:
    print("grade : b")
elif net >= 15000:
    print("grade : c")
else:
    print("grade : d")