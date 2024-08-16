import os
def parse_logfile(logfile_path, output_file):
    
    with open(logfile_path, 'r') as logfile, open(output_file, "w") as file:
        for line in logfile:
            stripped_line = line.strip()
            if stripped_line == "":
                file.write("\n")
            elif '=' in stripped_line:
                key, value = stripped_line.split('=', 1)
                key, value = key.strip(), value.strip()
                file.write(f"{key} = {value}\n")

        print(f"Data extracted from input file {logfile_path}")
        print(f"Data written to the output file {output_file}")
    
def main():
    logfile_path = "dummy_logfile.txt"
    if os.path.exists(logfile_path):
        print(f"The input file namely {logfile_path} exists")
    else:
        print("File does not exist")
    output_file = "generated.txt"
    parse_logfile(logfile_path, output_file)
    print("Parsing complete")

if __name__ == "__main__":
    main()





