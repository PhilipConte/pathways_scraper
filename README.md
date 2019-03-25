# pathways_scraper

This script will scrapes the Virginia Tech timetable using [pyvt](https://github.com/VirginiaTech/pyvt).

It creates a json mapping each CLE area and Pathway to their courses

## Installation
 Requires python3

```bash
# Clone this repository
git clone https://github.com/PhilipConte/pathways_scraper.git

# Go into the repository
cd pathways_scraper

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Create areas.json
python pathways_scraper.py > areas.json
```
You can use a utility to format it to look pretty like the copy I uploaded
