import argparse
import logging
import os
import re
import shutil

# Helper function to set up loggers
def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(level)
    
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Set up loggers
info_logger = setup_logger('info_logger', '../11610/qor/logs/parsing_log/info_H.log', logging.INFO)
error_logger = setup_logger('error_logger', '../11610/qor/logs/parsing_log/error_H.log', logging.ERROR)



def merge_sect(parsed_groups, fermi_id=None):
    groups = {
        'group1': {'gpu', 'machine_name', 'design_size'},
        'group2': {'high_curvature_internal_checking_count', 'mrc_area_count'},
        'group3': {'mean_fermi'},
        'group4': {'target_prep_runtime'}
    }
    result_dict = {group: [] for group in groups}
    for item in parsed_groups:
        first_line, *remaining_lines = item.split('\n')
        key = first_line.split(' = ', 1)[0]
        for group, keys in groups.items():
            if key in keys:
                result_dict[group].append(item)
                break
    output_list = [result_dict[group] for group in ['group1', 'group2', 'group3', 'group4']]
    output_list[1], output_list[3] = output_list[3], output_list[1]
    output_list[2], output_list[3] = output_list[3], output_list[2]

    if fermi_id:
        output_list[0].insert(0, f'fermi_id = {fermi_id}')
        output_list[0].insert(1, 'revision = None')

    return ['\n'.join(group) for group in output_list]

def parse_logfile(logfile_path, output_file_path, fermi_id=None):
    try:
        with open(logfile_path, 'r') as logfile:
            info_logger.info(f"Reading file {logfile_path}")
            parsed_groups, current_group = [], []
            for line in logfile:
                stripped_line = line.strip()
                if not stripped_line:
                    if current_group:
                        parsed_groups.append("\n".join(current_group))
                        current_group = []
                elif '=' in stripped_line:
                    current_group.append(stripped_line)
            if current_group:
                parsed_groups.append("\n".join(current_group))
    except IOError as e:
        error_logger.error(f"Error reading file {logfile_path}: {e}")
        return []
    
    output_list = merge_sect(parsed_groups, fermi_id)
    headers = [
        '[Main_Stats]',
        '[Runtime_Analysis_Stats]',
        '[Geometric_Analysis_Stats_Fermi]',
        '[Statistical_Analysis]'
    ]
    
    if len(headers) != len(output_list):
        error_logger.error("The number of headers does not match the number of output list elements.")
        raise ValueError("The number of headers does not match the number of output list elements.")
    
    try:
        with open(output_file_path, 'w') as output_file:
            for header, group in zip(headers, output_list):
                output_file.write(f"{header}\n{group}\n\n")
        info_logger.info(f"Data extracted from input file {logfile_path} and written to {output_file_path}")
    except IOError as e:
        error_logger.error(f"Error writing file {output_file_path}: {e}")
    
    return output_list



def main():
    parser = argparse.ArgumentParser(description="Parse a log file and generate a fermi.txt file.")
    parser.add_argument('-l', '--location', action='store_true', help='Log the location or path of run.')
    parser.add_argument('-id', '--id', action='store_true', help='ID of the run.')
    parser.add_argument('-p', '--parse', action='store_true', help='Only parse the file and create fermi.txt.')
    parser.add_argument('-r', '--rsync', action='store_true', help='Directory of rsync, which will contain only the qor folder.')
    args = parser.parse_args()
    
    logfile_path = "../11610/logs/optimization/dummy_logfile.txt"
    output_file_path = "../11610/qor/fermi.txt"
    # Define the directory to be checked/created
    rsync_dir = "../rsync/qor"
    fermi_dir = re.search(r'../(\d+)/', logfile_path)

    # Check if any flags are provided
    if not (args.location or args.id or args.parse or args.rsync):
        error_logger.error("No flags provided. Exiting.")
        return

    # # Default to parse the log file if no flags are provided
    # if not (args.location or args.id or args.parse or args.rsync):
    #     info_logger.info("No flags provided. Defaulting to parse the log file and create fermi.txt.")
    #     args.parse = True


    if args.parse:
        if os.path.exists(logfile_path):
            info_logger.info(f"The input file namely {logfile_path} exists")

            # Remove the check for the rsync directory
            info_logger.info("Parsing the file and creating fermi.txt")
            output_list = parse_logfile(logfile_path, output_file_path, fermi_id=fermi_dir.group(1))
            if output_list:
                info_logger.info("Parsing complete")
        else:
            error_logger.error("File does not exist")

    
    if args.location:
        info_logger.info("Logging the location of the run")
        current_dir = os.getcwd()
        # Calculate the path two levels up
        path = os.path.abspath(os.path.join(current_dir, '..'))
        info_logger.info(f"The location of the run is: {path}")
        
    if args.id:
        # Extract the ID number from the path using regex
        info_logger.info("Logging the location of the run")
        
        if fermi_dir:
            id_number = fermi_dir.group(1)
            info_logger.info(f"The ID of the run is: {id_number}")
        else:
            error_logger.error("Failed to extract ID number from path.")
        # info_logger.info("Logging the ID of the run")
        # # Get the parent directory path and extract the name of the parent directory
        # parent_dir = os.path.basename(os.path.dirname(os.getcwd()))
        # info_logger.info(f"The name of the run is: {parent_dir}")
    
    if args.rsync:
        # Check if the directory exists and create it if necessary
        if not os.path.isdir(rsync_dir):
            try:
                os.makedirs(rsync_dir, exist_ok=True)
                info_logger.info(f"Created directory: {rsync_dir}")
            except Exception as e:
                error_logger.error(f"Failed to create directory {rsync_dir}. Error: {e}")
                return  # Exit if the directory creation fails
        else:
            info_logger.info(f"Rsync directory already exists: {rsync_dir}")

        # Copy the file from the source location to the newly created folder
        source_file = "../11610/qor/fermi.txt"
        destination_file = os.path.join(rsync_dir, "fermi.txt")
        try:
            shutil.copy(source_file, destination_file)
            info_logger.info(f"Copied {source_file} to {destination_file}")
        except Exception as e:
            error_logger.error(f"Failed to copy file from {source_file} to {destination_file}. Error: {e}")


    
if __name__ == "__main__":
    main()
