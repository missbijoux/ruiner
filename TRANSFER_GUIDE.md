# Transfer Guide 📤

How to use the stress test on another computer - multiple options!

## ✅ Option 1: Use the Pre-Made Zip File (EASIEST)

**I already created this for you!** → `stress_test_portable.zip`

### On This Computer:
1. Find the file: `stress_test_portable.zip` in the Ruiner folder
2. Transfer it via:
   - 💾 **USB Drive**: Copy to USB, plug into other computer
   - ☁️ **Email/Cloud**: Email it or upload to Google Drive/Dropbox/iCloud
   - 🌐 **AirDrop**: If it's another Mac nearby
   - 💬 **Messaging**: Send via Slack, Discord, Messages, etc.

### On the Other Computer:
1. Unzip the file
2. Open Terminal (Mac/Linux) or Command Prompt (Windows)
3. Navigate to the folder: `cd path/to/unzipped/folder`
4. Run: `python3 stress_test.py --help`

**Requirements**: Python 3 must be installed (most Mac/Linux have it by default)

---

## 🚀 Option 2: Create Standalone Executable (NO PYTHON NEEDED!)

**Best for**: Computers without Python, non-technical users, Windows computers

### Step 1: Build the Executable (On This Computer)

```bash
cd "/Users/bijoux/Documents/Coding Projects/Ruiner"
./build_executable.sh
```

This will create a standalone executable at: `dist/stress_test`

### Step 2: Transfer the Executable

The executable is in the `dist/` folder. Transfer just that one file!

- **Mac → Mac**: Transfer `dist/stress_test` (works immediately)
- **Mac → Linux**: Transfer `dist/stress_test` (works immediately)
- **Mac → Windows**: You'll need to build on Windows or use Option 1

### Step 3: Run on Other Computer

```bash
# Mac/Linux - might need to make it executable first
chmod +x stress_test
./stress_test --help

# Then run tests
./stress_test -i medium -d 60
```

**Advantages**:
- ✅ No Python installation needed
- ✅ Single file to transfer
- ✅ Faster startup
- ✅ More professional

**Disadvantages**:
- ❌ Larger file size (~10-20 MB vs 10 KB)
- ❌ Platform-specific (Mac exe won't run on Windows)

---

## 📝 Option 3: Copy Just the Python Script

**Best for**: Quick testing, developers, when size matters

### Copy this single file:
```
stress_test.py
```

### On the other computer:
```bash
python3 stress_test.py --help
```

That's it! Super simple.

---

## 🌐 Option 4: Host on GitHub (For Multiple Computers)

If you want to share with many computers or keep it updated:

```bash
cd "/Users/bijoux/Documents/Coding Projects/Ruiner"
git init
git add stress_test.py README.md QUICK_START.md
git commit -m "Initial commit"
# Then push to GitHub
```

On other computers:
```bash
git clone your-repo-url
cd repo-name
python3 stress_test.py
```

---

## 🖥️ Platform-Specific Notes

### Windows Computer (From Mac)

**Method A - Use Python Script**:
1. Transfer `stress_test_portable.zip`
2. Ensure Python is installed (download from python.org)
3. Open Command Prompt or PowerShell
4. Run: `python stress_test.py -i medium -d 60`

**Method B - Build Windows Executable**:
You need to build on Windows itself:
1. Transfer `stress_test.py` to Windows computer
2. Install PyInstaller: `pip install pyinstaller`
3. Build: `pyinstaller --onefile stress_test.py`
4. Use the `dist/stress_test.exe` file

### Mac Computer (From Mac)

Use any option! The standalone executable works perfectly.

### Linux Computer (From Mac)

The Python script works best. The Mac executable might work but not guaranteed.

---

## 📦 File Size Comparison

| Method | File Size | Python Required? |
|--------|-----------|------------------|
| Python Script | ~10 KB | Yes (3.6+) |
| Zip Package | ~20 KB | Yes (3.6+) |
| Standalone Exe | ~10-20 MB | No |

---

## 🔒 Security Note

When transferring executables:
- Some antivirus software may flag stress testing tools
- The Python script is more transparent (readable source code)
- Build executables yourself rather than downloading pre-built ones

---

## ⚡ Quick Recommendation

**For most users**: Use **Option 1** (the zip file I created)
- It's ready to go
- Small file size
- Works on all platforms
- Source code is visible and editable

**For non-technical users**: Use **Option 2** (standalone executable)
- No Python needed
- Just double-click to run
- More professional

---

## 🆘 Troubleshooting Transfer Issues

### "Python not found" on other computer
→ Install Python from python.org (Windows) or use Homebrew (Mac)

### "Permission denied"
→ Run: `chmod +x stress_test.py`

### Executable won't run on other Mac
→ Run: `xattr -d com.apple.quarantine stress_test`
→ Or: System Preferences → Security → Allow

### Windows says "Unrecognized app"
→ Click "More info" → "Run anyway"
→ Or use the Python script instead

---

## 💡 My Recommendation

**Use the `stress_test_portable.zip` file I just created for you!**

It's sitting in your Ruiner folder right now, ready to transfer. It includes:
- ✅ The stress test script
- ✅ Full README documentation
- ✅ Quick start guide
- ✅ Works on Windows, Mac, and Linux
- ✅ Small file size (under 25 KB)

Just transfer that one zip file and unzip it on the other computer! 🎉

