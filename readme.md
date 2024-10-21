# Square Root Calculator

This project calculates square roots for numbers provided by different vendors.

## Setup

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.

## Configuration

The `mapper.py` file contains the configuration for different vendors. Each vendor has the following properties:
- `key`: The key in the JSON data that contains the number to calculate the square root of.
- `file`: The input JSON file for the vendor.
- `write_file`: The output JSON file for the vendor's results.

You can add or modify vendors in this file as needed.

## Input Files

Prepare your input JSON files according to the configuration in `mapper.py`. For example:
- `numbers_vendor_A.json`
- `numbers_vendor_B.json`

## Running the Program

To run the program, execute the following command in your terminal:

python entrypoint.py