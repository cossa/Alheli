a = ["Master", "online"]
a.insert(1, "code")
print(a)

c = [1,2,3]
c = [4, 5, 6]
d = [1,2,3]
c.insert(0, d)
print(c)

company = ["Julia", "Erick", "Dillon"]
company.sort()
print(company)

company = ["Julia", "Erick", "Dillon"]
company.sort(reverse=True)
print(company)

company = ["Julia", "Erick", "Dillon"]
company.sort(reverse=True, key=len)
print(company)