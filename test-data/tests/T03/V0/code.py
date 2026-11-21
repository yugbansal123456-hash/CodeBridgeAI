# Word frequency using dictionary
words = ["the", "cat", "and", "the", "dog", "and", "the", "bird"]

counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

# C++ map prints keys in sorted order
for word in sorted(counts):
    print(f"{word}: {counts[word]}")

print("Unique words:", len(counts))

# List operations
nums = []

for i in range(1, 6):
    nums.append(i * i)

nums.pop()
nums.insert(0, 0)

print("Vector:", *nums)
print(
    "Size:", len(nums),
    ", front:", nums[0],
    ", back:", nums[-1]
)
