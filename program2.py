
# Question 2: Direct Mapped Cache Simulation

# Number of cache lines
CACHE_LINES = 8

# Memory block access sequence
blocks = [3, 11, 3, 19, 11, 27, 3]

# Initially empty cache
cache = [None] * CACHE_LINES

# Hit and miss counters
hits = 0
misses = 0

print("DIRECT MAPPED CACHE SIMULATION")
print("=" * 75)

# Process each memory block
for block in blocks:

    # Calculate cache line
    line = block % CACHE_LINES

    print("\nMemory Block:", block)
    print("Cache Line:", line)

    # Check HIT or MISS
    if cache[line] == block:
        print("Status: HIT")
        hits += 1

    else:
        print("Status: MISS")
        misses += 1

        # Load block into cache
        cache[line] = block

    # Display cache contents
    print("Cache Contents:")
    for i in range(CACHE_LINES):
        print("Line", i, ":", cache[i])

    print("-" * 75)

# Calculate hit ratio
total_accesses = len(blocks)
hit_ratio = hits / total_accesses

# Display final results
print("\nFINAL RESULTS")
print("=" * 75)

print("Total Memory Accesses:", total_accesses)
print("Total Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", round(hit_ratio, 2))
print("Hit Ratio Percentage:", round(hit_ratio * 100, 2), "%")
