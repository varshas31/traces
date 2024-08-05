from trace_module import SimpleTracer

def view_product(product_name):
    # Trace this function
    tracer.log("view-product", _view_product_internal, product_name)

def _view_product_internal(product_name):
    print("Viewing product {}".format(product_name))
    # Simulate some work
    for i in range(2):
        print("Loading product details {}".format(i))
    # Call add_to_cart here
    add_to_cart(product_name)

def add_to_cart(product_name):
    # Trace this function
    tracer.log("add-to-cart", _add_to_cart_internal, product_name)

def _add_to_cart_internal(product_name):
    print("Adding product {} to cart".format(product_name))
    # Simulate some work
    print("Updating cart with product {}".format(1))
    # Call checkout here
    checkout("User Cart")

def checkout(cart_name):
    # Trace this function
    tracer.log("checkout", _checkout_internal, cart_name)

def _checkout_internal(cart_name):
    print("Checking out {}".format(cart_name))
    # Simulate some work
    print("Processing checkout step {}".format(1))

def main():
    global tracer
    tracer = SimpleTracer("example", jaeger_host="localhost", jaeger_port=6831)

    # Start tracing the main function
    tracer.log("main", _main_internal)

def _main_internal():
    # Start the trace by calling view_product
    view_product("SmartPhone")

if __name__ == "__main__":
    main()
