
# Fixed Width File Parser

This program parses a fixed-width file based on a specification provided in a JSON file and outputs a CSV file.

## Usage

To use the program, run the following command in your terminal:

```bash
python3 solution.py <spec_file> <input_file> <output_file>
```

Replace `<spec_file>`, `<input_file>`, and `<output_file>` with the paths to your specification JSON file, input fixed-width file, and desired output CSV file, respectively.

For example:

```bash
python3 solution.py spec.json input.txt output.csv
```

## Testing

To run the test cases for this program, use the following command:

```bash
python3 -m unittest test_parser.py
```

This will run all the test cases defined in `test_parser.py` and display the results in your terminal.
