# 🏷️ PESEL Verifier

![Project Status](https://img.shields.io/badge/status-completed-brightgreen)

A Python program to verify the correctness of **PESEL (Polish National Identification Number)**. It checks the length, digits, date validity, and checksum of PESEL numbers.

## 📸 Preview
This script reads PESEL numbers from a file (`1e6.dat`), validates them, and provides statistical results about valid and invalid PESELs.

## 🛠️ Technologies Used
- **Python** – Core programming language used.

## 🚀 Features
- Checks if the PESEL contains only digits.
- Validates the PESEL length (11 characters).
- Verifies the encoded birth date for correctness.
- Computes and validates the PESEL checksum.
- Distinguishes between male and female PESELs.

## 📦 Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Retr0647/PESEL-verification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PESEL-verification
   ```
3. Place your PESEL data file (`1e6.dat`) in the project directory.
4. Run the script:
   ```bash
   python PESEL.py
   ```

## 📄 Documentation
Detailed documentation of all functions and validation steps can be found in the **`docs/`** folder.

## 🎯 Usage 
To use the program simply run it on your device. You can also change the interpreted file for `1e6_2.dat` to 
see different outcomes or for `1e3.dat` which has a smaller number of PESEL numbers so it will be easier to verify.

## 📜 License
This project is open-source and available under the **MIT License**.

## 📞 Contact
For any questions, feel free to reach out via [GitHub Issues](https://github.com/Retr0647/PESEL-verification/issues).
