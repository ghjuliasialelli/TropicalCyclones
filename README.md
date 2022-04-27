# :tornado: Tropical Cyclones Name Extraction

### TL;DR - Click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ghjuliasialelli/TropicalCyclones/main?labpath=main.ipynb) to interact with the TC names extractor.

## About

This repository consists of the back-end for an Jupyter notebook interface (using Binder) that allows users to upload an Excel file containing storm events names, and download the same file augmented with a column (`TC names`) containing the extracted tropical cyclone (TC) names. 


## File structure

- [`TC-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/TC-names.xlsx) : Database of WMO (World Meteorological Organization) tropical cyclone names.
- [`main.ipynb`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/main.ipynb) : Jupyter notebook on which Binder relies, client-interface.
- [`requirements.txt`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/requirements.txt) : Package requirements for the code execution.
- [`tools.py`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/tools.py) : Contains all the functions needed to execute `main.ipynb`. 

