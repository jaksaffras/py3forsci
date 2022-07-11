
actor = "Chris Hemsworth"
city = "Sydney"
value = 23.45781

print(actor, city, value)  #  str(actor) + ' ' + str(city) + ' ' + str(value) + '\n'
print("DONE")

print(actor, city, value, sep="//")
print(actor, city, value, sep="+")
print(actor, city, value, sep=" *** ")
print(actor, city, value, sep="")
print(actor, city, value, sep="\n")
print()   # only print "\n"


print(actor, end=" ")
print("jellyfish", end="+")
print("wombat")

print("actor: {}".format(actor))


print(actor, "lives in", city)

print(f"{actor} lives in {city}")  # f-string (Python 3.6+)
print("{} lives in {}".format(actor, city))  #  old-style formatting
print("%s lives in %s" % (actor, city))  # oldest (Python 2) formatting


print(f"2 + 2 is {2 + 2}")

print("value is", value)
print(f"value is {value:.2f}")
print("value is {:.2f}".format(value))

print("2 + 2: {}".format(2 + 2))

print(f"len of actor is {len(actor)}")





