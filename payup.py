event_name = input("What's the name of the event? ")
cost = float(input("What's the cost of the event? "))
service_charge = float(input("What's the service charge? "))
group_size = int(input("What's the group size? "))
# input() ile kullanıcının vereceği değerleri değişkende tutup kullanıyoruz.
service_charge_total = cost * service_charge / 100
grand_total = cost + service_charge_total
total_per_person = grand_total / group_size

#print(type(cost))
#print(type(service_charge))
#print(type(group_size))

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event_name}:")
print()
print(f"Cost: ${cost: .2f}")
print(f"Service Charge: ${service_charge_total: .2f}")
print(f"Group Size: {group_size}")
print(f"Grand Total: ${grand_total: .2f}")
print(f"Each person must PayUp: ${total_per_person: .2f}")
# .2f ile basamak limiti belirliyoruz.