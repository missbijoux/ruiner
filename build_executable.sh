#!/bin/bash
# Build script to create standalone executable

echo "=========================================="
echo "Building Stress Test Executable"
echo "=========================================="
echo ""

# Check if pyinstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
fi

echo "Building executable..."
pyinstaller --onefile \
    --name stress_test \
    --clean \
    --noconfirm \
    stress_test.py

echo ""
echo "=========================================="
echo "Build Complete!"
echo "=========================================="
echo ""
echo "The executable is located at:"
echo "  dist/stress_test"
echo ""
echo "To distribute to another computer:"
echo "  1. Copy the 'dist/stress_test' file"
echo "  2. Run it without needing Python!"
echo ""

