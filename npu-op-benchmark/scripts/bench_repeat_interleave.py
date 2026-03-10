#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
bench = Path(__file__).with_name('bench_op.py')
cmd = [sys.executable, str(bench), '--op', 'repeat_interleave', *sys.argv[1:]]
raise SystemExit(subprocess.call(cmd))
