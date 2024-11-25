import os

from helpers.constants import DATA_DIR

input_files = sorted([os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
                     if os.path.isfile(os.path.join(DATA_DIR, f)) and f.endswith('.txt')])

for file in input_files:
    with open(file) as f:
        filename = os.path.basename(file)
        line = f.readline()
        n, _, _ = map(int, line.strip().split())
        print(filename, n)