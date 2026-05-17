#payment aggregator for a matatu fare collection system
total_fare = 0
total_passengers = 0
underpayments = []
while True:
    fare = int(input("How much did the passenger pay? "))
    if fare < 50:
        print(f"Invalid fare. Please enter a valid fare. Total passengers: {total_passengers}")
        continue
    if fare == 0:
        print("No more passengers. Ending fare collection.")
        break
    total_fare += fare
    total_passengers += 1
    print(f"Total fare collected: {total_fare}")
    print(f"Total passengers: {total_passengers}")
    MIN_FARE = 50
    SENTINEL_VALUE = 0
    if fare < MIN_FARE:
        print(f"Invalid fare. Please enter a valid fare. Total passengers: {total_passengers}")
        continue
    #underpayment handling
    underpayments = []
    underpayments.append((fare, total_passengers))
    if fare == SENTINEL_VALUE:
        print("No more passengers. Ending fare collection.")
        break
print(f"Total fare collected: {total_fare}")
print(f"Total passengers: {total_passengers}")
print(f"Underpayments: {underpayments}")

    