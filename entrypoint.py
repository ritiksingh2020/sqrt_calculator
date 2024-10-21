from reader import ReaderClass
from writer import writerClass
from generate_sqrt import GenearteSquareRoot
from mapper import mapping
import concurrent.futures

def process_vendor_data(vendor, input_file):
    reader = ReaderClass(input_file)
    data = reader.fetch_json()

    sqrt_generator = GenearteSquareRoot(data, mapping, vendor)
    result = sqrt_generator.calculate_squareroot()

    writer = writerClass(mapping[vendor]["write_file"])
    success = writer.write_json(result)

    if success:
        print(f"Successfully processed data for {vendor}")
    else:
        print(f"Failed to process data for {vendor}")

def process_vendor_wrapper(args):
    vendor, input_file = args
    try:
        process_vendor_data(vendor, input_file)
    except Exception as e:
        print(f"Error processing {vendor}: {str(e)}")

if __name__ == "__main__":
    vendors = {vendor: data["file"] for vendor, data in mapping.items()}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_vendor_wrapper, vendors.items())
