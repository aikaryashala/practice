# DOM Creation & Manipulation from Browser Console

This exercise demonstrates that **DOM is a live object model**, independent of initially written HTML. You will start with a **blank HTML file** and build everything using **DevTools Console**.

---

## 1. Create a Blank HTML File

On a **Windows machine**, open **Git Bash** (recommended, since it is already installed) and create a blank file using `touch`:

```bash
touch blank.html
```

Ensure the file has **no content at all**.

Open this file in the **Ulaa browser**.

### Open DevTools → Console

- **Windows**: `Ctrl + Shift + J`
- **macOS**: `Cmd + Option + J`

---

## 2. Observe the Existing DOM

> Useful shortcuts while working with DevTools:
>
> | Action                       | Windows            | macOS              |
> | ---------------------------- | ------------------ | ------------------ |
> | Open DevTools                | `Ctrl + Shift + I` | `Cmd + Option + I` |
> | Open Console directly        | `Ctrl + Shift + J` | `Cmd + Option + J` |
> | Switch to Elements panel     | `Ctrl + Shift + C` | `Cmd + Shift + C`  |
> | Run selected code in Console | `Enter`            | `Enter`            |

Even though the file is empty, the browser creates a DOM structure.

Run:

```js
document.documentElement
document.head
document.body
```

Expected structure:

```
html
├── head
└── body
```

---

## 3. Add a `<title>` to the Document

```js
const titleNode = document.createElement("title");
titleNode.textContent = "Create HTML using DOM";
document.head.appendChild(titleNode);
```

✔ Observe the browser tab title updating immediately.

---

## 4. Add a Heading (`<h1>`) to the Body

```js
const heading = document.createElement("h1");
heading.textContent = "Welcome to the developer world using Console";
document.body.appendChild(heading);
```

---

## 5. Add a Paragraph to the Body

```js
const para1 = document.createElement("p");
para1.textContent = "e para appendChild() use chesi add chesamu";
document.body.appendChild(para1);
```

---

## 6. Add One More Paragraph

```js
const para2 = document.createElement("p");
para2.textContent = "Idhi rendo paragraph... ela edhayina add cheyochu, manam veru veru websites lo choosevanni.";
document.body.appendChild(para2);
```

---

## 7. Remove the Earlier Paragraph

### Option A: Using `removeChild`

```js
document.body.removeChild(para1);
```

### Option B: Using `remove()` (modern)

```js
para1.remove();
```

✔ Only the second paragraph remains.

---

## 8. Inspect the Generated HTML

Run:

```js
document.documentElement.outerHTML
```

This HTML is **generated from the DOM**, not typed by you.

---

## 9. Key Learning Outcomes

- DOM exists even without HTML
- DOM nodes are **JavaScript objects**
- `appendChild()` **moves** nodes, it does not copy them
- HTML is just a serialization of the DOM

---

## 10. Mental Model

```
Console / JS
     ↓
   DOM Tree
     ↓
   Rendering
```

You have created a full webpage **without writing HTML**.

---

## 11. Serialize the DOM to Print the HTML Code

Serialization means **converting the live DOM back into HTML text**.

Run the following in the Console:

```js
document.documentElement.outerHTML
```

This prints the **entire HTML document** as a string.

### Optional: Pretty‑print using console.log

```js
console.log(document.documentElement.outerHTML);
```

### What to Observe

- This HTML was **not typed manually**
- It was **generated from the DOM tree**
- Browser can always convert: `DOM → HTML`

This confirms an important idea (in simple words):

> The browser works using the **DOM in memory**. HTML is just a **text version printed from the DOM** so humans can see it.

In other words:

- Browser **does not think in HTML text**
- Browser **thinks in DOM objects**
- HTML you see is just the **output of the DOM**

---

✅ This file is meant to be **executed step‑by‑step in the browser console**, not run as a script.

