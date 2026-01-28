
from tabulate import tabulate
import numpy as np

x = np.linspace(0, (2 * np.pi), 1000)
y = np.sin(x)

table_data = [(a, b) for a, b in zip(x, y)]
table_headers = ["sin(x)","x"]
table = tabulate(table_data, tablefmt = "grid", headers = table_headers, floatfmt = ".3f")

def main():
	print(table)

if __name__ == "__main__":
	main()