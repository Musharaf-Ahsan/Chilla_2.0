# WHILE & FOR LOOPS
# x=0
# while (x<=10):
#     print(x)
#     x=x+1

#FOR LOOPS

# for x in range(0,10):
#     print(x)

#array
days=["mon","tue","wed","thu","fri","sat","sun"]
for d in days:
    # if (d=="fri"):
    #     break  #loop stops
    if (d=="fri"):
        continue #skips d
    print(d)