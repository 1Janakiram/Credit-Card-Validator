# 💳 Credit Card Validator – Python Implementation

A Python program to **validate credit card numbers** using **Luhn’s Algorithm**, and identify the card type – **Visa**, **MasterCard**, or **American Express**.

---

## 📚 Problem Description

Credit card numbers are structured sequences, not just random digits. Each card number includes:
- **Prefix rules** that help identify the card issuer.
- A **checksum digit**, computed using **Luhn’s Algorithm**, to verify its validity.

This project simulates the same algorithm used by payment systems to detect errors in card numbers.

---

## 🧠 Luhn’s Algorithm – Explained

To determine if a card number is valid:

1. Starting from the **second-to-last digit**, multiply **every other digit by 2**.
2. If the result of the multiplication is greater than 9, **add the digits** of the result (e.g., `12 → 1 + 2 = 3`).
3. Add these results to the sum of digits **not multiplied by 2**.
4. If the total **modulo 10 equals 0**, the number is considered **valid**.

> ✅ Example:
> ```
> Number: 4003600000000014
> Doubled digits: 1•2, 0•2, 0•2, ..., 6•2, 0•2, 4•2 → 2 + 0 + ... + 12 + 0 + 8
> Sum of digits: 2 + 0 + ... + 1 + 2 + 0 + 8 = 13
> Sum of undoubled digits: 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 7
> Total: 13 + 7 = 20 → **Valid**
> ```

---

## 🔍 Card Type Detection

| Card Type       | Prefix        | Length     |
|-----------------|---------------|------------|
| American Express| 34, 37        | 15 digits  |
| MasterCard      | 51–55         | 16 digits  |
| Visa            | 4             | 13 or 16   |

---


## 🖥 Sample Usage

```bash
$ python3 credit.py
Number: 378282246310005
AMEX

$ python3 credit.py
Number: 5105105105105100
MASTERCARD

$ python3 credit.py
Number: 1234567890123456
INVALID
```
---

## 💡 Possible Improvements

- 🔢 Accept card numbers via command-line args or file  
- 🌐 Build a web version using Flask or Django  
- 🛠 Refactor to a CLI tool using `argparse`  
- 🧪 Integrate GitHub Actions for CI  
- 📦 Package and upload to PyPI  

---

## 📃 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Janakiram Chilukuri**  
Feel free to connect with me on [GitHub](https://github.com/<your-username>)!




