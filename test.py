nepali_hotel = [("veg momo",100,1),
                ("chicken momo",120,1),
                ("buff momo",150,1),
                ("chowmein",100,1)]

to_dollars = lambda x:(x[0],x[1]*132,x[2])

american_hotel = list(map(to_dollars,nepali_hotel))

for i in american_hotel:
    print(i,end="   ")
    print()

voters_list = [["RAM",18],
               ["SAM",17],
               ["HARI",50],
               ]

can_vote = lambda x:  x[1]>=18

voters = list(filter(can_vote,voters_list))

for i in voters:
    #print(i)
    print(f"{i[0]} can vote")
    print()





 
