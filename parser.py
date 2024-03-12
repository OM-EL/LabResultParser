import numpy as np

# Initialization
Npoint = 2000
Qc = 1940.0
T_on, T_off, power = 3, 0.5, 200.0
periode = T_on + T_off
hs, ds = 5.45, 5.45  # mm
Vs = np.pi * ds ** 2 * hs / 4.0
Vc = 86.69 * 43.18 * 250  # mm^3
Fc = 2.440348

print(f"Volume de l'echantillon: {Vs}")
print(f"Volume de la cavite: {Vc}")
print(f"Frequence de resonnance a vide Fc: {Fc}")


def safe_decode(binary_line, primary='utf-8', fallback='ISO-8859-1'):
    """Attempt to decode a binary line using a primary encoding, falling back to a secondary encoding in case of failure."""
    try:
        return binary_line.decode(primary)
    except UnicodeDecodeError:
        return binary_line.decode(fallback)


# Error handling for reading Ncycle
def read_ncycle(file):
    while True:
        line = file.readline()
        if not line:  # End of file
            raise ValueError("Ncycle not found in file.")
        decoded_line = safe_decode(line)
        parts = decoded_line.strip().split()
        if parts:  # Non-empty line
            try:
                return int(parts[-1])
            except ValueError:
                continue  # Not an integer, try the next line


# Open the data file in binary mode and the output files in text mode
with open('05_02_2024-11_55', 'rb') as data_file, \
        open('power_vs_time.dat', 'w') as power_file, \
        open('temperature_vs_time.dat', 'w') as temp_file:
    # Improved Ncycle reading with error handling
    Ncycle = read_ncycle(data_file)

    # Placeholder: Reading x values and y values
    x_values = np.zeros(Npoint)  # Assuming how to populate based on actual data
    for cycle in range(Ncycle):
        # Placeholder for reading y values and temperature for each cycle
        y_values = np.zeros(Npoint)  # Assuming how to populate based on actual data
        temperature = 25.0  # Example placeholder temperature

        # Analysis logic placeholder (Bandwidth, Quality Factor, etc.)
        # Add analysis code here as needed

        # Writing to output files (placeholders for actual values)
        power_file.write(f"{cycle * periode}, 0\n")
        power_file.write(f"{cycle * periode + T_off}, {power}\n")

        temp_file.write(f"{cycle * periode}, {temperature}\n")

print("Analysis completed and results written to output files.")
