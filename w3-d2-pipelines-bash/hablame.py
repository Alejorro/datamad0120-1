#!/usr/bin/env python

from subprocess import check_output
import pandas as pd
import random
from io import StringIO
import argparse

def bash_command(cmd):
    return check_output(['/bin/bash', '-c', cmd]).decode('utf-8')

def main(nVeces):
    voices = bash_command('say --voice="?"')
    #df = pd.read_csv(StringIO(voices), encoding="utf-8", sep=r"\w*\^",header=None)
    #print(df)
    voices = voices.split("\n")
    voices = list(map(lambda x: x.split(" ")[0],voices))[0:-1]
    selectedVoice = random.choice(voices)

    ta = random.choice(["Felipe","Fran","Ovi","Blanca","Clara"])
    frase = f"Hola {ta}"
    print(f"Saludando a {ta} con la voz de {selectedVoice}")

    print(f"Saludando {nVeces}...")
    for n in range(nVeces):
        bash_command(f'say --voice "{selectedVoice}" "{frase}"')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Saludar a un TA random con voz random')
    parser.add_argument('-n', dest='nveces', default=1, help='Saluda a un TA random n-veces', type=int)

    args = parser.parse_args()
    main(args.nveces)
