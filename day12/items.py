items={
    "rice":70,
    "sugar":46,
    "milk":67,
    "bread":50,
    "oil":55
}
total=0
for price in items.values():
    total=total+price
print("items:",items)
print("total price:",total)