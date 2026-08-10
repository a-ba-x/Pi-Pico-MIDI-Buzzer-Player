# open the generated song file
with open("song_play.txt") as f:  # your file with the python code
    for line in f:
        line = line.strip()   # remove \n
        if not line or line.startswith("#"):
            continue          # skip empty lines or comments
        exec(line)  
