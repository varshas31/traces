from trace_module import SimpleTracer

def view_product(product_name):
    print("Viewing product {}".format(product_name))
    # Simulate some work
    for i in range(2):
        print("Loading product details {}".format(i))

def add_to_cart(product_name):
    print("Adding product {} to cart".format(product_name))
    # Simulate some work
    print("Updating cart with product {}".format(1))

def checkout(cart_name):
    print("Checking out {}".format(cart_name))
    # Simulate some work
    print("Processing checkout step {}".format(1))

def main():
    tracer = SimpleTracer("traces-app")
    tracer.log("view-product", view_product, "SmartPhone")
    tracer.log("add-to-cart", add_to_cart, "SmartPhone")
    tracer.log("checkout", checkout, "User Cart")

if __name__ == "__main__":
    main()

