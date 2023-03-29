#Dictionary is nothing but a key value pair
d1 = {}

d2 = {"Saurabh": "Student",
      "Ashutosh": "Fish",
      "Gaurav": "Roti",
      "Shubham": {"B":"maggie", "L":"roti", "D":"Chicken"}}

d2["Ankit"] = "Junk Food"
d2[420] = "kebabs"
print(d2);
del d2[420]
print(d2["Shubham"])
d3 = d2.copy() #if not write copy and we make changes in d3 then the changes will also be made in d2
del d3["Saurabh"]
d2.update({"leena":"Toffee"})
print(d2.keys())
print(d2.items())