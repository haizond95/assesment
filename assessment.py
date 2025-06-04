def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(100, 100, 100, 10))     # STANDARD
print(sort(200, 50, 50, 10))       # SPECIAL
print(sort(100, 100, 100, 25))     # SPECIAL
print(sort(200, 200, 200, 25))     # REJECTED
print(sort(149, 149, 149, 19.9))   # STANDARD
