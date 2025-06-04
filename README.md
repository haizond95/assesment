# Package Classification Function

This repository contains a Python function to classify packages based on their **volume** and **mass**. The classification follows these rules:

### Classification Rules

- A package is **bulky** if:
  - Its volume (Width × Height × Length) is **≥ 1,000,000 cm³**, or
  - Any one of its dimensions is **≥ 150 cm**
- A package is **heavy** if:
  - Its mass is **≥ 20 kg**

### Return Categories

- `"REJECTED"`: If the package is both bulky **and** heavy
- `"SPECIAL"`: If the package is either bulky **or** heavy (but not both)
- `"STANDARD"`: If the package is neither bulky nor heavy

---

### Example 

```python
print(sort(100, 100, 100, 10))     # STANDARD
print(sort(200, 50, 50, 10))       # SPECIAL
print(sort(100, 100, 100, 25))     # SPECIAL
print(sort(200, 200, 200, 25))     # REJECTED
print(sort(149, 149, 149, 19.9))   # STANDARD

---

### Author

This solution was completed as part of a technical interview assessment.
