# Format the following text
# "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
# Into the next one
# "Un día que el viento soplaba con fuerza...
# - Mira como se mueve aquella banderola -dijo un monje.
# - Lo que se mueve es el viento -respondió otro monje.
# - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro."

text = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
print("Original text: \n",text,"\n")
print("Format:")

lines = text.split("#")

for i,line in enumerate(lines):
    lines[i] = line.capitalize()
    if i == 0:
        lines[i] = lines[i] + "..."
    else:
        lines[i] = "- " + lines[i] + "."

for line in lines:
    print(line)