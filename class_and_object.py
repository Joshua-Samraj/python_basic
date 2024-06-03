class goa:
    name = ""
    drink =""
    def party(self):
        print("lets party.....")
    def beach(self):
        print("enjoy the beach")

ramesh = goa()  
suresh = goa()
 
ramesh.name = "Ramesh"
suresh.name = "Suresh"
ramesh.drink = "yes"
suresh.drink = "no"


print(ramesh.name,end="")

print(" Drink : ",ramesh.drink)
print(suresh.name ,end="")

print(" Drink : ",suresh.drink)

