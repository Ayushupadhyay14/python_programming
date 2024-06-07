""" Transport mode selection
     choose a mode of transportation based on the distance 
     (<3km: walk 3-15km: bike>15km:car)"""
     
distance = 5

if distance <3:
    Transport="Walk"
elif distance<=15:
    Transport="Bike"    
else:
    Transport="Car"
print("AI recommends you the transport of :",Transport)    
    