# Templates, Holes, and Data Binding

> **How to use this file**
>
> 1. Read this file end-to-end once.
> 2. Do NOT try to understand everything deeply.
> 3. Later, once I explain each example line by line.
> 4. You can understand and do everything in this file
>
> **Main idea:**  
> One idea appears everywhere:
>
> **Template + Data → Result**

---

## 1. Python Strings Have Holes

Start with plain Python strings.

```python
template = "Flight from {} to {} takes {} minutes"
print(template.format("Visakhapatnam", "Vijayawada", 65))
```

Think of `{}` as **holes**.

---

## 2. Same Template, Different Data

```python
template = "Flight from {} to {} takes {} minutes"

print(template.format("Srikakulam", "Chennai", 90))
print(template.format("Vizianagaram", "Bengaluru", 85))
```

Notice:
- Template stays the same
- Only the values change

---

## 3. Positional Indexes

You can number the holes.

```python
template = "Origin: {0}, Destination: {1}, Duration: {2} mins"
print(template.format("Visakhapatnam", "Vijayawada", 65))
```

Indexes control *which value goes where*.

---

## 4. Using the Same Argument Multiple Times

```python
template = "{0} → {1}. {0} is the origin."
print(template.format("Visakhapatnam", "Vijayawada"))
```

The same value can fill **multiple holes**.

---

## 5. Keyword Arguments (Named Holes)

```python
template = "Origin: {origin}, Destination: {destination}, Duration: {duration} mins"

print(template.format(
    origin="Visakhapatnam",
    destination="Vijayawada",
    duration=65
))
```

Named holes:
- Are easier to read
- Are safer for large templates

---

## 6. Repeating Named Holes

```python
template = "{origin} → {destination}. Flight starts at {origin}."

print(template.format(
    origin="Vizianagaram",
    destination="Bengaluru"
))
```

Same name, same value, many times.

---

## 7. HTML Is Just a String

HTML is also plain text.

```python
html = "<p>Flight from {} to {}</p>"
print(html.format("Visakhapatnam", "Vijayawada"))
```

Nothing new yet — same idea.

---

## 8. HTML with Multiple Holes

```python
html = """
<h2>Flight Details</h2>
<p>Origin: {origin}</p>
<p>Destination: {destination}</p>
<p>Duration: {duration} minutes</p>
<p>{origin} → {destination}</p>
"""

print(html.format(
    origin="Visakhapatnam",
    destination="Vijayawada",
    duration=65
))
```

Same data appears multiple times.

---

## 9. Imagine Data Comes from a Database

```python
origin = "Srikakulam"
destination = "Chennai"
duration = 90

html = "<p>{} → {} ({} mins)</p>"
print(html.format(origin, destination, duration))
```

Where data comes from does **not** matter.

---

## 10. SQL Queries Also Have Holes

```python
cursor.execute(
    "INSERT INTO flights (origin, destination, duration) VALUES (?, ?, ?)",
    ("Visakhapatnam", "Vijayawada", 65)
)
```

`?` are **holes** for values.

---

## 11. Same SQL Template, Different Values

```python
cursor.execute(
    "INSERT INTO flights (origin, destination, duration) VALUES (?, ?, ?)",
    ("Vizianagaram", "Bengaluru", 85)
)
```

Again:
- Structure stays the same
- Values change

---

## 12. SQL with Conditions

```python
cursor.execute(
    "SELECT * FROM flights WHERE origin = ?",
    ("Visakhapatnam",)
)
```

```python
cursor.execute(
    "SELECT * FROM flights WHERE duration > ?",
    (80,)
)
```

Holes are filled later.

---

## 13. One Pattern Everywhere

```python
# Python
"{} → {}".format(origin, destination)

# SQL
"WHERE origin = ?"
```

Different tools, same idea.

---

## 14. Key Idea to Remember

> **Structure stays fixed**  
> **Data changes**  
> **Engine fills the holes**

---

# 🧪 Lab Exercises (Write the Output)

> **Instructions**
> - Do NOT run the code
> - Write the output by hand
> - Focus on how values fill holes

---

### Exercise 1

```python
template = "{} → {}"
print(template.format("Visakhapatnam", "Vijayawada"))
```

**Output:**  
____________________________

---

### Exercise 2 (Same value used twice)

```python
template = "{0} to {1}. {0} is the origin."
print(template.format("Srikakulam", "Chennai"))
```

**Output:**  
____________________________

---

### Exercise 3 (Named holes)

```python
template = "{origin} → {destination} ({origin})"
print(template.format(
    origin="Vizianagaram",
    destination="Bengaluru"
))
```

**Output:**  
____________________________

---

### Exercise 4 (HTML string)

```python
html = "<p>{origin} to {destination}</p>"
print(html.format(
    origin="Visakhapatnam",
    destination="Vijayawada"
))
```

**Output:**  
____________________________

---

### Exercise 5 (Multiple repetition)

```python
template = "{city} → {city} → {city}"
print(template.format(city="Visakhapatnam"))
```

**Output:**  
____________________________

---

### Exercise 6 (SQL – identify holes)

```sql
INSERT INTO flights (origin, destination, duration)
VALUES (?, ?, ?);
```

**Question:**  
How many holes are present?  
____________________________

---

### Exercise 7 (Concept check)

Fill in the blanks:

```
Template + ________ → Result
```

---

## End Note

This file is **only for pattern recognition**.

Explanation, rules, and reasons will come **after** you are comfortable with the examples.
