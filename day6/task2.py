import math

def calculate_trig_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    
    return {
        "sin": sin_value,
        "cos": cos_value,
    }

angle = 30  
result = calculate_trig_values(angle)
print(result)

print(dir())

print(math.floor(-4.2))

print(math.ceil(-4.2))
print (round(math.sqrt(8), 2))
print(math.log(2))
print(math.gcd(5,8))