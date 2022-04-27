# :tornado: Tropical Cyclones Name Extraction

### TL;DR - Click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ghjuliasialelli/TropicalCyclones/main?labpath=main.ipynb) to interact with the TC names extractor.

## About

This repository consists of the back-end for an Jupyter notebook interface (using Binder) that allows users to upload an Excel file containing storm events names, and download the same file augmented with a column (`TC names`) containing the extracted tropical cyclone (TC) names. 


## File structure
- [`Extra-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/Extra-names.xlsx) : TC names lacking from `TC-names.xlsx` but matched in `IDMC_data_match_events_manual_check.xlsx`. 
- [`IBTRACS-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/IBTRACS-names.xlsx) : TC names scraped from [IBTrACS](http://ibtracs.unca.edu/). 
- [`TC-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/TC-names.xlsx) : Database of WMO (World Meteorological Organization) tropical cyclone names.
- [`ibtracs_scraper.py`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/ibtracs_scraper.py) : Script for obtaining `IBTRACS-names.xlsx`. 
- [`main.ipynb`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/main.ipynb) : Jupyter notebook on which Binder relies, client-interface.
- [`requirements.txt`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/requirements.txt) : Package requirements for the code execution.
- [`tools.py`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/tools.py) : Contains all the functions needed to execute `main.ipynb`. 


## Details on the construction of the databases

TODO
