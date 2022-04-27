# :tornado: Tropical Cyclones Name Extraction

### TL;DR - Click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ghjuliasialelli/TropicalCyclones/main?labpath=main.ipynb) to interact with the TC names extractor.

## About

This repository consists of the back-end for an Jupyter notebook interface (using Binder) that allows users to upload an Excel file containing storm events names, and download the same file augmented with a column (`TC names`) containing the extracted tropical cyclone (TC) names. 


## File structure
- [`Extra-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/Extra-names.xlsx) : Supplementary TC names, lacking from `TC-names.xlsx` but matched in `IDMC_data_match_events_manual_check.xlsx`.
- [`IBTRACS-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/IBTRACS-names.xlsx) : TC names scraped from [IBTrACS](http://ibtracs.unca.edu/). 
- [`TC-names.xlsx`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/TC-names.xlsx) : Database of [WMO](https://public.wmo.int/en) (World Meteorological Organization) tropical cyclone names.
- [`ibtracs_scraper.py`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/ibtracs_scraper.py) : Script for obtaining `IBTRACS-names.xlsx`. 
- [`main.ipynb`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/main.ipynb) : Jupyter notebook on which Binder relies, client-interface.
- [`requirements.txt`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/requirements.txt) : Package requirements for the code execution.
- [`tools.py`](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/tools.py) : Contains all the functions needed to execute `main.ipynb`. 


## Details on the construction of the databases

### `TC-names.xlsx` 
This file consists of Tropical Cyclone (TC) names obtained from the World Meteorological Organization's [Tropical Cyclone Naming conventions](https://public.wmo.int/en/our-mandate/focus-areas/natural-hazards-and-disaster-risk-reduction/tropical-cyclones/Naming). The names are split in various sheets, one for each of the following regions: Caribbean Sea, Gulf of Mexico and the North Atlantic Names ; Eastern North Pacific Names ; Central North Pacific Names ; Western North Pacific and the South China Sea Names ; Australian Tropical Cyclone Warning Centre's (TCWC) Area of Responsibility ; Regional Specialised Meteorological Centre Nadi's Area of Responsibility ; Port Moresby Tropical Cyclone Warning Centre's Area of Responsibility ; Jakarta Tropical Cyclone Warning Centre's Area of Responsibility ; Northern Indian Ocean Names - Arabian Sea and the Bay of Bengal ; Southwest Indian Ocean Names. There are two additional sheets, one for Greek Names (sometimes used by agencies to supplement their lists of TC names), and one for "Extra Names" (described [below](https://github.com/ghjuliasialelli/TropicalCyclones/blob/main/markdown_readme### "Extra Names")).

### `IBTRACS-names.xlsx`
This file consists of TC names obtained from [IBTrACS](http://ibtracs.unca.edu/) (the International Best Track Archive for Climate Stewardship), which is the most complete global collection of tropical cyclones available. It merges recent and historical tropical cyclone data from multiple agencies to create a unified, publicly available, best-track dataset that improves inter-agency comparisons. IBTrACS was developed collaboratively with all the World Meteorological Organization (WMO) Regional Specialized Meteorological Centres, as well as other organizations and individuals from around the world. A simple script (`ibtracs_scraper.py`) was used to scrape all the TC names from the website.

### "Extra Names"
/!\ Not be be confused with `Extra-names.xlsx`. This sheet, part of `TC-names.xlsx`, is basically the intersection between TC names in `IBTRACS-names.xlsx` and `Extra-names.xlsx`. 
 
