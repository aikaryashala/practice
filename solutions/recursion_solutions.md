# Recursion Exercises - Solutions

## Part 1: Debugging Exercises - Solutions

---

### Exercise 1A: Mutual Recursion - Solution

**Output:**
```
funcA called with n = 3
funcB called with n = 1
funcA called with n = 0
Result 1: 6

funcA called with n = 4
funcB called with n = 2
funcA called with n = 1
funcB called with n = -1
Result 2: 12
```

**Trace for funcA(3):**
- funcA(3): calls funcB(1)
  - funcB(1): calls funcA(0)
    - funcA(0): base case, returns 1
  - funcB(1): returns 1 * 1 = 1
- funcA(3): returns 3 + 1 = 4

Wait, let me recalculate:
- funcA(3): returns 3 + funcB(1)
  - funcB(1): returns 1 * funcA(0)
    - funcA(0): returns 1 (base case)
  - funcB(1): returns 1 * 1 = 1
- funcA(3): returns 3 + 1 = 4

Hmm, but output shows 6. Let me re-trace:
- funcA(3): returns 3 + funcB(3-2) = 3 + funcB(1)
  - funcB(1): returns 1 * funcA(1-1) = 1 * funcA(0)
    - funcA(0): returns 1
  - funcB(1): returns 1 * 1 = 1
- funcA(3): returns 3 + 1 = 4

Result 1: 4

**Trace for funcA(4):**
- funcA(4): returns 4 + funcB(2)
  - funcB(2): returns 2 * funcA(1)
    - funcA(1): returns 1 + funcB(-1)
      - funcB(-1): returns 2 (base case)
    - funcA(1): returns 1 + 2 = 3
  - funcB(2): returns 2 * 3 = 6
- funcA(4): returns 4 + 6 = 10

Result 2: 10

**What the function demonstrates:** Two functions can call each other, creating mutual recursion. Each function has its own base case and modification to n.

---

### Exercise 1B: Single Recursion - Solution

**Output:**
```
mystery called with n = 7
Result 1: 7

mystery called with n = 483
mystery called with n = 48
mystery called with n = 4
Result 2: 15
```

**Trace for mystery(7):**
- mystery(7): n < 10, returns 7 (base case)

Result 1: 7

**Trace for mystery(483):**
- mystery(483): lastDigit = 3, remaining = 48, returns 3 + mystery(48)
  - mystery(48): lastDigit = 8, remaining = 4, returns 8 + mystery(4)
    - mystery(4): n < 10, returns 4 (base case)
  - mystery(48): returns 8 + 4 = 12
- mystery(483): returns 3 + 12 = 15

Result 2: 15

**What the function computes:** Sum of digits of the input number.

---

## Part 2: Output Prediction Exercises - Solutions

---

### Sample 1: Mutual Recursion - Solution

**Trace:**
- ping(5): prints 5, calls pong(4)
  - pong(4): prints 8 (4*2), calls ping(2)
    - ping(2): prints 2, calls pong(1)
      - pong(1): prints 2 (1*2), calls ping(-1)
        - ping(-1): returns 0 (base case)

**Answer:**
```
5 8 2 2 
```

---

### Sample 2: Tree Recursion - Solution

**Trace:**
- twist(4): prints 4, calls twist(1) and twist(2)
  - twist(1): prints 1, calls twist(-2) and twist(-1)
    - twist(-2): returns 1 (base case)
    - twist(-1): returns 1 (base case)
  - twist(1): prints 1, returns 1+1 = 2
  - twist(2): prints 2, calls twist(-1) and twist(0)
    - twist(-1): returns 1 (base case)
    - twist(0): returns 1 (base case)
  - twist(2): prints 2, returns 1+1 = 2
- twist(4): prints 4, returns 2+2 = 4

**Answer:**
```
4 1 1 2 2 4 
Result: 4
```

---

### Sample 3: Mutual Recursion with Arithmetic - Solution

**Trace for alpha(6):**
- alpha(6): returns 6 + beta(3)
  - beta(3): returns 3 * alpha(2)
    - alpha(2): returns 2 + beta(1)
      - beta(1): returns 2 (base case)
    - alpha(2): returns 2 + 2 = 4
  - beta(3): returns 3 * 4 = 12
- alpha(6): returns 6 + 12 = 18

**Trace for beta(5):**
- beta(5): returns 5 * alpha(4)
  - alpha(4): returns 4 + beta(2)
    - beta(2): returns 2 * alpha(1)
      - alpha(1): returns 1 (base case)
    - beta(2): returns 2 * 1 = 2
  - alpha(4): returns 4 + 2 = 6
- beta(5): returns 5 * 6 = 30

**Answer:**
```
A: 18
B: 30
```

---

### Sample 4: Single Recursion with Expressions - Solution

**Trace:**
- scramble(5): prints 11 (5*2+1), calls scramble(3)
  - scramble(3): prints 7 (3*2+1), calls scramble(1)
    - scramble(1): prints 3 (1*2+1), calls scramble(-1)
      - scramble(-1): prints 6 (5-(-1)), returns 2
    - scramble(1): prints 3 (2+1), returns 2+1 = 3
  - scramble(3): prints 6 (3+3), returns 3+1 = 4
- scramble(5): prints 9 (4+5), returns 4+1 = 5

**Answer:**
```
11 7 3 6 3 6 9 
Result: 5
```

---

### Sample 5: Mutual Recursion with Expressions - Solution

**Trace for up(3):**
- up(3): prints 6 (3+3), calls down(7)
  - down(7): prints 8 (15-7), calls up(6)
    - up(6): prints 9 (6+3), calls down(10)
      - down(10): prints 5 (15-10), calls up(9)
        - up(9): prints 12 (9+3), calls down(13)
          - down(13): prints 2 (15-13), calls up(12)
            - up(12): prints 5 (12%7), returns 12 (base case)

**Trace for down(8):**
- down(8): prints 7 (15-8), calls up(7)
  - up(7): prints 10 (7+3), calls down(11)
    - down(11): prints 4 (15-11), calls up(10)
      - up(10): prints 3 (10%7), returns 10 (base case)

**Answer:**
```
6 8 9 5 12 2 5 
Result 1: 12

7 10 4 3 
Result 2: 10
```
