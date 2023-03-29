s = set()
print(type(s))
l = [1,2,3,4]
s_from_list = set(l)
print(s_from_list)
s.add(1)
s.add(1)  # 1 is already present so not double :)
s.add(2)
s.add(3)
print(s)

s.remove(2)
print(s)
s1 = {4,6}
print(s.isdisjoint(s1))