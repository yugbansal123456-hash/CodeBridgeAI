words = ["the", "cat", "and", "the", "dog", "and", "the", "bird"]
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

# C++ std::map iterates in sorted key order.
for word in sorted(counts):
    print(f"{word}: {counts[word]}")

print(f"Unique words: {len(counts)}")

nums = []
for i in range(1, 6):
    nums.append(i * i)

nums.pop()
nums.insert(0, 0)

print("Vector:", *nums)
print(f"Size: {len(nums)}, front: {nums[0]}, back: {nums[-1]}")
