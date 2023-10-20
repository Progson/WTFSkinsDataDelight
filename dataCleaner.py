import csv
from datetime import datetime
def split_date_and_time(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Zapisz nagłówki z dodatkowymi kolumnami
        headers = next(reader)
        headers.extend(["day", "month", "year", "hour", "minute", "second"])
        writer.writerow(headers)
        
        for row in reader:
            if len(row) >= 5:  # Upewnij się, że wiersz ma co najmniej 5 kolumn (indeksy 3 i 4)
                date_str, time_str = row[3], row[4]
                if date_str and time_str:  # Upewnij się, że dane w tych kolumnach nie są puste
                    # Parsuj datę i czas
                    try:
                        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
                        time_obj = datetime.strptime(time_str, "%H:%M:%S")
                        # Rozdziel na osobne kolumny
                        row.extend([
                            date_obj.day,
                            date_obj.month,
                            date_obj.year,
                            time_obj.hour,
                            time_obj.minute,
                            time_obj.second
                        ])
                    except ValueError:
                        print(f"Nieprawidłowe dane w wierszu: {', '.join(row)}")
                else:
                    print(f"Brakujące dane w wierszu:'{row}")
            else:
                print(f"Nie wystarczająca liczba kolumn w wierszu: {row}")

            # Zawsze zapisuj wiersz, nawet jeśli brakuje kolumn
            writer.writerow(row)

    print("Kolumny 'date' i 'time' zostały rozdzielone.")
 
def remove_x_from_first_3_columns(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)

        # Zapisz nagłówki
        headers = next(reader)

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(headers)

            for row in reader:
                # Usuń "x" z przodu trzech pierwszych kolumn
                for i in range(3):
                    if row[i].startswith('x'):
                        row[i] = row[i][1:]  # Usuń "x"
                writer.writerow(row)

    print("Plik z usuniętą literą 'x' z pierwszych trzech kolumn został zapisany.")
    
def check_records(input_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)

        # Zapisz nagłówki
        headers = next(reader)

        all_records_have_all_data = True

        for row in reader:
            # Sprawdź, czy wiersz ma wszystkie wartości (nie ma pustych pól)
            if not all(row):
                all_records_have_all_data = False
                print(f"Brakujące dane w wierszu: {', '.join(row)}")

        if all_records_have_all_data:
            print("Wszystkie rekordy mają wszystkie dane.")
        else:
            print("Niektóre rekordy mają brakujące dane.")
            
def remove_records_with_missing_data(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        with open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

        # Zapisz nagłówki
            headers = next(reader)
            writer.writerow(headers)

            for row in reader:
            # Sprawdź, czy wiersz ma wszystkie wartości (nie ma pustych pól)
                if all(row):
                    writer.writerow(row)

    print("Rekordy z brakującymi danymi zostały usunięte.")

def copy_columns_except_3rd_and_4th(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Skopiuj kolumny poza trzecią (indeks 2) i czwartą (indeks 3) kolumną
            new_row = row[:3] + row[5:]
            writer.writerow(new_row)

    print("Kolumny poza trzecią i czwartą zostały skopiowane.")

input_file = 'data.csv'
output_file = 'clean_stage_1.csv'

remove_records_with_missing_data(input_file=input_file,output_file=output_file)
check_records(output_file)
input_file = output_file
output_file = 'clean_stage_2.csv'
remove_x_from_first_3_columns(input_file=input_file,output_file=output_file)
input_file = output_file
output_file = 'clean_stage_3.csv'
split_date_and_time(input_file, output_file)
input_file = output_file
output_file = 'prepared_data.csv'
copy_columns_except_3rd_and_4th(input_file,output_file)
exit()
