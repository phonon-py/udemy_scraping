import pandas as pd

df = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Peach'],
    'Price': [100, 120, 150]
})
print(df)

df2 = pd.DataFrame([
    {'Fruit': 'Apple', 'Price': 100},
    {'Fruit': 'Banana', 'Price': 120},
    {'Fruit': 'Peach', 'Price': 150},
])

print(df2)
