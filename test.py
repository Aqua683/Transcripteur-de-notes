import pandas as pd
from tabulate import tabulate
from openpyxl import load_workbook

# Read the Excel file
df_RAW = pd.read_excel('MusicDatabase.xlsx', sheet_name = "RAW_DATA")
df_PROCESSED = pd.read_excel('MusicDatabase.xlsx', sheet_name = "PROCESSED_DATA")
df_REFERENCE = pd.read_excel('MusicDatabase.xlsx', sheet_name = "REFERENCE")

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


def get_rythmn_from_duration(duration, tempoFormula):
    # Ratios for different note types based on real music rhythm
    if duration == 4 * tempoFormula:
        return "Whole Note"
    elif duration == 2 * tempoFormula:
        return "Half Note"
    elif duration == tempoFormula:
        return "Quarter Note"
    elif duration == tempoFormula / 2:
        return "Eighth Note"
    elif duration == tempoFormula / 4:
        return "Sixteenth Note"
    else:
        return "Unknown note type"

for index, row in df_RAW.iterrows():
    freq = row["Frequency(Hz)"]
    note = get_note_from_frequency(freq)
    duration = row["Duration(ms)"]
    IdSong = row["IdSong"]
    tempo = 60
    tempoFormula = 60000/tempo
    rythmn = get_rythmn_from_duration(duration, tempoFormula)
    df_PROCESSED.loc[index, "Note"] = note
    df_PROCESSED.loc[index, "Rythmn"] = rythmn


print(tabulate(df_PROCESSED, headers='keys', tablefmt='pretty'))
with pd.ExcelWriter('MusicDatabase.xlsx', mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_PROCESSED.to_excel(writer, sheet_name='PROCESSED_DATA', index=False)

# Print the contents of the file
