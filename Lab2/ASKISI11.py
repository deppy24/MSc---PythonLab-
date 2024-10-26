import math
import random 
random.seed
r=random.randrange(20)
y=random.randrange(20)
p=math.pi
E=p*r*(math.sqrt(r**2+y**2)+r)
V=(1/3)*p*(r**2)*y
print(f"Το ολικο εμβαδον του κωνου ισουται με {E}, ενω ο ογκος του ισουται με {V}")