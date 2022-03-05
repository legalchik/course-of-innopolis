
prost = []
for i in range(10, 250):  #  В условий не сказано что включительно))
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        prost.append(i)
        
print(sum(prost)) 
