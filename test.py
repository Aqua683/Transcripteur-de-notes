import pandas as pd

# Read the Excel file
df_RAW = pd.read_excel('MusicDatabase.xlsx', sheet_name = "RAW_DATA")
df_PROCESSED = pd.read_excel('MusicDatabase.xlsx', sheet_name = "PROCESSED_DATA")


def get_note_from_frequency(frequency):
    switcher = {
        261.63: "C",
        293.66: "D",
        329.63: "E",
        349.23: "F",
        392.00: "G",
        440.00: "A",
        493.88: "B",
        523.25: "C (Higher Octave)"
    }
    # Return the corresponding note or a default message if not found
    return switcher.get(frequency, "Note: ")

for index, row in df_RAW.iterrows():
    freq = row["Frequency(Hz)"]
    note = get_note_from_frequency(freq)
    print(f"{freq} Hz is: {note}")


# Print the contents of the file
