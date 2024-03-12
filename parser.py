import numpy as np

# Initialize constants and variables for analysis
Npoint = 2000  # Number of data points per cycle
Qc = 1940.0  # Quality factor
T_on, T_off, power = 3, 0.5, 200.0  # Timing for power application and the power value
periode = T_on + T_off  # Total period of one cycle of power application
hs, ds = 5.45, 5.45  # Sample height and diameter in mm
Vs = np.pi * ds ** 2 * hs / 4.0  # Volume of the sample calculated using the cylinder volume formula
Vc = 86.69 * 43.18 * 250  # Cavity volume in cubic mm
Fc = 2.440348  # Resonance frequency

# Print initial calculated values for verification
print(f"Volume de l'echantillon: {Vs}")
print(f"Volume de la cavite: {Vc}")
print(f"Frequence de resonnance a vide Fc: {Fc}")


def safe_decode(binary_line, primary='utf-8', fallback='ISO-8859-1'):
    """
    Attempt to decode a binary line using a primary encoding,
    falling back to a secondary encoding in case of failure.
    """
    try:
        return binary_line.decode(primary)
    except UnicodeDecodeError:
        return binary_line.decode(fallback)


# Function to handle the reading of Ncycle from the file, with error handling for empty or non-numeric lines
def read_ncycle(file):
    while True:
        line = file.readline()
        if not line:  # If end of file is reached without finding Ncycle
            raise ValueError("Ncycle not found in file.")
        decoded_line = safe_decode(line)
        parts = decoded_line.strip().split()
        if parts:  # Checks if the line is not empty
            try:
                return int(parts[-1])  # Attempts to return the last part of the line as Ncycle
            except ValueError:
                continue  # If conversion to int fails, move to the next line


# Open the data file in binary mode to handle potential encoding issues
with open('05_02_2024-11_55', 'rb') as data_file, \
        open('power_vs_time.dat', 'w') as power_file, \
        open('temperature_vs_time.dat', 'w') as temp_file:
    # Use the read_ncycle function to robustly read and interpret Ncycle from the data file
    Ncycle = read_ncycle(data_file)

    # Placeholder for actual data reading process
    x_values = np.zeros(Npoint)  # Example initialization of x_values

    # Process data for each cycle based on Ncycle
    for cycle in range(Ncycle):
        # Placeholder for reading y values and temperature for each cycle
        y_values = np.zeros(Npoint)  # Example initialization of y_values
        temperature = 25.0  # Example placeholder temperature value

        # Placeholder for analysis logic such as finding specific points, bandwidth, and quality factor

        # Writing power cycle and temperature data to output files
        power_file.write(f"{cycle * periode}, 0\n")  # Zero power at cycle start
        power_file.write(f"{cycle * periode + T_off}, {power}\n")  # Power applied after T_off

        # Write temperature data at the start of each cycle
        temp_file.write(f"{cycle * periode}, {temperature}\n")

# Indicate completion of analysis and data writing process
print("Analysis completed and results written to output files.")
