# Flask App 

## Overview

This project is designed to achieve the following functionalities:
* Parse data: Read the data from log file to generate new file and write the desired data to it. 
* Record data: Read data from generated file (fermi.txt) and write to mysql databse.
* API: Extract and show the data using apis.
* Docker: Setup application docker.
* Postman: API testing using postman.
* CI/CD: Automate the process.
 
## Project Structure

Here's a breakdown of the directory structure:
<pre>

├── Project
│   ├── .github
│   │   ├── workflows
│   │   │   ├── ci-cd-pipeline.yml
│
│   ├── 917
│   │   ├── logs
│   │   │   ├── check_summary
│   │   │   ├── check.summary
│   │   │   ├── exporting
│   │   │   ├── failures
│   │   │   ├── import
│   │   │   ├── model_check
│   │   │   ├── optimization
│   │   │   │   ├── dummy_logfile.txt
│   │   │   │   ├── ilt-opt-flow-tmilt.log
│   │   │   ├── reassembly
│   │   │   ├── recipe
│   │   │   ├── shotcat
│   │   │   ├── summarizing
│   │   │   ├── dummy_logfile.txt
│   │   ├── qor
│   │   │   ├── assest
│   │   │   ├── logs
│   │   │   │   ├── parsing_log
│   │   │   │   │   ├── error_H.log
│   │   │   │   │   ├── info_H.log
│   │   │   │   │   ├── error.log
│   │   │   │   │   ├── info.log
│   │   │   ├── script
│   │   │   ├── Fermi_stats.txt
│   │   │   ├── fermi.txt
│   
│   ├── 11610
│   │   ├── logs
│   │   │   ├── check_summary
│   │   │   ├── check.summary
│   │   │   ├── exporting
│   │   │   ├── failures
│   │   │   ├── import
│   │   │   ├── model_check
│   │   │   ├── optimization
│   │   │   │   ├── dummy_logfile.txt
│   │   │   │   ├── ilt-opt-flow-tmilt.log
│   │   │   ├── reassembly
│   │   │   ├── recipe
│   │   │   ├── shotcat
│   │   │   ├── summarizing
│   │   │   ├── dummy_logfile.txt
│   │   ├── qor
│   │   │   ├── assest
│   │   │   ├── logs
│   │   │   │   ├── parsing_log
│   │   │   │   │   ├── error_H.log
│   │   │   │   │   ├── info_H.log
│   │   │   │   │   ├── error.log
│   │   │   │   │   ├── info.log
│   │   │   ├── script
│   │   │   ├── Fermi_stats.txt
│   │   │   ├── fermi.txt
│
│   ├── postman
│   │   ├── Project.postman_collection.json
│   │   ├── Project.postman_collection2.json
│
│   ├── random
│   │   ├── fermi_stats.txt
│   │   ├── test.py
│
│   ├── rsync
│   │   ├── 917
│   │   │   ├── qor
│   │   │   │   ├── fermi.txt
│   │   ├── 11610
│   │   │   ├── qor
│   │   │   │   ├── fermi.txt
│
│   ├── scripts
│   │   ├── _pycache (hidden directory)
│   │   ├── static 
│   │   │   ├── css
│   │   │   │   ├── abc.css
│   │   │   │   ├── styles.css
│   │   ├── templates 
│   │   │   ├── error.html
│   │   │   ├── index.html
│   │   │   ├── results.html
│   │   │   ├── success.html
│   │   ├── api.py
│   │   ├── app.py
│   │   ├── parse.py
│   │   ├── record.py
│   │   ├── requirements.txt
│
│   ├── venv
│
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── merge.txt
│   ├── README.md

</pre>

## Setup

### Prerequisites

- Python 3.x
- Docker (if using Docker)
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>

    git clone git@github.com:MuhammadHammad-QA/Project.git
    cd Project
    ```

2. Set up a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip3 install -r scripts/requirements.txt
    ```

## Usage

### Running the Parser

The main script for parsing log files is [`scripts/parse.py`]. It provides several command-line options:

- `-l`, `--location`: The location or path of the folder.
- `-id`, `--id`: Folder name (ID of the run).
- `-p`, `--parse`: Only parse the file and create `fermi.txt`.
- `-r`, `--rsync`: Directory of rsync, which will contain only the `qor` folder.

Example usage:
```sh
python3 scripts/parse.py -l <location> -id <id> -p -r
```

### Running the Recorder

The script to record data to database:

Example usage:
```sh
python3 scripts/record.py rsync/917/qor/fermi.txt
```


### Running the API

Extract and visulize data:

Example usage:
```sh
python3 scripts/app.py 
```


### Docker 

To build and run the project using Docker:
Files: Dockerfile, docker-compose.yml

Example usage:
```sh
docker-compose build
docker-compose up
```


### CI/CD

The project includes a CI/CD pipeline configuration in .github/workflows/ci-cd-pipeline.yml.

### Postman

Postman collections for API testing are available in the postman/ directory.