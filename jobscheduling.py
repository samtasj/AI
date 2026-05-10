# Job Scheduling using Greedy Algorithm

jobs = [
    ['J1', 2, 100],
    ['J2', 1, 50],
    ['J3', 2, 10],
    ['J4', 1, 20]
]

# Sort jobs according to profit (highest first)
jobs.sort(key=lambda x: x[2], reverse=True)

# Find maximum deadline
max_deadline = 0

for job in jobs:
    if job[1] > max_deadline:
        max_deadline = job[1]

# Create slots
slots = [False] * max_deadline

# Store selected jobs
result = []

total_profit = 0

# Perform scheduling
for job in jobs:

    job_id = job[0]
    deadline = job[1]
    profit = job[2]

    # Find free slot before deadline
    for j in range(deadline - 1, -1, -1):

        if slots[j] == False:

            slots[j] = True
            result.append(job_id)
            total_profit += profit
            break

# Print result
print("Selected Jobs:", result)

print("Total Profit:", total_profit)
