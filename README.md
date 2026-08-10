# Pi-Pico-MIDI-Buzzer-Player

A Raspberry Pi Pico project to convert MIDI files into Python instructions for a buzzer connected to the microcontroller.

The goal of this project was to explore the process of transforming musical data into instructions for a resource-constrained embedded system (and, honestly, to play a song I like).

---

## Overview

The workflow is :

(Sheet music)

↓

MIDI file

↓

CSV file

↓

Python code generated for the Pico and stored in a .txt file

↓

Pico executes the generated code progressively

↓

Buzzer plays the song

### Engineering constraint 

The Raspberry Pi Pico has limited memory, so directly generating a large .py file containing the entire song can become impractical, especially for longer pieces.

To address this constraint, the project separates offline preprocessing from on-device execution. The MIDI data is processed on a computer, where the conversion script generates the Python instructions needed to play the song. These instructions are stored in a .txt file rather than as a standalone Python program.

The Pico then uses ```main.py``` to read and execute the generated instructions progressively, avoiding the need to load the entire generated program into memory at once.

### How it works

The conversion script reads the MIDI-derived CSV file and extracts, for each note :
- its name, which determines the pitch
- its velocity, which is converted into the buzzer's volume (```strength```)
- its duration, which determines how long the Pico waits before proceeding to the next note

Each note is then converted into two Python instructions, such as :
```
buzzer.play('c4', 2.4)
time.sleep(0.5)
```
The first instruction makes the buzzer play the corresponding note at the calculated volume, while the second preserves the note's duration.

The resulting instructions are written to ```song_play.txt``` and progressively executed by ```main.py``` on the Raspberry Pi Pico.

##  Hardware 

Required components :
- Raspberry Pi Pico
- Breadboard
- Buzzer
- Two connecting wires

<img width="600" height="740" alt="circuit_image_music_buzzer" src="https://github.com/user-attachments/assets/12647458-9922-4f2a-8090-fc65681eb11c" />
  
##  Project files
- ```csv_from_midi_to_pi_pico_buzzer_code.py``` : converts MIDI-derived data into instructions compatible with the Raspberry Pi Pico and stores them in a file called ```song_play.txt```
- ```main.py``` : runs on the Raspberry Pi Pico and executes the generated instructions progressively from ```song_play.txt```



---


## Step-by-step tutorial to go from this repo to your own beeping musical device

### Step 0 (Optional) : Create a MIDI File from a Music Sheet
_If you already have a `.mid` file, skip this section._

If you don’t already have your song in a MIDI file:

1. Create or upload your music sheet on **MuseScore**.
2. Go to:

   ```
   File → Export → MIDI file
   ```
3. Save the file as:

   ```
   song.mid
   ```



### Step 1. Convert your MIDI file to a CSV file

1. Go to: https://midi-to-csv.vercel.app/  
2. Upload your `song.mid` file.  
3. Download the generated CSV file.

You should now have ```song.csv```



### Step 2. Build your Raspberry Pi Pico circuit

You will need :
- a Raspberry Pi Pico
- a breadboard
- a buzzer
- two connecting wires

Connect your buzzer to a GPIO pin and to a GND pin :

<img width="600" height="740" alt="circuit_image_music_buzzer" src="https://github.com/user-attachments/assets/12647458-9922-4f2a-8090-fc65681eb11c" />



### Step 3. Generate the code for your Raspberry Pi Pico, and save it in a .txt file

Place the following files in the same folder on your computer:

- ```song.csv```
- ```csv_from_midi_to_pi_pico_buzzer_code.py```

Open a terminal or Python console in this folder and run ```python csv_from_midi_to_pi_pico_buzzer_code.py```

Before running the script, check that the buzzer GPIO pin matches your hardware configuration : in the script, replace 21 in: ```buzzer = Speaker(21)``` with the GPIO pin connected to your buzzer.

The script will generate ```song_play.txt```.



### Step 4. Copy Files to the Raspberry Pi Pico

Copy the following files to your Pico:

- `song_play.txt`
- `main.py`

Make sure the files are placed in the Pico's main directory.



## Result

Once the files are uploaded, connect the Pico to power. The Raspberry Pi Pico will execute the generated instructions and play your song through the connected buzzer.

---

© 2026 Andrea BAÑALES AGUIAR

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the LICENSE file for details.
