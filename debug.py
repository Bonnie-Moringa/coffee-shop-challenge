from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
Julius = Customer("Julius")
Stella = Customer("Stella")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = Julius.create_order(latte, 5.0)
order2 = Julius.create_order(espresso, 6.5)
order3 = Stella.create_order(latte, 7.0)

# Test customer.orders()
print(f"{Julius.name}'s Orders:")
for order in Julius.orders():
    print(f"- {order.coffee.name}, ${order.price}")

# Test customer.coffees()
print(f"{Julius.name}'s Coffees: {[coffee.name for coffee in Julius.coffees()]}")

# Test coffee.orders()
print(f"Orders for {latte.name}:")
for order in latte.orders():
    print(f"- {order.customer.name}, Ksh{order.price}")

# Test coffee.customers()
print(f"Customers who ordered {latte.name}: {[customer.name for customer in latte.customers()]}")

# Test coffee.num_orders() and average_price()
print(f"{latte.name} has {latte.num_orders()} orders, average price: Ksh{latte.average_price():.2f}")
