import sys
from commands import process_command

args = sys.argv[1:]

if not args:
    print("Mini Dave waiting...")
else:
    cmd = args[0]
    process_command(cmd)
