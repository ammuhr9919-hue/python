product={
    "pencil":"15",
    "Pen":"10",
    "book":"150"
}
product["notebook"]=150
product["bag"]=500
product.pop("pencil")
print("product:",product)
print("product name:",product.keys())
print("price:",product.values())