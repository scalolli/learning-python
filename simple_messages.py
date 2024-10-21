messages = ["Hello", "World"]
result = " ".join(messages)

for message in messages:
    print(message)

print("Result is % s!" % result)

nums = [1, 2, 3]

incremented_array = map(lambda x: x + 1, nums)

print(list(incremented_array))

name = "ada lovelace"
print(f"{name.title()} - {name.upper()} - {name.lower()}")
