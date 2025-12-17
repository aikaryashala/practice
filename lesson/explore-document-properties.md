# Exploring HTML using `document` Properties (Console Exercise)

This exercise helps you understand **basic HTML tags** by exploring
**ready-made `document.*` properties** from the browser Console.

You will **NOT write JavaScript in the HTML file**.
You will only **observe and query** the DOM.

---

## 0. Download the HTML file

Download `explore_document_properties.html` file to your computer.

## 1. Open the HTML File

Open `explore-document-properties.html` in the **Ulaa browser**.

Open **DevTools → Console**:

- **Windows**: `Ctrl + Shift + J`
- **macOS**: `Cmd + Option + J`

---

## 2. Page-Level Information

```js
document.title
document.URL
document.documentURI
document.domain
```

---

## 3. Exploring Links (`<a>` tags)

```js
document.links
document.links.length

document.links[0].textContent
document.links[0].href

document.links[1].textContent
document.links[1].href
```

---

## 4. Exploring Images (`<img>` tags)

```js
document.images
document.images.length

document.images[0].src
document.images[1].src
```

---

## 5. Exploring Forms (`<form>` tags)

```js
document.forms
document.forms.length

document.forms[0]
document.forms[0].elements

document.forms[1]
document.forms[1].elements
```

---

## 6. Document Structure

```js
document.head
document.body
document.documentElement
```

---

## 7. Key Takeaway

- HTML tags become **objects**
- Same tags form **collections**
- Browser gives **shortcuts** for common elements

✅ Stop here. No DOM modification yet.
