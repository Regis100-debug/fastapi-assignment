from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/product")
def create_product(product: dict = Body(...)):
    name = product.get("name")
    price = product.get("price")

    return {
        "message": "Product created",
        "product_name": name,
        "price": price
    }

@app.post("/customer")
def create_customer(customer: dict = Body(...)):
    return {
        "message": "Customer created",
        "customer_name": customer["name"],
        "email": customer["email"]
    }

@app.post("/order")
def create_order(order: dict = Body(...)):
    return {
        "message": "Order created",
        "customer": order["customer"],
        "product": order["product"],
        "quantity": order["quantity"]
    }