import sys
import glob
from hashlib import sha256
import matplotlib.pyplot as plt

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        with open(fn, "rb") as file:
            for line_bytes in file:
                hash_code = sha256(line_bytes).hexdigest()
                if fn not in groups:
                    groups[fn] = set()
                groups[fn].add(hash_code)
    return groups

if __name__ == "__main__":
    args = sys.argv[1:]
    filenames = []
    for arg in args:
        matches = glob.glob(arg)
        filenames.extend(matches if matches else [arg])
    groups = find_groups(filenames)
    for filename, values in groups.items():
        int_conversions = []
        for hex_code in list(values):
            int_convert = int(hex_code[:8], 16)
            int_conversions.append(int_convert)
        plt.hist(int_conversions, bins=20, edgecolor='black', color='skyblue')
        plt.xlabel('Hash')
        plt.ylabel('Count')
        plt.title('Hashing Distribution')
        plt.show()
    