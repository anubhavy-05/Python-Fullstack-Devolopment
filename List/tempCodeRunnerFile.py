charge =[50,25,25]
refund = sum(charge[:2]) 
charge.remove(25)
print(sum(charge)-refund)