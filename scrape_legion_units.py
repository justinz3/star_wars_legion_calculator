#!/usr/bin/env python3
"""
Star Wars Legion Wiki Scraper
Scrapes unit data from starwarslegion.fandom.com and outputs JSON files
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
import argparse
from typing import Dict, List, Tuple, Optional
from collections import defaultdict


class LegionWikiScraper:
    BASE_URL = "https://starwarslegion.fandom.com"
    UNIT_LIST_URL = f"{BASE_URL}/wiki/Unit_List"

    # Mapping for dice colors (wiki notation → our array format [white, black, red])
    DICE_COLOR_MAP = {
        'white': 0,
        'black': 1,
        'red': 2
    }

    def __init__(self, verbose=False, rate_limit=1.0):
        self.verbose = verbose
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; LegionCalculator/1.0)'
        })
        self.units_scraped = 0
        self.units_skipped = 0
        self.total_warnings = 0

    def log(self, message: str, level: str = "INFO"):
        """Print log message if verbose mode is enabled"""
        if self.verbose or level == "ERROR":
            print(f"[{level}] {message}")

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch a page and return BeautifulSoup object"""
        try:
            self.log(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)

            if response.status_code == 404:
                self.log(f"Page not found: {url}", "WARN")
                return None

            response.raise_for_status()
            time.sleep(self.rate_limit)  # Rate limiting
            return BeautifulSoup(response.content, 'html.parser')

        except requests.RequestException as e:
            self.log(f"Error fetching {url}: {e}", "ERROR")
            return None

    def get_unit_list(self) -> Dict[str, Dict[str, List[Tuple[str, str]]]]:
        """
        Scrape the Unit_List page and return organized unit data
        Returns: {faction: {rank: [(name, url), ...]}}
        """
        self.log("Fetching unit list...")
        soup = self.fetch_page(self.UNIT_LIST_URL)

        if not soup:
            self.log("Failed to fetch unit list", "ERROR")
            return {}

        units = defaultdict(lambda: defaultdict(list))

        # Faction mapping
        faction_keywords = {
            'imperial': 'empire',
            'empire': 'empire',
            'separatist': 'separatist',
            'mercenary': 'mercenary',
            'shadow collective': 'mercenary',
            'rebel': 'rebel',
            'republic': 'republic',
            'galactic republic': 'republic'
        }

        # Rank keywords
        rank_keywords = ['commander', 'operative', 'corps', 'special forces', 'support', 'heavy']

        # Parse the content - find the main table
        content = soup.find('div', {'class': 'mw-parser-output'})
        if not content:
            self.log("Could not find main content", "ERROR")
            return {}

        # Find the first table (which contains all units)
        table = content.find('table')
        if not table:
            self.log("Could not find unit table", "ERROR")
            return {}

        # Process each cell that contains faction data
        # Each cell can contain multiple factions separated by tables or paragraphs
        for cell in table.find_all(['td', 'th']):
            # Find faction separators (both tables and paragraphs)
            faction_separators = []

            # Find table separators
            for sep_table in cell.find_all('table'):
                sep_text = sep_table.get_text().strip()
                for keyword, faction in faction_keywords.items():
                    if keyword in sep_text.lower() or f'{keyword} units' in sep_text.lower():
                        faction_separators.append((sep_table, faction))
                        break

            # Find paragraph separators (like "Mercenary (Non Faction)")
            for para in cell.find_all('p'):
                para_text = para.get_text().strip()
                # Check for mercenary specifically
                if 'non faction' in para_text.lower() or 'mercenary' in para_text.lower():
                    faction_separators.append((para, 'mercenary'))
                    continue
                # Check other factions
                for keyword, faction in faction_keywords.items():
                    if keyword in para_text.lower():
                        faction_separators.append((para, faction))
                        break

            if not faction_separators:
                # No separators, check if cell header indicates faction
                cell_text = cell.get_text()
                for keyword, faction in faction_keywords.items():
                    if keyword + ' units' in cell_text.lower()[:100]:
                        faction_separators.append((None, faction))
                        break

            if not faction_separators:
                continue

            # Get all content as a list of elements
            cell_elements = list(cell.children)

            # Process each faction section
            for i, (separator, current_faction) in enumerate(faction_separators):
                self.log(f"Processing faction: {current_faction}")

                if separator:
                    # Find the separator's position in the cell
                    try:
                        sep_idx = cell_elements.index(separator)
                    except ValueError:
                        continue

                    # Get content between this separator and the next
                    next_sep_idx = len(cell_elements)
                    if i + 1 < len(faction_separators):
                        next_sep, _ = faction_separators[i + 1]
                        try:
                            next_sep_idx = cell_elements.index(next_sep)
                        except ValueError:
                            pass

                    # Extract text and links from this faction's section
                    section_elements = cell_elements[sep_idx + 1:next_sep_idx]
                else:
                    # No separator, use whole cell
                    section_elements = cell_elements

                # Build section text for rank detection
                section_text = ''.join(str(elem) for elem in section_elements)
                section_soup = BeautifulSoup(section_text, 'html.parser')
                section_text_plain = section_soup.get_text()

                # Find all links in this section
                for link in section_soup.find_all('a'):
                    href = link.get('href', '')

                    # Skip non-wiki links, images, and faction/category links
                    if (not href.startswith('/wiki/') or
                        'File:' in href or
                        'Category:' in href or
                        'Symbol' in href):
                        continue

                    name = link.get_text().strip()

                    # Skip faction headers and empty names
                    if not name or name.lower() in faction_keywords.keys():
                        continue

                    # Determine rank by looking backwards in section text
                    link_position = section_text_plain.find(name)
                    if link_position == -1:
                        continue

                    text_before = section_text_plain[:link_position].lower()
                    found_rank = None
                    max_pos = -1

                    for rank_check in rank_keywords:
                        pos = text_before.rfind(rank_check)
                        if pos > max_pos:
                            max_pos = pos
                            found_rank = rank_check

                    if found_rank and current_faction:
                        url = self.BASE_URL + href
                        # Avoid duplicates
                        if (name, url) not in units[current_faction][found_rank]:
                            units[current_faction][found_rank].append((name, url))
                            self.log(f"  [{current_faction}] {found_rank}: {name}")

        return dict(units)

    def parse_dice_pool(self, text: str) -> Tuple[List[int], Dict[str, int]]:
        """
        Parse dice notation from wiki text
        Returns: ([white, black, red], {keyword: value})
        """
        dice = [0, 0, 0]  # [white, black, red]
        keywords = {}

        if not text:
            return dice, keywords

        # Look for dice icons and numbers
        # Common patterns: "2 red", "1 white 1 black", etc.
        for color_name, color_idx in self.DICE_COLOR_MAP.items():
            # Match patterns like "2 red" or "red: 2"
            pattern = rf'(\d+)\s*{color_name}|{color_name}\s*:?\s*(\d+)'
            matches = re.findall(pattern, text.lower())
            for match in matches:
                count = int(match[0] or match[1])
                dice[color_idx] = count

        # Parse weapon keywords with values
        keyword_pattern = r'(impact|pierce|critical|blast|lethal|suppressive|scatter)\s*(\d+)?'
        for match in re.finditer(keyword_pattern, text.lower()):
            keyword = match.group(1)
            value = int(match.group(2)) if match.group(2) else 1
            keywords[keyword] = value

        return dice, keywords

    def parse_weapons_from_infobox(self, weapon_elem) -> List[Dict]:
        """Parse weapons from the infobox weapon element"""
        weapons = []

        # Get the HTML content
        html_str = str(weapon_elem)

        # Split by weapon (weapons are separated by <br> tags and have bold names)
        # Strategy: find all bold spans, each one is likely a weapon name
        bold_spans = weapon_elem.find_all('span', {'style': re.compile(r'font-weight\s*:\s*bold', re.I)})

        current_weapon = None

        for span in bold_spans:
            span_text = span.get_text().strip()

            # Check if this looks like a keyword line (Impact 2, Pierce 2, etc.)
            # Keywords are ONLY keywords with numbers, not weapon names
            is_keyword_line = False

            # Check if it's a pure keyword line (e.g., "Impact 2, Pierce 2")
            if re.match(r'^[A-Z][a-z]+\s+\d+(\s*,\s*[A-Z][a-z]+\s+\d+)*$', span_text):
                is_keyword_line = True
            # Or just a single keyword without number (less common)
            elif span_text.lower() in ['impact', 'pierce', 'blast', 'critical', 'lethal', 'suppressive', 'scatter', 'versatile']:
                is_keyword_line = True
            # Check if it contains keywords but is NOT a weapon name
            elif any(kw in span_text.lower() for kw in ['impact', 'pierce', 'blast', 'critical', 'lethal', 'suppressive']):
                # Make sure it's not a weapon name (weapon names usually contain weapon-type words)
                weapon_indicators = ['blaster', 'lightsaber', 'cannon', 'rifle', 'pistol', 'sword', 'staff', 'bow', 'blade', 'gun', 'laser']
                if not any(indicator in span_text.lower() for indicator in weapon_indicators):
                    is_keyword_line = True

            if is_keyword_line:
                # This is a keywords line for the current weapon
                if current_weapon:
                    # Parse keywords
                    keywords = {}
                    for match in re.finditer(r'([A-Za-z]+)\s+(\d+)', span_text):
                        keyword = match.group(1).lower()
                        value = int(match.group(2))
                        keywords[keyword] = value
                    current_weapon['keywords'].update(keywords)
            else:
                # This is a new weapon name
                # Save previous weapon if exists
                if current_weapon:
                    weapons.append(current_weapon)

                # Start new weapon
                current_weapon = {
                    'name': span_text,
                    'dice': [0, 0, 0],
                    'range': '',
                    'keywords': {},
                    'warnings': []
                }

                # Look for range and dice after this span
                # Get parent and subsequent siblings
                parent = span.parent
                siblings_html = ''
                if parent:
                    # Get next elements until we hit another weapon name
                    next_elem = span.find_next()
                    search_count = 0
                    found_dice_count = 0

                    while next_elem and search_count < 20:
                        elem_text = next_elem.get_text().strip()

                        # Check if we hit another weapon name (bold span that's not a keyword)
                        if next_elem.name == 'span' and next_elem.get('style') and 'bold' in next_elem.get('style', ''):
                            # Check if this is a weapon name (not keywords)
                            is_next_weapon = False
                            next_text = next_elem.get_text().strip()

                            # Check if it's a weapon name pattern
                            weapon_indicators = ['blaster', 'lightsaber', 'cannon', 'rifle', 'pistol', 'sword', 'staff', 'bow', 'blade', 'gun', 'laser', "'s", 'trooper']
                            if any(indicator in next_text.lower() for indicator in weapon_indicators):
                                is_next_weapon = True
                            # Or if it's not a pure keyword pattern
                            elif not re.match(r'^[A-Z][a-z]+\s+\d+(\s*,\s*[A-Z][a-z]+\s+\d+)*$', next_text):
                                is_next_weapon = True

                            if is_next_weapon:
                                break

                        # Look for range (only if we haven't found it yet)
                        if not current_weapon['range'] and 'range:' in elem_text.lower():
                            range_match = re.search(r'range:\s*(\d+-\d+|melee|\d+)', elem_text.lower())
                            if range_match:
                                current_weapon['range'] = range_match.group(1)

                        # Look for dice images
                        if next_elem.name == 'img' or (next_elem.name in ['span', 'a'] and next_elem.find('img')):
                            img = next_elem.find('img') if next_elem.name != 'img' else next_elem
                            if img:
                                img_name = img.get('data-image-name', '').lower()

                                # Determine dice color
                                dice_color = None
                                if 'attack_die_white' in img_name or 'attack die white' in img_name:
                                    dice_color = 0  # white
                                elif 'attack_die_black' in img_name or 'attack die black' in img_name:
                                    dice_color = 1  # black
                                elif 'attack_die_red' in img_name or 'attack die red' in img_name:
                                    dice_color = 2  # red

                                if dice_color is not None:
                                    # Get the number after the image
                                    next_text = next_elem.next_sibling
                                    if next_text and isinstance(next_text, str):
                                        # Extract number from text
                                        num_match = re.search(r'(\d+)', next_text)
                                        if num_match:
                                            count = int(num_match.group(1))
                                            current_weapon['dice'][dice_color] = count
                                            found_dice_count += 1

                                            # Stop after finding first set of dice for this weapon
                                            # (most weapons have one dice type)
                                            if found_dice_count >= 3:  # Max types of dice (white, black, red)
                                                break

                        next_elem = next_elem.find_next()
                        search_count += 1

                # Validate weapon data
                if current_weapon['dice'] == [0, 0, 0]:
                    current_weapon['warnings'].append("No dice pool found")
                if not current_weapon['range']:
                    current_weapon['warnings'].append("No range found")

        # Add the last weapon
        if current_weapon:
            weapons.append(current_weapon)

        return weapons

    def parse_weapon(self, weapon_elem) -> Optional[Dict]:
        """Parse a weapon from wiki text (legacy method)"""
        weapon_data = {
            'name': '',
            'dice': [0, 0, 0],
            'range': '',
            'keywords': {},
            'warnings': []
        }

        # Try to extract weapon name (usually in bold or as header)
        name_elem = weapon_elem.find(['b', 'strong']) or weapon_elem
        weapon_data['name'] = name_elem.get_text().strip()

        # Get all text for parsing
        full_text = weapon_elem.get_text()

        # Parse range
        range_match = re.search(r'range:?\s*(\d+-\d+|melee|\d+)', full_text.lower())
        if range_match:
            weapon_data['range'] = range_match.group(1)
        else:
            weapon_data['warnings'].append("Could not parse weapon range")

        # Parse dice pool and keywords
        dice, keywords = self.parse_dice_pool(full_text)
        weapon_data['dice'] = dice
        weapon_data['keywords'] = keywords

        # Warn if no dice found
        if dice == [0, 0, 0]:
            weapon_data['warnings'].append("No dice pool found")

        return weapon_data

    def scrape_unit(self, name: str, url: str, faction: str, rank: str) -> Optional[Dict]:
        """Scrape a single unit page"""
        self.log(f"Scraping unit: {name}")

        soup = self.fetch_page(url)
        if not soup:
            self.units_skipped += 1
            return None

        unit_data = {
            'name': name,
            'faction': faction,
            'rank': rank,
            'size': 1,
            'weapons': [],
            'defense_die': 'white',
            'surge_hit': False,
            'surge_crit': False,
            'surge_block': False,
            'armor': 0,
            'shields': 0,
            'dodges': 0,
            'impervious': False,
            'immune_pierce': False,
            'cover_improvement': 0,
            'warnings': []
        }

        # Find the portable infobox
        infobox = soup.find('aside', {'class': 'portable-infobox'})
        if not infobox:
            unit_data['warnings'].append("Could not find infobox")
            self.units_scraped += 1
            self.total_warnings += len(unit_data['warnings'])
            return unit_data

        # Parse minis per unit
        minis_elem = infobox.find('div', {'data-source': 'minis per unit'})
        if minis_elem:
            value_div = minis_elem.find('div', {'class': 'pi-data-value'})
            if value_div:
                try:
                    unit_data['size'] = int(value_div.get_text().strip())
                except ValueError:
                    unit_data['warnings'].append("Could not parse unit size")
        else:
            unit_data['warnings'].append("Could not find unit size")

        # Parse defense die
        defense_elem = infobox.find('div', {'data-source': 'defense'})
        if defense_elem:
            img = defense_elem.find('img')
            if img:
                img_name = img.get('data-image-name', '').lower()
                if 'red' in img_name:
                    unit_data['defense_die'] = 'red'
                elif 'white' in img_name:
                    unit_data['defense_die'] = 'white'
                else:
                    unit_data['warnings'].append(f"Unknown defense die color: {img_name}")
            else:
                unit_data['warnings'].append("Defense die image not found")
        else:
            unit_data['warnings'].append("Could not find defense die")

        # Parse surge conversions
        surge_elem = infobox.find('div', {'data-source': 'surge'})
        if surge_elem:
            # Look for attack surge and what it converts to
            imgs = surge_elem.find_all('img')
            img_names = [img.get('data-image-name', '').lower() for img in imgs]

            # Check if attack surge exists
            if any('attack_surge' in name for name in img_names):
                # Check what it converts to
                if any('critical' in name for name in img_names):
                    unit_data['surge_crit'] = True
                elif any('hit' in name for name in img_names):
                    unit_data['surge_hit'] = True

            # Check for defense surge (block)
            if any('defense_surge' in name or 'block' in name for name in img_names):
                unit_data['surge_block'] = True

        # Parse keywords
        keywords_elem = infobox.find('div', {'data-source': 'keywords'})
        if keywords_elem:
            keywords_text = keywords_elem.get_text().lower()

            # Armor
            armor_match = re.search(r'armor\s*(\d+)?', keywords_text)
            if armor_match:
                unit_data['armor'] = int(armor_match.group(1)) if armor_match.group(1) else 1

            # Shields / Shielded
            shields_match = re.search(r'shield(?:ed)?\s*(\d+)', keywords_text)
            if shields_match:
                unit_data['shields'] = int(shields_match.group(1))

            # Dodge
            dodges_match = re.search(r'dodge\s*(\d+)', keywords_text)
            if dodges_match:
                unit_data['dodges'] = int(dodges_match.group(1))

            # Cover
            cover_match = re.search(r'cover\s*(\d+)', keywords_text)
            if cover_match:
                unit_data['cover_improvement'] = int(cover_match.group(1))

            # Boolean keywords
            if 'impervious' in keywords_text:
                unit_data['impervious'] = True

            if 'immune' in keywords_text and 'pierce' in keywords_text:
                unit_data['immune_pierce'] = True

        # Parse weapons from infobox
        weapon_elem = infobox.find('div', {'data-source': 'weapon'})
        if weapon_elem:
            weapons = self.parse_weapons_from_infobox(weapon_elem)
            unit_data['weapons'] = weapons

            for weapon in weapons:
                if weapon.get('warnings'):
                    unit_data['warnings'].extend(weapon['warnings'])

        if not unit_data['weapons']:
            unit_data['warnings'].append("No weapons found")

        # Look for unit-specific upgrades (heavy weapons, personnel, etc.)
        upgrades = []

        # Find "Unit Specific Upgrades" section in the main content
        content = soup.find('div', {'class': 'mw-parser-output'})
        if content:
            # Look for the header
            for header in content.find_all(['h2', 'h3']):
                header_text = header.get_text().strip()
                if 'unit specific upgrade' in header_text.lower():
                    # Get the next <ul> element
                    next_elem = header.find_next_sibling()
                    while next_elem:
                        if next_elem.name == 'ul':
                            # Found the upgrades list
                            for li in next_elem.find_all('li'):
                                link = li.find('a')
                                if link and link.get('href'):
                                    href = link['href']
                                    if href.startswith('/wiki/') and 'File:' not in href:
                                        link_text = link.get_text().strip()
                                        upgrades.append({
                                            'name': link_text,
                                            'url': self.BASE_URL + href
                                        })
                            break
                        elif next_elem.name in ['h2', 'h3', 'h4']:
                            # Hit another header, stop looking
                            break
                        next_elem = next_elem.find_next_sibling()
                    break

        unit_data['upgrades'] = upgrades

        self.units_scraped += 1
        self.total_warnings += len(unit_data['warnings'])

        return unit_data

    def scrape_upgrade(self, upgrade_name: str, upgrade_url: str) -> Optional[Dict]:
        """Scrape an upgrade card (weapon)"""
        self.log(f"  Scraping upgrade: {upgrade_name}")

        soup = self.fetch_page(upgrade_url)
        if not soup:
            return None

        weapon_data = {
            'name': upgrade_name,
            'dice': [0, 0, 0],
            'range': '',
            'keywords': {},
            'warnings': []
        }

        # Try to find the portable infobox first (same as units)
        infobox = soup.find('aside', {'class': 'portable-infobox'})
        if infobox:
            # Look for weapon info in the infobox
            weapon_elem = infobox.find('div', {'data-source': 'weapon'})
            if weapon_elem:
                weapons = self.parse_weapons_from_infobox(weapon_elem)
                if weapons:
                    # Use the first weapon found
                    first_weapon = weapons[0]
                    weapon_data['dice'] = first_weapon['dice']
                    weapon_data['range'] = first_weapon.get('range', '')
                    weapon_data['keywords'] = first_weapon.get('keywords', {})
                    if first_weapon.get('warnings'):
                        weapon_data['warnings'].extend(first_weapon['warnings'])
                    return weapon_data

        # Fallback: parse from main content
        content = soup.find('div', {'class': 'mw-parser-output'})
        if not content:
            weapon_data['warnings'].append("Could not find page content")
            return weapon_data

        # Look for range in text
        page_text = content.get_text()
        range_match = re.search(r'range:?\s*(\d+-\d+|melee|\d+)', page_text.lower())
        if range_match:
            weapon_data['range'] = range_match.group(1)

        # Look for paragraphs containing "Range:" which have the weapon dice
        for p in content.find_all('p'):
            if 'Range:' not in p.get_text():
                continue

            # Find dice images in this paragraph
            # Images are wrapped in <span typeof="mw:File"><a><img/></a></span>
            # The number comes right after the </span> tag
            for span in p.find_all('span', {'typeof': 'mw:File'}):
                # Find the dice image inside this span
                img = span.find('img')
                if not img:
                    continue

                img_name = img.get('data-image-name', '').lower()

                # Determine dice color
                dice_color = None
                if 'attack_die_white' in img_name or 'attack die white' in img_name:
                    dice_color = 0
                elif 'attack_die_black' in img_name or 'attack die black' in img_name:
                    dice_color = 1
                elif 'attack_die_red' in img_name or 'attack die red' in img_name:
                    dice_color = 2

                if dice_color is not None:
                    # Get number after the span (not the image)
                    next_text = span.next_sibling
                    if next_text and isinstance(next_text, str):
                        num_match = re.search(r'(\d+)', next_text)
                        if num_match:
                            count = int(num_match.group(1))
                            weapon_data['dice'][dice_color] = count

        # Parse keywords from text
        keywords = {}
        for match in re.finditer(r'(impact|pierce|critical|blast|lethal|suppressive|scatter)\s*(\d+)?', page_text.lower()):
            keyword = match.group(1)
            value = int(match.group(2)) if match.group(2) else 1
            keywords[keyword] = value

        weapon_data['keywords'] = keywords

        if weapon_data['dice'] == [0, 0, 0]:
            weapon_data['warnings'].append("No dice pool found in upgrade")

        return weapon_data

    def scrape_faction(self, faction: str, units_dict: Dict[str, List[Tuple[str, str]]]) -> Dict[str, Dict]:
        """Scrape all units for a faction"""
        print(f"\n{'='*60}")
        print(f"Scraping {faction.upper()} units...")
        print(f"{'='*60}\n")

        faction_data = {}

        for rank, units in units_dict.items():
            print(f"\n{rank.upper()}:")
            for name, url in units:
                unit_data = self.scrape_unit(name, url, faction, rank)
                if unit_data:
                    # Generate unit_id (lowercase, no spaces)
                    unit_id = re.sub(r'[^a-z0-9]', '', name.lower().replace(' ', ''))

                    # Scrape upgrades if present
                    if unit_data.get('upgrades'):
                        for upgrade in unit_data['upgrades']:
                            if upgrade.get('url'):
                                weapon = self.scrape_upgrade(upgrade['name'], upgrade['url'])
                                if weapon and weapon['dice'] != [0, 0, 0]:
                                    # Only add upgrades with actual weapons (non-zero dice)
                                    unit_data['weapons'].append(weapon)

                    # Remove upgrades list from final output (already processed)
                    unit_data.pop('upgrades', None)

                    faction_data[unit_id] = unit_data

                    # Print summary
                    status = "✓" if not unit_data['warnings'] else "⚠"
                    print(f"  {status} {name}")
                    if unit_data['warnings'] and self.verbose:
                        for warning in unit_data['warnings']:
                            print(f"      - {warning}")

        return faction_data

    def run(self, specific_faction: Optional[str] = None):
        """Main scraping routine"""
        print(f"\n{'='*60}")
        print("Star Wars Legion Wiki Scraper")
        print(f"{'='*60}\n")

        # Get unit list
        all_units = self.get_unit_list()

        if not all_units:
            print("ERROR: Failed to get unit list")
            return

        print(f"\nFound {sum(len(ranks) for ranks in all_units.values())} ranks across {len(all_units)} factions")

        # Scrape each faction
        factions_to_scrape = [specific_faction] if specific_faction else all_units.keys()

        for faction in factions_to_scrape:
            if faction not in all_units:
                print(f"WARNING: Faction '{faction}' not found in unit list")
                continue

            faction_data = self.scrape_faction(faction, all_units[faction])

            # Save to JSON
            output_file = f"{faction}_units.json"
            with open(output_file, 'w') as f:
                json.dump(faction_data, f, indent=2)

            print(f"\n✓ Saved {len(faction_data)} units to {output_file}")

        # Print summary
        print(f"\n{'='*60}")
        print("SUMMARY")
        print(f"{'='*60}")
        print(f"Units scraped: {self.units_scraped}")
        print(f"Units skipped: {self.units_skipped}")
        print(f"Total warnings: {self.total_warnings}")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description='Scrape Star Wars Legion wiki for unit data')
    parser.add_argument('--faction', type=str, help='Scrape only this faction (empire, rebel, republic, separatist, mercenary)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--rate-limit', type=float, default=1.0, help='Delay between requests in seconds (default: 1.0)')

    args = parser.parse_args()

    scraper = LegionWikiScraper(verbose=args.verbose, rate_limit=args.rate_limit)
    scraper.run(specific_faction=args.faction)


if __name__ == '__main__':
    main()
