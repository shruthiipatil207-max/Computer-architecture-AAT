
# Question 1: Assembly Language Simulation

# Initialize memory
memory = {
    100: 12,
    104: 8
}

# Initialize registers
registers = {
    "R1": 0,
    "R2": 0,
    "R3": 0
}

print("ASSEMBLY LANGUAGE SIMULATION")
print("-" * 50)

# Step 1: LOAD R1, 100
print("\nInstruction: LOAD R1, 100")
registers["R1"] = memory[100]
print("R1 =", registers["R1"])

# Step 2: LOAD R2, 104
print("\nInstruction: LOAD R2, 104")
registers["R2"] = memory[104]
print("R2 =", registers["R2"])

# Step 3: ADD R3, R1, R2
print("\nInstruction: ADD R3, R1, R2")
registers["R3"] = registers["R1"] + registers["R2"]
print("R3 =", registers["R3"])

# Step 4: STORE R3, 108
print("\nInstruction: STORE R3, 108")
memory[108] = registers["R3"]
print("Memory[108] =", memory[108])

# Display final register contents
print("\nFINAL REGISTER CONTENTS")
print("-" * 50)

for reg, value in registers.items():
    print(reg, "=", value)

# Display final memory contents
print("\nFINAL MEMORY CONTENTS")
for address, value in memory.items():
    print("M[" + str(address) + "] =", value)
