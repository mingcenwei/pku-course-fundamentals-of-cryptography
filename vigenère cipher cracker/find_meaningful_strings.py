from nostril import nonsense

INPUT_FILENAME = "brute_force_results.txt"
OUTPUT_FILENAME = "meaningful_results.txt"

with open(INPUT_FILENAME) as input_file, open(OUTPUT_FILENAME, "w") as output_file:
    for line in input_file:
        if not nonsense(line):
            output_file.write(line)