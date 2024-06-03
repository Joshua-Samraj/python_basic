class laptop:
    Price = 0
    Processor = ""
    Ram = ""

    
        
hp = laptop()
Dell = laptop()

hp.price = 50000
hp.processor = "Intel"
hp.ram = "4GB"


Dell.price = 10000
Dell.processor = "amd"
Dell.ram = "8gb"

print("HP LATOP CONFIGURATION:")
print("Price : ",hp.price)
print("Processor : ",hp.processor)
print("Ram : ",hp.ram)
print("")
print("DELL CONFIGURATION:")
print("Price : ",Dell.price)
print("Processor : ",Dell.processor)
print("Ram : ",Dell.ram)