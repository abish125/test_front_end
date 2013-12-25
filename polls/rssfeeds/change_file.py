f= open ("allergy_and_immunology1.txt", "r")
x= f.readlines()

end = ""

for y in range(len(x)):
    if y%2==0:
        for z in x[y].lower():
            if z == " ":
                end = end + "_"
            else:
                end = end + z
print end
    
g = open("allergy_and_immunology.txt", "w")
g.write(end)
