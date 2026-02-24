# Pi-Pico-Music-Buzzer

Here is how to play a song with a Raspberry Pi Pico and a buzzer, from a MIDI file (or a music sheet, with extra steps).

---

## Optional: Create a MIDI File from a Music Sheet
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

---

## 1. Convert your MIDI file to a CSV file

1. Go to: https://midi-to-csv.vercel.app/  
2. Upload your `song.mid` file.  
3. Download the generated CSV file.

You should now have ```song.csv```

---

## 2. Build your Raspberry Pi Pico circuit

You will need :
- a Raspberry Pi Pico
- a breadboard
- a buzzer
- two cables

Connect your buzzer to a GPIO pin and to a GND pin :

<img width="600" height="740" alt="circuit_image_music_buzzer" src="https://github.com/user-attachments/assets/12647458-9922-4f2a-8090-fc65681eb11c" />


---

## 3. Generate the code for your Raspberry Pi Pico, and save it in a .txt file

Put ```song.csv``` and ```csv_from_midi_to_pi_pico_buzzer_code.py``` in the same folder and open your python console.

Run the conversion script: ```csv_from_midi_to_pi_pico_buzzer_code.py```

Before running the script, check that the buzzer GPIO pin is correctly set for your hardware configuration, 
ie, that in ```buzzer = Speaker(21)```  (line 4), you have your output pin instead of 21.

After execution, the script will generate: ```song_play.txt```

Saving the code in a .txt format is done because if one produces a .py file with the same code, it can easily reach thousands of lines of code so it will be too heavy for the Pi Pico's RAM and will not load. 

That is why ```main.py``` will execute the code one line at a time by importing it from the .txt file.

---

## 4. Copy Files to the Raspberry Pi Pico

Copy the following files to your Pico:

- `song_play.txt`
- `main.py`

---

## Result

Once the files are uploaded, the Raspberry Pi Pico will play your song through the connected buzzer once you plug it in.

---

© 2026 Andrea BAÑALES AGUIAR

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the LICENSE file for details.
