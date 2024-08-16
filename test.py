# import os
# def parse_logfile(logfile_path, output_file):
#     additional_lines = [
#         "[Main_Stats]",
#         "[Runtime_Analysis_Stats]",
#         "[Geometric_Analysis_Stats_Fermi]",
#         "[Statistical_Analysis]"
#     ]
#     with open(logfile_path, 'r') as logfile, open(output_file, "w") as file:
#         index = 0
#         for line in logfile:
#             stripped_line = line.strip()
#             if stripped_line == "":
#                 file.write("\n")
#                 if index < len(additional_lines):
#                     file.write(f"{additional_lines[index]}\n")
#                     index += 1
#             elif '=' in stripped_line:
#                 key, value = stripped_line.split('=', 1)
#                 key, value = key.strip(), value.strip()
#                 file.write(f"{key} = {value}\n")

#         print(f"Data extracted from input file {logfile_path}")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()










# import os
# def parse_logfile(logfile_path, output_file):
#     additional_lines = [
#         "[Main_Stats]",
#         "[Runtime_Analysis_Stats]",
#         "[Geometric_Analysis_Stats_Fermi]",
#         "[Statistical_Analysis]"
#     ]
#     with open(logfile_path, 'r') as logfile, open(output_file, "w") as file:
#         index = 0
#         for line in logfile:
#             stripped_line = line.strip()
#             if stripped_line == "":
#                 file.write("\n")
#                 if index < len(additional_lines):
#                     file.write(f"{additional_lines[index]}\n")
#                     index += 1
#             elif '=' in stripped_line:
#                 key, value = stripped_line.split('=', 1)
#                 key, value = key.strip(), value.strip()
#                 file.write(f"{key} = {value}\n")

#         print(f"Data extracted from input file {logfile_path}")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()












































# import os

# def parse_logfile(logfile_path, output_file):
#     fermi_data = {}
#     with open(logfile_path, 'r') as logfile:
#         for line in logfile:
#             if '=' in line:
#                 key, value = line.strip().split('=')
#                 fermi_data[key.strip()] = value.strip()
#         print(f"Data extracted from input file {logfile_path}")

#     with open(output_file, "w") as file:
#         for key, value in fermi_data.items():
#             file.write(f"{key} = {value}\n")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()




