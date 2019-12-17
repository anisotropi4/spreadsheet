# Dump `ODS` spreadsheet content `ods2tsv.py`

The `ods2tsv.py` script dumps the content of `ods` files to a `[tabname].tsv` diles in the (default) `output` directory. Command line parameters:

+   ```--tabnames``` to dump the names of the tabs in the file(s) and stop  
+   ```--path``` (optional) set the output directory path (default) output  
+   ```--tab``` (optional) set the name of the tab to process  
+   ```--csv``` (optional) output in CSV rather than TSV format  
+   ```--sourcename``` (optional) append file name to the outpuf file 

If not present in the current directory, the `ods2tsv.py` script creates the (default) `output` directory

## Dependencies

The `ods2tsv.py` is a simple wrapper script based on the python3 and the [xlrd](https://pypi.org/project/xlrd), [odfpy](https://https://github.com/eea/odfpy) and [pandas](https://pandas.pydata.org) libraries.

## Set up a virtual python environment

It is recommended that python library dependencies are managed via a `virtual environment`. This is configured and activated as follows:

```
   $ virtualenv venv
   $ source venv/bin/activate
```

In the virtual environment use `pip` to install the `pandas` and `odfpy` libraries: 

```
    (venv) $ ./venv/bin/pip install pandas odfpy
```

The `ods2tsv.py` library dependencies  are then met:

```
    (venv) $ ./ods2tsv.py -h
usage: ods2tsv.py [-h] [--tabnames | --tab TAB]
                  [--path PATH | --csv | --stdout] [--sourcename]
                  [inputfiles [inputfiles ...]]

Dump ods files tab(s) to .tsv files, to the (default output) path

positional arguments:
  inputfiles    name of ods-file to process

optional arguments:
  -h, --help    show this help message and exit
  --tabnames    dump name of tabs
  --tab TAB     name of tab to process
  --path PATH   output directory file
  --csv         csv file output
  --stdout      dump a tab to stdout
  --sourcename  prepend filename to output tab file
```

The `virtual environment` is deactivated as follows:

```
    (venv)$ deactivate 
```

## Usage Examples

To run following examples download the `bus0112.ods` and `bus0113.ods` [bus passenger journey statistics](https://www.gov.uk/government/statistical-data-sets/bus01-local-bus-passenger-journeys) files.

### Basic usage
Dump the `BUS0112` tab from the `bus0112.ods` file in a `.tsv` format in the `output` directory:

```
  $ ./ods2tsv.py connectivity-statistics-destination-lists.xls 
  $ ls output
BUS0112.tsv
```

### All tabs in a file
Dump the names of the tabs from the `bus0112.ods` file:

```
$ ./ods2tsv.py --tabnames 
BUS0112
```

### One tab into a given directory
Dump the `BUS0112` tab data into the `bus` directory:

```
  $ ./ods2tsv.py --tab BUS0112 --path bus bus0112.ods 
  $ ls bus
BUS0112.tsv
```

### All tabs from multiple-files into multiple `.tsv` files and append filename

Dump all the tab data from the `bus0112.ods` and `bus0113.ods` files into the `output` directory with filenames `<tab>.tsv`:

```
  $ ./ods2tsv.py --sourcename bus0112.ods bus0113.ods
  $ ls output
bus0112:BUS0112.tsv
bus0113:BUS0113.tsv
```

### Dump a named-tab into a `.csv` files 

Dump the `BUS0112` tab data from the `bus0112.ods` file into the `output` directory with filenames `BUS0112.csv`:

```
  $ ./ods2tsv.py --csv --tab BUS0112 bus0112.ods
  $ ls output
BUS0112.csv
```
