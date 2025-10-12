# Quick Start Guide 🚀

## Run Your First Test (30 seconds)

```bash
cd "/Users/bijoux/Documents/Coding Projects/Ruiner"
python3 stress_test.py --intensity light --duration 30
```

## Common Commands

### 1. Light Test (Safe for First Time)
```bash
python3 stress_test.py -i light -d 60
```
Perfect for: First-time testing, running in background

### 2. Medium Test (Balanced)
```bash
python3 stress_test.py -i medium -d 120
```
Perfect for: General stress testing, daily testing

### 3. Heavy Test (Intense)
```bash
python3 stress_test.py -i heavy -d 180
```
Perfect for: Performance testing, system validation

### 4. Extreme Test (Maximum)
```bash
python3 stress_test.py -i extreme -d 60
```
Perfect for: Stability testing, finding limits (⚠️ Use with caution!)

## Test Specific Components

### CPU Only
```bash
python3 stress_test.py -i heavy -d 120 -c cpu
```

### Memory Only
```bash
python3 stress_test.py -i medium -d 60 -c memory
```

### Disk Only
```bash
python3 stress_test.py -i medium -d 90 -c disk
```

## Stop Anytime

Press `Ctrl + C` to stop the test immediately!

## View All Options

```bash
python3 stress_test.py --help
```

---

**Tip**: Start with light intensity and work your way up! 💡

