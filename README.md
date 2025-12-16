# **ASCII Art Generator – Windows CLI Edition**

A fast, interactive **Windows-only** CLI tool that displays **large ASCII art** for letters, numbers, words, symbols, and even alphabet ranges.
Built using internally defined ASCII character patterns, instant keypress navigation, and vibrant **color-themed output** using `colorama`.

This mini project recreates the feel of classic DOS-style interfaces—clean, snappy, and visually bold.

---

## 🚀 **Features**

* **Instant single-key navigation** using `msvcrt.getch()`
* **Colorful output** powered by Colorama
* Generate ASCII art for:

  * Single Characters
  * Full Words (A–Z, 0–9, symbols)
  * Alphabet Ranges (e.g., `A-D`)
  * Alphabets-only Mode
  * Numbers-only Mode
* **Optimized for Windows Terminal / CMD**
* **Menu-driven UX** with quick screen transitions

---

## 📦 **Installation**

### 1. Create & Activate Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```
pip install colorama pyfiglet
```

---

## ▶️ **Run the Program**

```
python main.py
```

---

## 🖥 **How It Works**

* The script stores all ASCII patterns in 5 structured rows.
* Each character is mapped using fixed-width slicing.
* Coloring is done row-by-row to preserve the ASCII structure.
* For each input:

  * The correct pattern segment is extracted
  * Characters are printed side-by-side to form large ASCII text

---

## 📘 **Example**

Input:

```
A
```

Output:

```
 *** 
*   *
*****
*   *
*   *
```

---

## ⚠️ **Notes**

* This tool is **Windows-only** due to `msvcrt.getch()` and `cls`.
* Max input length for words: **15 characters**
* Ranges must follow the format: `A-D`
