# import the necessary packages
import argparse, logging, os, shutil

# Helper function to set up loggers
def setup_logger(name, log_file, level=logging.INFO):
    # Create a logger
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(level)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def merge_sect(parsed_groups, fermi_id=None):
    # Define groups of keys
    groups = {
        'group1': {'gpu', 'machine_name', 'design_size'},
        'group2': {'high_curvature_internal_checking_count', 'mrc_area_count'},
        'group3': {'mean_fermi'},
        'group4': {'target_prep_runtime'}
    }
    # Initialize a dictionary to store the results
    result_dict = {group: [] for group in groups}

    # Iterate over the parsed groups and assign them to the appropriate group
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
        output_list[0].insert(1, 'revision = master')

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
    # Create a parser object
    parser = argparse.ArgumentParser(description="Parse a log file and generate a fermi.txt file.")
    # Add arguments
    parser.add_argument('-l', '--location', type=str, required=True, help='The location or path of the folder.')
    parser.add_argument('-id', '--id', type=str, required=True, help='Folder name (ID of the run).')
    parser.add_argument('-p', '--parse', required=True, action='store_true', help='Only parse the file and create fermi.txt.')
    parser.add_argument('-r', '--rsync', action='store_true', help='Directory of rsync, which will contain only the qor folder.')
    # Parse the arguments
    args = parser.parse_args()

    # Combine the location and ID to form the complete path
    locat = os.path.abspath(args.location)
    combined_path = os.path.join(locat, args.id)
    # Define variables
    global info_logger, error_logger
    
    # Set up loggers
    info_logger = setup_logger('info_logger', os.path.join(combined_path, "qor/logs/parsing_log/info_H.log"), logging.INFO)
    error_logger = setup_logger('error_logger', os.path.join(combined_path, "qor/logs/parsing_log/error_H.log"), logging.ERROR)
    
    if args.parse:
        logfile_path = os.path.join(combined_path, "logs/optimization/dummy_logfile.txt")
        output_file_path = os.path.join(combined_path, "qor/fermi.txt")
        
        if os.path.exists(logfile_path):
            info_logger.info(f"The input file {logfile_path} exists")
            fermi_id = args.id
            info_logger.info("Parsing the file and creating fermi.txt")
            output_list = parse_logfile(logfile_path, output_file_path, fermi_id=fermi_id)
            if output_list:
                info_logger.info("Parsing complete")
        else:
            error_logger.error(f"Log file does not exist at {logfile_path}")

    if args.rsync:
        rsync_dir = os.path.join(locat, f"rsync/{args.id}/qor")
        try:
            os.makedirs(rsync_dir, exist_ok=True)
            info_logger.info(f"Directory created or already exists: {rsync_dir}")
        except Exception as e:
            error_logger.error(f"Failed to create directory {rsync_dir}. Error: {e}")
            return

        source_file = os.path.join(combined_path, "qor/fermi.txt")
        destination_file = os.path.join(rsync_dir, "fermi.txt")
        try:
            shutil.copy(source_file, destination_file)
            info_logger.info(f"Copied {source_file} to {destination_file}")
        except Exception as e:
            error_logger.error(f"Failed to copy file from {source_file} to {destination_file}. Error: {e}")


if __name__ == "__main__":
    main()

