# Star Wars Legion Probability Calculator

A Python-based probability calculator for Star Wars: Legion tabletop wargame.

## Features

- Calculate attack probability distributions for any unit matchup
- Support for all major factions: Republic, Separatist, Empire, Rebel, Mercenary
- CLI and GUI interfaces
- 149+ units with upgrade cards automatically scraped from the wiki
- Special mechanics: Makashi Mastery (bypass Immune: Pierce), High Velocity (ignore dodges)
- Cover system (Light/Heavy cover with probabilistic dice rolling)
- All standard attack/defense modifiers

## Installation

### Setting up a Virtual Environment (Recommended)

1. **Create a virtual environment:**
   ```bash
   python3 -m venv swl
   ```

2. **Activate the virtual environment:**
   - On Linux/Mac:
     ```bash
     source swl/bin/activate
     ```
   - On Windows:
     ```bash
     swl\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Quick Install (Without venv)

If you prefer not to use a virtual environment:
```bash
pip install -r requirements.txt
```

### Dependencies

The project requires:
- **PyQt6** (≥6.0.0) - GUI framework
- **matplotlib** (≥3.5.0) - Chart rendering
- **requests** (≥2.28.0) - Web scraper HTTP requests
- **beautifulsoup4** (≥4.11.0) - Web scraper HTML parsing

## Usage

### CLI Mode
Run the calculator with predefined test cases:
```bash
python calculator.py
```

### GUI Mode
Launch the graphical interface:
```bash
python gui.py
```

#### GUI Features:
- **Hierarchical unit selection**: Choose faction → unit type → unit → weapon
- **Multiple attackers**: Add multiple units to simulate Arsenal or Fire Support
- **All modifiers supported**: Aims, Pierce, Cover, Dodges, Shields, etc.
- **Special mechanics**: Checkboxes for Makashi Mastery and High Velocity
- **Visual bar chart**: Vertical probability distribution with expected damage

## Web Scraper

The project includes a web scraper that automatically fetches unit data from the Star Wars Legion wiki.

### Running the Scraper

**Scrape all factions:**
```bash
python3 scrape_legion_units.py --rate-limit 0.25
```

**Scrape a specific faction:**
```bash
python3 scrape_legion_units.py --faction empire --rate-limit 0.25
```

**Verbose output:**
```bash
python3 scrape_legion_units.py --verbose --rate-limit 0.5
```

### Scraper Features

- Automatically extracts unit data from https://starwarslegion.fandom.com
- Scrapes unit stats: name, size, weapons, defense dice, surge conversions
- Parses weapon upgrades (heavy weapons, personnel cards, etc.)
- Extracts dice pools and keywords (Impact, Pierce, Critical, Blast, etc.)
- Outputs structured JSON files for each faction
- Rate limiting to avoid overwhelming the server (default: 1.0 seconds between requests)

### Importing Scraped Data

After scraping, import the data into the Python config files:
```bash
python3 import_scraped_units.py
```

This will update all faction configs with the newly scraped units.

## File Structure

- `calculator.py` - CLI calculator with test cases
- `gui.py` - PyQt6 GUI application
- `scrape_legion_units.py` - Web scraper for wiki data
- `import_scraped_units.py` - Imports JSON into Python configs
- `unit_registry.py` - Hierarchical unit organization (auto-loads all units)
- `unit.py` - Core unit and combat logic
- `dice.py` - Dice probability calculations
- `weapon.py` - Weapon definitions
- `distribution.py` - Damage distribution output formatting
- `*_config.py` - Unit configurations by faction
- `constants.py` - Game constants (cover levels, etc.)

## Implemented Mechanics

### Attack Mechanics
- Aims (with Precise rerolls)
- Surge conversions (Hit/Crit)
- Impact (convert hits to crits)
- Critical tokens
- Pierce
- Dice improvements

### Defense Mechanics
- Cover (Light/Heavy with white dice rolls)
- Cover improvement (unit keyword)
- Dodges
- Shields
- Armor
- Defense surge conversions
- Immune: Pierce
- Impervious

### Special Mechanics
- **Makashi Mastery** (bypass_immune_pierce flag): Bypasses Immune: Pierce
- **High Velocity** (ignore_dodges flag): Ignores dodge tokens

## Units Implemented

All units are automatically loaded from faction config files. The web scraper has imported:

- **Empire**: 40 units (Commanders, Operatives, Corps, Special Forces, Support, Heavy)
- **Rebel**: 43 units (all categories)
- **Republic**: 29 units (all categories)
- **Separatist**: 26 units (all categories)
- **Mercenary**: 11 units (Shadow Collective faction)

**Total: 149 units** including unit-specific upgrade cards

Each unit includes:
- Base weapons with dice pools and keywords
- Unit-specific upgrade weapons (heavy weapons, special equipment)
- Defense stats and special abilities
- Proper categorization by rank (Commander, Operative, Corps, etc.)

## Example Usage

```python
from calculator import SWLegion

# Basic attack
SWLegion.attack(['vader'], 'luke')

# With cover
SWLegion.attack(['p1'], 'b1', cover=COVER_LIGHT)

# With Makashi Mastery (bypasses Immune: Pierce but reduces pierce by 1)
SWLegion.attack(['dooku'], 'ob', weapons=[0], bypass_immune_pierce=True, pierce=-1)

# High Velocity (ignores dodges)
SWLegion.attack(['aat'], 'target', weapons=[1], ignore_dodges=True)
```

## Notes

- CLI output uses horizontal bar charts for easy terminal printing
- GUI uses vertical bar charts for better visualization
- Expected damage is calculated and displayed in both modes
- All calculations use exact probability distributions (not simulations)
