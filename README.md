# OS Break Simulator

⚠️ **WARNING: This code modifies Windows system files and can break your OS. Run only in an isolated VM.** ⚠️

## What it does

This project demonstrates how malicious code can manipulate Windows file permissions and attempt to delete system files. It disguises itself as a harmless number guessing game, but triggers destructive actions on wrong guesses.

## How it works

1. Takes ownership of C:\Windows\System32 using `takeown`
2. Grants full control permissions using `icacls`
3. Attempts to delete all files in System32
4. Wrapped in a deceptive number guessing game interface

## Educational purposes only

This code is for understanding:

- Windows permission structures
- File system security
- Social engineering techniques
- The importance of running trusted code

## Requirements

- Windows OS
- Administrator privileges
- Virtual machine (strongly recommended)

## Usage

```bash
python os_break.py
```

## Disclaimer

The author is not responsible for damaged systems. This is for educational security research only.
