tea_types = ("green", "black", "oolong", "white", "herbal")
# print("Available tea types:")
# for tea in tea_types:
#     print(f"- {tea}")

len(tea_types)  # 5
more_tea = ("chamomile", "peppermint")
all_tea = tea_types + more_tea
print("All tea types:")
for tea in all_tea:
    print(f"- {tea}")