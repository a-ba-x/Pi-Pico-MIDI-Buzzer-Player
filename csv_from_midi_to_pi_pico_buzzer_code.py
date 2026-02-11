import csv

with open("song.csv", newline="") as f, open("song_play.txt", "w") as out:
    reader = csv.DictReader(f)

    out.write("import time\n")
    out.write("from machine import Pin, ADC\n")
    out.write("from picozero import Switch, Speaker\n")
    out.write("buzzer = Speaker(21)\n\n")

    for row in reader:
        if row["Event Type"] != "note_on":
            continue

        note = row["Note Name"].lower()
        velocity = float(row["Velocity"])
        duration = round(float(row["Duration (seconds)"]), 3)

        strength = round(3 * velocity / 75, 3)

        out.write(f"buzzer.play('{note}', {strength})\n")
        out.write(f"time.sleep({duration})\n\n")
