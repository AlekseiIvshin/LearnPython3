import sys

try:
  for line in sys.stdin:
    print(line)
except KeyboardInterrupt:
  print("Good bye!")
