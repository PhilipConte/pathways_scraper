# pathways_scraper

Scrapes the Virginia Tech timetable using [pyvt](https://github.com/VirginiaTech/pyvt)

Creates a json mapping each CLE area or Pathway to its courses

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
You should update the TERM variable to use the most current semester
```bash
# Create areas.json
python pathways_scraper.py > areas.json
```
You can use a utility to format it to look pretty like the copy I uploaded
