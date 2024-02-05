import json

# Open file
with open('seoData.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate through the products and print product names with non-null SEO data
count = 0
for product in data:
    if product.get('seo') is None:
        # print(product['id'])
        print(product['name'])
        count += 1
print("Count: " + str(count))