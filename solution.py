import argparse
import csv
import json

def parse_fixed_width_file(spec_file, input_file, output_file):
    # Load the spec from JSON
    with open(spec_file, 'r') as file:
        spec = json.load(file)
    
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))  # Convert offsets to integers
    include_header = spec["IncludeHeader"] == "True"
    fixed_width_encoding = spec["FixedWidthEncoding"]
    delimited_encoding = spec["DelimitedEncoding"]
    
    with open(input_file, 'r', encoding=fixed_width_encoding) as infile, open(output_file, 'w', encoding=delimited_encoding, newline='') as outfile:
        writer = csv.writer(outfile)
        
        if include_header:
            writer.writerow(column_names)

        for line in infile:
            row = []
            start = 0
            for width in offsets:
                end = start + width
                row.append(line[start:end].strip())
                start = end
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse a fixed width file.',
                                     usage='%(prog)s <spec_file> <input_file> <output_file>')
    parser.add_argument('spec_file', help='The specification file')
    parser.add_argument('input_file', help='The input file name')
    parser.add_argument('output_file', help='The output file name')
    args = parser.parse_args()
    
    parse_fixed_width_file(args.spec_file, args.input_file, args.output_file)