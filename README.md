# PC Stress Test Tool 🔥

A comprehensive, cross-platform stress testing utility with adjustable intensity levels to test your PC's performance under load.

## Features

- **Multi-Component Testing**: Stress test CPU, Memory, and Disk I/O
- **Adjustable Intensity**: 4 levels from light to extreme
- **Real-time Progress**: Visual progress bar and elapsed time display
- **Safe & Controllable**: Easy to stop with Ctrl+C, automatic cleanup
- **Color-coded Output**: Clear visual feedback during testing

## Installation

No installation required! Just make sure you have Python 3 installed:

```bash
python3 --version
```

Make the script executable (macOS/Linux):
```bash
chmod +x stress_test.py
```

## Usage

### Basic Usage

```bash
# Run with default settings (medium intensity, 60 seconds, all components)
python3 stress_test.py

# Or if you made it executable:
./stress_test.py
```

### With Options

```bash
# Light stress test for 30 seconds
python3 stress_test.py --intensity light --duration 30

# Heavy CPU stress test for 2 minutes
python3 stress_test.py --intensity heavy --duration 120 --components cpu

# Extreme stress test until manually stopped
python3 stress_test.py --intensity extreme --duration 0

# Memory stress only, medium intensity, 90 seconds
python3 stress_test.py -i medium -d 90 -c memory
```

## Options

### Intensity Levels

| Level | CPU Threads | CPU Load | Memory | Disk I/O | Use Case |
|-------|-------------|----------|---------|----------|----------|
| **light** | 25% of cores | 30% | 100 MB | Light | Quick test, background running |
| **medium** | 50% of cores | 60% | 500 MB | Moderate | General stress testing |
| **heavy** | All cores | 85% | 1.5 GB | Heavy | Performance testing |
| **extreme** | 2x cores | 100% | 3 GB | Intensive | Maximum stress, stability testing |

### Command-line Arguments

- `-i, --intensity`: Choose intensity level
  - Options: `light`, `medium`, `heavy`, `extreme`
  - Default: `medium`

- `-d, --duration`: Test duration in seconds
  - Range: 0 (infinite) to any positive number
  - Default: `60`
  - Use `0` for infinite duration (stop with Ctrl+C)

- `-c, --components`: Which components to stress test
  - Options: `cpu`, `memory`, `disk`, `all`
  - Default: `all`

### Examples

```bash
# Quick 30-second light test
python3 stress_test.py -i light -d 30

# 5-minute heavy stress on CPU only
python3 stress_test.py -i heavy -d 300 -c cpu

# Extreme test until you stop it
python3 stress_test.py -i extreme -d 0

# Test memory only with medium intensity
python3 stress_test.py -c memory
```

## What Each Component Tests

### CPU Stress
- Spawns multiple worker processes (based on intensity)
- Performs intensive mathematical calculations
- Uses multi-processing for true parallel execution
- Tests: sqrt, sin, cos, log operations in tight loops

### Memory Stress
- Allocates large blocks of memory
- Writes random data to ensure actual memory usage
- Keeps memory active with random access patterns
- Automatically cleans up when stopped

### Disk I/O Stress
- Performs repeated write and read operations
- Uses temporary files (auto-deleted on exit)
- Forces synchronization to disk (fsync)
- Tests sequential read/write performance

## Safety Features

1. **Graceful Shutdown**: Press `Ctrl+C` at any time to stop
2. **Automatic Cleanup**: Temp files and memory are always freed
3. **Progress Monitoring**: Real-time feedback on test status
4. **Configurable Intensity**: Start light to ensure system stability

## System Requirements

- **Python**: 3.6 or higher
- **Operating System**: 
  - macOS (tested)
  - Linux
  - Windows
- **Disk Space**: At least 1 GB free for extreme disk tests
- **Memory**: Varies by intensity (100 MB to 3 GB)

## Warning ⚠️

- **Extreme tests** can significantly heat up your system
- Ensure adequate cooling before running heavy/extreme tests
- Don't run extreme tests for extended periods without monitoring
- Close important applications before stress testing
- Monitor system temperature during testing

## Troubleshooting

### Script won't run
```bash
# Make sure Python 3 is installed
python3 --version

# Or try with just python
python stress_test.py
```

### Permission denied
```bash
# Make the script executable
chmod +x stress_test.py
```

### Out of memory
- Use a lower intensity level
- Test components individually
- Reduce duration

### System becomes unresponsive
- Start with `light` intensity first
- Test individual components before using `all`
- Reduce duration for extreme tests

## Tips for Best Results

1. **Start Light**: Begin with light intensity to see how your system handles it
2. **Monitor Temperature**: Use system monitoring tools to watch temperatures
3. **Individual Components**: Test CPU, memory, and disk separately first
4. **Cooling**: Ensure good ventilation and cooling
5. **Benchmarking**: Run multiple tests and compare results
6. **Stability Testing**: Use for extended periods to test system stability

## Example Output

```
============================================================
           PC STRESS TEST UTILITY
============================================================

Intensity Level: HEAVY
Components: ALL
Duration: 60 seconds
CPU Threads: 8
Start Time: 2025-10-12 14:30:00

WARNING: This will stress your system resources!
Press Ctrl+C to stop at any time.

============================================================

[CPU Worker 0] Started
[CPU Worker 1] Started
...
[MEMORY] Started - Allocating 1500 MB
[DISK I/O] Started - 100 operations

Progress: [████████████████░░░░░░░░] 65.5% | Elapsed: 39s | Remaining: 21s
```

## License

Free to use and modify. Use at your own risk.

## Support

If you encounter issues or have questions, check the troubleshooting section above or modify the script to suit your needs.

---

**Remember**: Stress testing is intended to verify system stability and performance. Always monitor your system and stop the test if anything seems wrong!

