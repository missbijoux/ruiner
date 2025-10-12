# Files Overview 📁

Here's what each file in this folder does:

## 🔥 Core Files

### `stress_test.py` ⭐
**The main stress test program**
- Run with: `python3 stress_test.py`
- This is the actual stress testing tool
- Size: ~10 KB
- Can be transferred alone if the other computer has Python

### `stress_test_portable.zip` ⭐⭐⭐
**READY TO TRANSFER - Use this!**
- Contains: stress_test.py + all documentation
- Size: ~20 KB
- Transfer via USB, email, cloud storage, AirDrop, etc.
- Works on Windows, Mac, and Linux
- Just unzip and run on the other computer

---

## 📚 Documentation Files

### `README.md`
Complete documentation with:
- Full usage instructions
- All command-line options
- Troubleshooting guide
- Safety warnings

### `QUICK_START.md`
Quick reference with common commands

### `TRANSFER_GUIDE.md`
How to move this to another computer (multiple methods)

### `FILES_OVERVIEW.md`
This file - explains what everything is

---

## 🔧 Build Tools (Optional)

### `build_executable.sh`
Script to create a standalone executable
- Run with: `./build_executable.sh`
- Creates an executable that doesn't need Python
- Output goes to `dist/stress_test`

### `requirements.txt`
Dependencies for building the executable
- Used by build_executable.sh

---

## 🎯 What You Need to Transfer

### Option A: Everything (Recommended)
**File**: `stress_test_portable.zip` (already created!)
- Includes program + all docs
- Easiest option

### Option B: Just the Program
**File**: `stress_test.py`
- Just the stress test tool
- Other computer needs Python
- Smallest transfer size

### Option C: Standalone Executable
**File**: `dist/stress_test` (after running build_executable.sh)
- No Python needed on other computer
- Larger file size but easier for end users
- Platform specific (Mac exe won't run on Windows)

---

## 📦 Current Folder Structure

```
Ruiner/
├── stress_test.py              ← Main program
├── stress_test_portable.zip    ← Transfer this! ⭐
├── README.md                   ← Documentation
├── QUICK_START.md              ← Quick reference
├── TRANSFER_GUIDE.md           ← How to transfer
├── FILES_OVERVIEW.md           ← This file
├── build_executable.sh         ← Build tool (optional)
└── requirements.txt            ← Dependencies (optional)
```

After building executable:
```
Ruiner/
├── ... (all above files)
├── dist/
│   └── stress_test            ← Standalone executable
└── build/                     ← Build artifacts (can delete)
```

---

## 🚀 Quick Actions

### To use locally:
```bash
python3 stress_test.py -i medium -d 60
```

### To transfer to another computer:
1. Take `stress_test_portable.zip`
2. Transfer via your preferred method
3. Unzip on other computer
4. Run: `python3 stress_test.py`

### To build standalone executable:
```bash
./build_executable.sh
# Then transfer: dist/stress_test
```

---

## 💾 File Sizes

- `stress_test.py`: ~10 KB
- `stress_test_portable.zip`: ~20 KB
- `dist/stress_test` (executable): ~10-20 MB
- All documentation: ~15 KB total

---

**Bottom Line**: Grab the `stress_test_portable.zip` file and you're good to go! 🎉

