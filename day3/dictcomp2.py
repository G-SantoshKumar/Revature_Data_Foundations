students = [("Alice", 85), ("Bob", 92), ("Charlie", 67)]
myDict = {name: ('A' if score > 90 else 
                 'B' if 80 <= score <= 90 else 
                 'C' if 70 <= score < 80 else 
                 'F') 
          for name, score in students}
print(myDict)