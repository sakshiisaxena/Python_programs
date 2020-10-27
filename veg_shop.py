#!/usr/bin/env python
# coding: utf-8

# In[4]:


items={"apple":100,
       "banana":200,
       "mango":300}
print('*********welcome to shop**********\n')
bill=0
for i in items:
    print(i,"\t$",items[i])
    
try:
    while True:
        order=input("enter your order")
        order=order.lower()
        if order == "cancel":
            break
        
        else:
            quantity=int(input('enter quantity:'))
            bill=bill+items[order]*quantity
    
except:
    print("order not valid")
print('Thank you for purchase,\n Your bill is',bill)


# In[ ]:




