import os

def merge_sect(parsed_groups):
    # Define group mappings
    groups = {
        'group1': {'gpu', 'machine_name', 'design_size'},
        'group2': {'high_curvature_internal_checking_count', 'mrc_area_count'},
        'group3': {'mean_fermi'},
        'group4': {'target_prep_runtime'}
    }
    
    # Initialize result dictionary
    result_dict = {group: [] for group in groups}
    
    # Process parsed_groups
    for item in parsed_groups:
        lines = item.split('\n')
        if not lines:
            continue

        first_line = lines[0]
        key = first_line.split(' = ', 1)[0]
        remaining_lines = '\n'.join(lines[1:])
        
        # Append to the appropriate group
        for group, keys in groups.items():
            if key in keys:
                result_dict[group].append(first_line + '\n' + remaining_lines)
                break
    
    # Collect results and apply swaps
    output_list = [ '\n'.join(result_dict.get(group, [])) for group in ['group1', 'group2', 'group3', 'group4'] ]
    
    # Swap the specified elements
    output_list[1], output_list[3] = output_list[3], output_list[1]
    output_list[2], output_list[3] = output_list[3], output_list[2]

    return output_list

def parse_logfile(logfile_path, output_file_path):
    parsed_groups = []
    current_group = []
    
    try:
        with open(logfile_path, 'r') as logfile:
            for line in logfile:
                stripped_line = line.strip()
                if stripped_line == "":
                    if current_group:
                        parsed_groups.append("\n".join(current_group))
                        current_group = []
                elif '=' in stripped_line:
                    key, value = stripped_line.split('=', 1)
                    key, value = key.strip(), value.strip()
                    current_group.append(f"{key} = {value}")
            
            if current_group:
                parsed_groups.append("\n".join(current_group))
    except IOError as e:
        print(f"Error reading file {logfile_path}: {e}")
        return []
    
    output_list = merge_sect(parsed_groups)

    headers = [
        '[Main_Stats]',
        '[Runtime_Analysis_Stats]',
        '[Geometric_Analysis_Stats_Fermi]',
        '[Statistical_Analysis]'
    ]
    
    # Ensure the number of headers matches the number of groups
    if len(headers) != len(output_list):
        raise ValueError("The number of headers does not match the number of output list elements.")
    
    try:
        with open(output_file_path, 'w') as output_file:
            for header, group in zip(headers, output_list):
                output_file.write(header + "\n")
                output_file.write(group + "\n\n")  
    except IOError as e:
        print(f"Error writing file {output_file_path}: {e}")
    
    print(f"Data extracted from input file {logfile_path} and written to {output_file_path}")
    return output_list

def main():
    logfile_path = "dummy_logfile.txt"
    output_file_path = "generated.txt"
    
    if os.path.exists(logfile_path):
        print(f"The input file namely {logfile_path} exists")
    else:
        print("File does not exist")
        return
    
    output_list = parse_logfile(logfile_path, output_file_path)
    if output_list:
        print("Parsing complete")

if __name__ == "__main__":
    main()
