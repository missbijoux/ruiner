#!/usr/bin/env python3
"""
PC Stress Test Tool
A comprehensive stress testing utility with adjustable intensity levels
"""

import os
import sys
import time
import multiprocessing
import threading
import argparse
import random
import math
from datetime import datetime, timedelta

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

class StressTest:
    def __init__(self, intensity='medium', duration=60, components='all'):
        """
        Initialize stress test
        
        Args:
            intensity: 'light', 'medium', 'heavy', 'extreme'
            duration: Test duration in seconds (0 = infinite)
            components: 'cpu', 'memory', 'disk', 'all'
        """
        self.intensity = intensity
        self.duration = duration
        self.components = components
        self.running = True
        self.start_time = None
        
        # Configure intensity parameters
        self.config = self._get_intensity_config()
        
    def _get_intensity_config(self):
        """Get configuration based on intensity level"""
        cpu_count = multiprocessing.cpu_count()
        
        configs = {
            'light': {
                'cpu_threads': max(1, cpu_count // 4),
                'cpu_load': 0.3,
                'memory_mb': 100,
                'disk_mb': 50,
                'disk_operations': 10
            },
            'medium': {
                'cpu_threads': max(1, cpu_count // 2),
                'cpu_load': 0.6,
                'memory_mb': 500,
                'disk_mb': 200,
                'disk_operations': 50
            },
            'heavy': {
                'cpu_threads': cpu_count,
                'cpu_load': 0.85,
                'memory_mb': 1500,
                'disk_mb': 500,
                'disk_operations': 100
            },
            'extreme': {
                'cpu_threads': cpu_count * 2,
                'cpu_load': 1.0,
                'memory_mb': 3000,
                'disk_mb': 1000,
                'disk_operations': 200
            }
        }
        
        return configs.get(self.intensity, configs['medium'])
    
    def print_header(self):
        """Print stress test header"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}           PC STRESS TEST UTILITY{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.END}\n")
        
        print(f"{Colors.YELLOW}Intensity Level:{Colors.END} {Colors.BOLD}{self.intensity.upper()}{Colors.END}")
        print(f"{Colors.YELLOW}Components:{Colors.END} {self.components.upper()}")
        print(f"{Colors.YELLOW}Duration:{Colors.END} {'Infinite (Ctrl+C to stop)' if self.duration == 0 else f'{self.duration} seconds'}")
        print(f"{Colors.YELLOW}CPU Threads:{Colors.END} {self.config['cpu_threads']}")
        print(f"{Colors.YELLOW}Start Time:{Colors.END} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"{Colors.RED}{Colors.BOLD}WARNING:{Colors.END} {Colors.RED}This will stress your system resources!{Colors.END}")
        print(f"{Colors.RED}Press Ctrl+C to stop at any time.{Colors.END}\n")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}\n")
    
    def cpu_stress(self, worker_id):
        """CPU stress test - performs intensive calculations"""
        print(f"{Colors.GREEN}[CPU Worker {worker_id}]{Colors.END} Started")
        
        while self.running:
            # Perform computationally expensive operations
            for _ in range(10000):
                if not self.running:
                    break
                # Mathematical operations
                result = math.sqrt(random.random() ** 2)
                result = math.sin(result) * math.cos(result)
                result = math.log(abs(result) + 1)
                
            # Add small delay based on cpu_load to control intensity
            if self.config['cpu_load'] < 1.0:
                time.sleep(0.01 * (1 - self.config['cpu_load']))
        
        print(f"{Colors.GREEN}[CPU Worker {worker_id}]{Colors.END} Stopped")
    
    def memory_stress(self):
        """Memory stress test - allocates and uses memory"""
        print(f"{Colors.BLUE}[MEMORY]{Colors.END} Started - Allocating {self.config['memory_mb']} MB")
        
        memory_blocks = []
        chunk_size = 1024 * 1024  # 1 MB chunks
        
        try:
            # Allocate memory
            for i in range(self.config['memory_mb']):
                if not self.running:
                    break
                # Allocate and fill memory
                block = bytearray(chunk_size)
                # Write data to ensure it's actually allocated
                for j in range(0, chunk_size, 4096):
                    block[j] = random.randint(0, 255)
                memory_blocks.append(block)
            
            print(f"{Colors.BLUE}[MEMORY]{Colors.END} Allocated {len(memory_blocks)} MB")
            
            # Keep memory allocated and occasionally access it
            while self.running:
                if memory_blocks:
                    # Randomly access memory to keep it active
                    block_idx = random.randint(0, len(memory_blocks) - 1)
                    pos = random.randint(0, chunk_size - 1)
                    memory_blocks[block_idx][pos] = random.randint(0, 255)
                time.sleep(0.1)
        
        except MemoryError:
            print(f"{Colors.RED}[MEMORY]{Colors.END} Memory allocation limit reached")
        
        finally:
            # Cleanup
            memory_blocks.clear()
            print(f"{Colors.BLUE}[MEMORY]{Colors.END} Stopped - Memory freed")
    
    def disk_stress(self):
        """Disk I/O stress test - reads and writes files"""
        temp_file = '/tmp/stress_test_temp.dat' if sys.platform != 'win32' else 'stress_test_temp.dat'
        
        print(f"{Colors.CYAN}[DISK I/O]{Colors.END} Started - {self.config['disk_operations']} operations")
        
        try:
            chunk_size = 1024 * 1024  # 1 MB
            
            while self.running:
                # Write test
                with open(temp_file, 'wb') as f:
                    for _ in range(self.config['disk_mb']):
                        if not self.running:
                            break
                        data = os.urandom(chunk_size)
                        f.write(data)
                        f.flush()
                        os.fsync(f.fileno())
                
                # Read test
                if self.running and os.path.exists(temp_file):
                    with open(temp_file, 'rb') as f:
                        while self.running:
                            chunk = f.read(chunk_size)
                            if not chunk:
                                break
                
                # Small delay between cycles
                time.sleep(0.5)
        
        except Exception as e:
            print(f"{Colors.RED}[DISK I/O]{Colors.END} Error: {e}")
        
        finally:
            # Cleanup temp file
            if os.path.exists(temp_file):
                os.remove(temp_file)
            print(f"{Colors.CYAN}[DISK I/O]{Colors.END} Stopped - Temp files cleaned")
    
    def monitor_progress(self):
        """Monitor and display progress"""
        self.start_time = datetime.now()
        
        while self.running:
            elapsed = (datetime.now() - self.start_time).total_seconds()
            
            if self.duration > 0:
                remaining = self.duration - elapsed
                if remaining <= 0:
                    self.running = False
                    break
                
                progress = (elapsed / self.duration) * 100
                bar_length = 40
                filled = int(bar_length * progress / 100)
                bar = '█' * filled + '░' * (bar_length - filled)
                
                print(f"\r{Colors.YELLOW}Progress:{Colors.END} [{bar}] {progress:.1f}% | "
                      f"{Colors.YELLOW}Elapsed:{Colors.END} {int(elapsed)}s | "
                      f"{Colors.YELLOW}Remaining:{Colors.END} {int(remaining)}s", end='', flush=True)
            else:
                # Infinite duration
                print(f"\r{Colors.YELLOW}Elapsed:{Colors.END} {int(elapsed)}s | "
                      f"{Colors.YELLOW}Status:{Colors.END} Running... (Ctrl+C to stop)", end='', flush=True)
            
            time.sleep(1)
        
        print()  # New line after progress bar
    
    def run(self):
        """Start the stress test"""
        self.print_header()
        
        threads = []
        processes = []
        
        try:
            # Start monitor thread
            monitor_thread = threading.Thread(target=self.monitor_progress)
            monitor_thread.daemon = True
            monitor_thread.start()
            
            # Start CPU stress (multi-process for true parallel execution)
            if self.components in ['cpu', 'all']:
                for i in range(self.config['cpu_threads']):
                    p = multiprocessing.Process(target=self.cpu_stress, args=(i,))
                    p.start()
                    processes.append(p)
            
            # Start Memory stress
            if self.components in ['memory', 'all']:
                mem_thread = threading.Thread(target=self.memory_stress)
                mem_thread.start()
                threads.append(mem_thread)
            
            # Start Disk stress
            if self.components in ['disk', 'all']:
                disk_thread = threading.Thread(target=self.disk_stress)
                disk_thread.start()
                threads.append(disk_thread)
            
            # Wait for completion or interruption
            monitor_thread.join()
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Interrupt received - stopping stress test...{Colors.END}")
        
        finally:
            # Stop all workers
            self.running = False
            
            # Wait for threads to finish
            for thread in threads:
                thread.join(timeout=5)
            
            # Terminate processes
            for process in processes:
                process.terminate()
                process.join(timeout=5)
            
            elapsed = (datetime.now() - self.start_time).total_seconds()
            print(f"\n{Colors.GREEN}{Colors.BOLD}Stress test completed!{Colors.END}")
            print(f"{Colors.GREEN}Total runtime: {elapsed:.1f} seconds{Colors.END}\n")


def main():
    parser = argparse.ArgumentParser(
        description='PC Stress Test Tool - Test your system under load',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --intensity light --duration 30
  %(prog)s --intensity extreme --duration 120 --components cpu
  %(prog)s --intensity medium --duration 0 --components all
  %(prog)s -i heavy -d 60 -c memory

Intensity Levels:
  light    - Minimal load, good for testing
  medium   - Moderate load (default)
  heavy    - High load, significant stress
  extreme  - Maximum load, use with caution!

Components:
  cpu      - CPU stress only
  memory   - Memory stress only
  disk     - Disk I/O stress only
  all      - All components (default)
        """
    )
    
    parser.add_argument(
        '-i', '--intensity',
        choices=['light', 'medium', 'heavy', 'extreme'],
        default='medium',
        help='Stress test intensity level (default: medium)'
    )
    
    parser.add_argument(
        '-d', '--duration',
        type=int,
        default=60,
        help='Duration in seconds (0 = infinite, default: 60)'
    )
    
    parser.add_argument(
        '-c', '--components',
        choices=['cpu', 'memory', 'disk', 'all'],
        default='all',
        help='Components to stress test (default: all)'
    )
    
    args = parser.parse_args()
    
    # Create and run stress test
    stress_test = StressTest(
        intensity=args.intensity,
        duration=args.duration,
        components=args.components
    )
    
    stress_test.run()


if __name__ == '__main__':
    multiprocessing.freeze_support()  # For Windows compatibility
    main()

