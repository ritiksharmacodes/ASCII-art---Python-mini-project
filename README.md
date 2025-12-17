# **ASCII Art Generator – Windows CLI Edition**

A fast, interactive **Windows-only** command-line application that generates **large ASCII art** for characters, words, numbers, and ranges using **multiple Figlet font styles**.

The app delivers a classic DOS-style experience with instant keypress navigation, vibrant color output, and dynamic font rendering powered by **pyfiglet**.

---

## 🚀 **Features**

* **Font selection menu** with 5 distinct ASCII styles:

  * Graffiti
  * Big
  * Epic
  * Modular
  * Electronic
* **Instant single-key navigation** using `msvcrt.getch()`
* **Color-rich output** via `colorama`
* Generate ASCII art for:

  * Single characters
  * Full words (up to 15 characters)
  * Alphabet ranges (e.g. `A-D`)
  * Alphabets-only input
  * Numbers-only input
* **Menu-driven UX** with fast screen refresh
* **Optimized for Windows Terminal / CMD**

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

* ASCII art is generated dynamically using **pyfiglet**
* Users select a font before accessing the main menu
* Input is validated based on the selected mode:

  * Length limits (max 15 characters)
  * Alphabet-only or number-only constraints
  * Proper range formatting (`A-D`)
* Output is rendered instantly using the selected font
* Screen transitions use `cls` for a clean CLI experience

---

## 🎨 **Available Fonts**

| Option | Font Name  |
| -----: | ---------- |
|      1 | Graffiti   |
|      2 | Big        |
|      3 | Epic       |
|      4 | Modular    |
|      5 | Electronic |

---

## 📘 **Example**

Input:

```
HELLO
```

Output (example – varies by font):

```
██╗  ██╗███████╗██╗     ██╗      ██████╗
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
```

---

## ⚠️ **Notes**

* **Windows-only** (uses `msvcrt` and `cls`)
* Maximum input length: **15 characters**
* Range input must follow strict format: `A-D`
* Fonts affect output width and alignment
