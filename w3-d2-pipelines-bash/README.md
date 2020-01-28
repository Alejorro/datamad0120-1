# Pipe in Bash
```bash
cat musica.txt | xargs youtube-dl --audio-format mp3 -x
cat vehicles/vehicles.csv | tail
cat vehicles/vehicles.csv | head

# Extract data from BIG CSV
cat vehicles/vehicles.csv | head | cut -d "," -f1 -f2 -f3

# Redirigir la salida por consola a un fichero
ls > ejemplo.txt
cat vehicles/vehicles.csv | cut -d "," -f1 -f2 -f3 > vehicles/vehicles_drop.csv

# Contar las lineas de un comando
cat vehicles/vehicles.csv | cut -d "," -f1 -f2 -f3 | grep "[Aa]udi" | head -n 50 | wc -l
```

## Other commands

```bash
# Ver permisos
ls -als

# Dar permisos de ejecución a un fichero

```