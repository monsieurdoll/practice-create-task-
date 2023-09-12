resturants = ["jack in the box", "taco bell", "chick fill a", "mcdonalds"]

new_resturant = input("what resturant would you like to add to the list of fast food resturants?")

def rankResturants(new_resturant, resturants) :
    for i in range(len(resturants)):
        rank = input("do you like a) " + new_resturant + " or b) " + resturants[i] + " more?")
        if rank =="a":
            resturants.insert(i, new_resturant)
            break

        elif rank == "b":
            continue

    if new_resturant not in resturants :
        resturants.append(new_resturant)

    return(resturants)

print("your new ranking is, " + rankResturants(new_resturant, resturants=))