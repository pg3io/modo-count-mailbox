# Modoboa count

![langage](https://img.shields.io/badge/Langage-Python-green.svg)

```
usage: modo-count.py [-h] -r EMAIL -t TOKEN -a URL [-o json/read]

optional arguments:
  -h, --help            show this help message and exit
  -r EMAIL, --reseller EMAIL
                        precise email of the reseller
  -t TOKEN, --token TOKEN
                        Token for access to data
  -a URL, --api URL     precise url modoboa
  -o json/read, --output json/read
                        precise output : json/read
```                

## Usage
```
python3 modo-count.py -r <EMAIL> -t <TOKEN> -a <URL>
```
or
```
python3 modo-count.py -r <EMAIL> -t <TOKEN> -a <URL> -o json
````

The output is going to be formated in JSON by default

## Format output for terminal usage
```
python3 modo-count.py -r <EMAIL> -t <TOKEN> -a <URL> -o read
```

## Docker usage

The output is going to be formated in JSON by default

### Build
```
docker build -t <NAME:VERSION> .
```
#### Run
```
docker run <NAME:VERSION> -r <EMAIL> -t <TOKEN> -a <URL>
```
or
```
docker run <NAME:VERSION> -r <EMAIL> -t <TOKEN> -a <URL> -o json
docker run <NAME:VERSION> -r <EMAIL> -t <TOKEN> -a <URL> -o read
```

# License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

# Author Information
This role was created in 11/10/2018 by [PG3](https://pg3.io)