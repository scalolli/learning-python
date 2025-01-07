motorbikes = ["honda", "yamaha", "royal enfield", "BMW", "Harley"]

for motorbike in motorbikes:
    print(motorbike.title())

print(motorbikes)
motorbikes.sort()
capitalisedMotorbikeTitles = list(map(lambda b: b.title(), motorbikes))
print(f"{capitalisedMotorbikeTitles} with length {len(capitalisedMotorbikeTitles)}")

bikes = []
bikes.append("Trek")
bikes.append("Canondale")

print(bikes)

