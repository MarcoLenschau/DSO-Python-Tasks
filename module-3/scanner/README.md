# Network Scanner

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Quickstart](#quickstart)

### Prerequisites

- Python 3.8
- ipaddress 1.0.23
- pythonping 1.1.4

### Installation

1. Clone the repository or download the script:
    ```
        git clone https://github.com/MarcoLenschau/DSO-Python-Tasks/tree/network-scanner/module-3/scanner
    ```
    
2. Change the directory:
    ```
        cd scanner
    ```

3. Install requirements:
    ```
        pip install -r requirements.txt
    ```

### Quickstart

1. Create a virtual enviroment:
    ```
        python -m venv venv
    ```
    
2. Active the virtual enviroment:
    ```
        source venv/bin/activate
    ```

3. Run the application:
    ```
        python3 main.py -n {NETWORK} -s {SUBNET} -csv {OUTPUT-FILE}
    ```