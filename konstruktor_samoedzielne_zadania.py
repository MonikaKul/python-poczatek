class Product:
    def __init__(self, name,  category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

class Order:
    def __init__(self, client_first_name, client_last_name, products = None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if products is None:
            products = []
        self.products = products
        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price

class Apple:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

def print_product(product):
    print(f"Nazwa: {product.name} | Kategoria: {product.category_name} | Cena: {product.unit_price}")

def print_order(order):
    print("=" * 20)
    print(f"Zamówienie zostało złożene przez: {order.client_first_name} {order.client_last_name}")
    print(f" O łącznej wartości {order.total_price} PLN")
    print("Zamówione produkty:")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("=" * 20)
    print()
def run_homework():
    cookies = Product(name= "Cookies", category_name="Food", unit_price= 3)
    order = Order(client_first_name="Jan", client_last_name="Kowalski", products = [cookies, cookies])
    empty_order = Order(client_first_name="Bazyl", client_last_name="Nowak")
    print_order(order)
    print_order(empty_order)

    #green_apple = Apple (species_name="Green", size=2, price=1.4)
    #red_apple = Apple (species_name= "Red", size = 3, price = 2.5)
    #print (red_apple.species_name, red_apple)
    #print(green_apple.species_name, green_apple)

    #old_potato = Potato(species_name="Old", size = 2, price = 1.2)
    #print(old_potato.species_name, old_potato)

    #cookies = Product(name= "Cookies", category_name="Food", unit_price= 3)
    #order = Order(client_first_name="Jan", client_last_name="Kowalski", products = [cookies])

    #print(cookies)
    #print(order)



if __name__ == '__main__':
    run_homework()