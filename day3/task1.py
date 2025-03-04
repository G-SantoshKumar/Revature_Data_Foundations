numbers = list(range(1, 21))  
labels = ['A', 'B', 'C', 'D']  


sections = {num: labels[i % 4] for i, num in enumerate(numbers)}


for num, label in sections.items():
    print(f" {num}: {label}")
