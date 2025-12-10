chai_types = {
    "black_tea" : "Strong and bold black tea",
    "green_tea" : "Light and refreshing green tea",
    "herbal_tea" : "Caffeine-free herbal infusion",
    "oolong_tea" : "Partially fermented tea with a rich flavor",
    "white_tea" : "Delicate and subtle white tea"
}

# chai_types["herbal_tea"] = "A soothing blend of herbs and spices"

# for chai in chai_types:
#     print(f"{chai}: {chai_types[chai]}")

# for key, value in chai_types.items():
#     print(f"{key}: {value}")

# if "herbal_tea" in chai_types:  
#     print("Herbal tea is available.")

chai_types["Earl_Grey"] = "Black tea flavored with bergamot oil"

chai_types.pop("oolong_tea")

tea_Shops = {
    "Tea Heaven": "123 Tea St.",
    "Chai Corner": {
        "address": "456 Chai Ave.",
        "specialty": {
            "chai_types": ["black_tea", "herbal_tea", "Earl_Grey"]
        }
    },
}
for shop in tea_Shops:
    print(f"{shop}: {tea_Shops[shop]}")
