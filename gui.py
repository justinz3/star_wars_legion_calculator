"""
Star Wars Legion Probability Calculator - GUI
A graphical interface for calculating attack probabilities in SW Legion
"""

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QPushButton, QSpinBox, QCheckBox,
                             QListWidget, QGroupBox, QGridLayout, QSizePolicy)
from PyQt6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from unit_registry import get_units_by_faction, get_unit_weapons, UNIT_TYPES
from unit import Unit
from constants import COVER_NONE, COVER_LIGHT, COVER_HEAVY


class MplCanvas(FigureCanvas):
    """Matplotlib canvas widget for embedding charts in PyQt"""
    def __init__(self, parent=None, width=12, height=8, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        # Don't create axes here - they'll be created dynamically in update_chart
        super(MplCanvas, self).__init__(self.figure)


class LegionCalculatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.units_by_faction = get_units_by_faction()
        self.attackers = []  # List of (unit_id, weapon_index, mini_count)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Star Wars Legion - Probability Calculator')
        self.setGeometry(100, 100, 1200, 900)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Top: Controls
        controls_widget = self.create_controls()
        main_layout.addWidget(controls_widget)

        # Middle: Graph Options
        options_widget = self.create_graph_options()
        main_layout.addWidget(options_widget)

        # Bottom: Chart
        self.canvas = MplCanvas(self, width=12, height=8, dpi=100)
        main_layout.addWidget(self.canvas)

        # Initialize with empty chart
        ax = self.canvas.figure.add_subplot(111)
        ax.set_xlabel('Damage')
        ax.set_ylabel('Probability (%)')
        ax.set_title('Select units and click Calculate')
        self.canvas.draw()

    def create_controls(self):
        """Create the control panel"""
        controls = QWidget()
        layout = QHBoxLayout()
        controls.setLayout(layout)

        # Left: Attacker selection
        attacker_group = self.create_attacker_panel()
        layout.addWidget(attacker_group)

        # Middle: Defender selection
        defender_group = self.create_defender_panel()
        layout.addWidget(defender_group)

        # Right: Modifiers
        modifiers_group = self.create_modifiers_panel()
        layout.addWidget(modifiers_group)

        return controls

    def create_attacker_panel(self):
        """Create attacker selection panel"""
        group = QGroupBox("Attackers")
        layout = QVBoxLayout()

        # Faction dropdown
        faction_layout = QHBoxLayout()
        faction_layout.addWidget(QLabel("Faction:"))
        self.attacker_faction = QComboBox()
        self.attacker_faction.addItems(['Republic', 'Separatist', 'Empire', 'Rebel'])
        self.attacker_faction.currentTextChanged.connect(self.update_attacker_types)
        faction_layout.addWidget(self.attacker_faction)
        layout.addLayout(faction_layout)

        # Type dropdown
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type:"))
        self.attacker_type = QComboBox()
        self.attacker_type.currentTextChanged.connect(self.update_attacker_units)
        type_layout.addWidget(self.attacker_type)
        layout.addLayout(type_layout)

        # Unit dropdown
        unit_layout = QHBoxLayout()
        unit_layout.addWidget(QLabel("Unit:"))
        self.attacker_unit = QComboBox()
        self.attacker_unit.currentTextChanged.connect(self.update_attacker_weapons)
        unit_layout.addWidget(self.attacker_unit)
        layout.addLayout(unit_layout)

        # Weapon dropdown
        weapon_layout = QHBoxLayout()
        weapon_layout.addWidget(QLabel("Weapon:"))
        self.attacker_weapon = QComboBox()
        weapon_layout.addWidget(self.attacker_weapon)
        layout.addLayout(weapon_layout)

        # Mini count spinbox
        minis_layout = QHBoxLayout()
        minis_layout.addWidget(QLabel("Minis:"))
        self.attacker_minis_spin = QSpinBox()
        self.attacker_minis_spin.setRange(1, 10)
        self.attacker_minis_spin.setValue(1)
        minis_layout.addWidget(self.attacker_minis_spin)
        layout.addLayout(minis_layout)

        # Add button
        add_btn = QPushButton("Add Attacker")
        add_btn.clicked.connect(self.add_attacker)
        layout.addWidget(add_btn)

        # List of attackers
        layout.addWidget(QLabel("Current Attackers:"))
        self.attacker_list = QListWidget()
        self.attacker_list.setMaximumHeight(150)
        layout.addWidget(self.attacker_list)

        # Remove button
        remove_btn = QPushButton("Remove Selected")
        remove_btn.clicked.connect(self.remove_attacker)
        layout.addWidget(remove_btn)

        group.setLayout(layout)

        # Initialize
        self.update_attacker_types()

        return group

    def create_defender_panel(self):
        """Create defender selection panel"""
        group = QGroupBox("Defender")
        layout = QVBoxLayout()

        # Faction dropdown
        faction_layout = QHBoxLayout()
        faction_layout.addWidget(QLabel("Faction:"))
        self.defender_faction = QComboBox()
        self.defender_faction.addItems(['Republic', 'Separatist', 'Empire', 'Rebel'])
        self.defender_faction.currentTextChanged.connect(self.update_defender_types)
        faction_layout.addWidget(self.defender_faction)
        layout.addLayout(faction_layout)

        # Type dropdown
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type:"))
        self.defender_type = QComboBox()
        self.defender_type.currentTextChanged.connect(self.update_defender_units)
        type_layout.addWidget(self.defender_type)
        layout.addLayout(type_layout)

        # Unit dropdown
        unit_layout = QHBoxLayout()
        unit_layout.addWidget(QLabel("Unit:"))
        self.defender_unit = QComboBox()
        unit_layout.addWidget(self.defender_unit)
        layout.addLayout(unit_layout)

        group.setLayout(layout)

        # Initialize
        self.update_defender_types()

        return group

    def create_modifiers_panel(self):
        """Create modifiers input panel with collapsible sections"""
        group = QGroupBox("Modifiers")
        layout = QVBoxLayout()

        # Attack Modifiers Section
        self.attack_mods_check = QCheckBox("Attack Modifiers")
        self.attack_mods_check.stateChanged.connect(self.toggle_attack_modifiers)
        layout.addWidget(self.attack_mods_check)

        self.attack_mods_widget = QWidget()
        attack_layout = QGridLayout()
        row = 0

        self.aims_spin = QSpinBox()
        self.aims_spin.setRange(0, 10)
        attack_layout.addWidget(QLabel("Aims:"), row, 0)
        attack_layout.addWidget(self.aims_spin, row, 1)
        row += 1

        self.precise_spin = QSpinBox()
        self.precise_spin.setRange(0, 10)
        attack_layout.addWidget(QLabel("Precise:"), row, 0)
        attack_layout.addWidget(self.precise_spin, row, 1)
        row += 1

        self.criticals_spin = QSpinBox()
        self.criticals_spin.setRange(0, 10)
        attack_layout.addWidget(QLabel("Criticals:"), row, 0)
        attack_layout.addWidget(self.criticals_spin, row, 1)
        row += 1

        self.hit_surges_spin = QSpinBox()
        self.hit_surges_spin.setRange(0, 10)
        attack_layout.addWidget(QLabel("Hit Surges:"), row, 0)
        attack_layout.addWidget(self.hit_surges_spin, row, 1)
        row += 1

        self.impacts_spin = QSpinBox()
        self.impacts_spin.setRange(0, 10)
        attack_layout.addWidget(QLabel("Impacts:"), row, 0)
        attack_layout.addWidget(self.impacts_spin, row, 1)
        row += 1

        self.pierce_spin = QSpinBox()
        self.pierce_spin.setRange(-5, 10)
        attack_layout.addWidget(QLabel("Pierce:"), row, 0)
        attack_layout.addWidget(self.pierce_spin, row, 1)
        row += 1

        self.improvements_spin = QSpinBox()
        self.improvements_spin.setRange(0, 10)
        attack_layout.addWidget(QLabel("Improvements:"), row, 0)
        attack_layout.addWidget(self.improvements_spin, row, 1)

        self.attack_mods_widget.setLayout(attack_layout)
        self.attack_mods_widget.setVisible(False)
        layout.addWidget(self.attack_mods_widget)

        # Defense Modifiers Section
        self.defense_mods_check = QCheckBox("Defense Modifiers")
        self.defense_mods_check.stateChanged.connect(self.toggle_defense_modifiers)
        layout.addWidget(self.defense_mods_check)

        self.defense_mods_widget = QWidget()
        defense_layout = QGridLayout()
        row = 0

        self.dodges_spin = QSpinBox()
        self.dodges_spin.setRange(0, 10)
        defense_layout.addWidget(QLabel("Dodges:"), row, 0)
        defense_layout.addWidget(self.dodges_spin, row, 1)
        row += 1

        self.cover_combo = QComboBox()
        self.cover_combo.addItems(['None', 'Light', 'Heavy'])
        defense_layout.addWidget(QLabel("Cover:"), row, 0)
        defense_layout.addWidget(self.cover_combo, row, 1)
        row += 1

        self.shields_spin = QSpinBox()
        self.shields_spin.setRange(0, 10)
        defense_layout.addWidget(QLabel("Shields:"), row, 0)
        defense_layout.addWidget(self.shields_spin, row, 1)
        row += 1

        self.def_surges_spin = QSpinBox()
        self.def_surges_spin.setRange(0, 10)
        defense_layout.addWidget(QLabel("Defense Surges:"), row, 0)
        defense_layout.addWidget(self.def_surges_spin, row, 1)

        self.defense_mods_widget.setLayout(defense_layout)
        self.defense_mods_widget.setVisible(False)
        layout.addWidget(self.defense_mods_widget)

        # Special Mechanics Section
        self.special_mods_check = QCheckBox("Special Mechanics")
        self.special_mods_check.stateChanged.connect(self.toggle_special_modifiers)
        layout.addWidget(self.special_mods_check)

        self.special_mods_widget = QWidget()
        special_layout = QVBoxLayout()

        self.ignore_dodges_check = QCheckBox("Ignore Dodges (High Velocity)")
        special_layout.addWidget(self.ignore_dodges_check)

        self.bypass_pierce_check = QCheckBox("Bypass Immune Pierce (Makashi)")
        special_layout.addWidget(self.bypass_pierce_check)

        self.special_mods_widget.setLayout(special_layout)
        self.special_mods_widget.setVisible(False)
        layout.addWidget(self.special_mods_widget)

        # Calculate button (always visible)
        calc_btn = QPushButton("CALCULATE")
        calc_btn.setStyleSheet("QPushButton { font-size: 16px; font-weight: bold; padding: 10px; }")
        calc_btn.clicked.connect(self.calculate)
        layout.addWidget(calc_btn)

        group.setLayout(layout)
        return group

    def toggle_attack_modifiers(self, state):
        """Show/hide attack modifiers section"""
        self.attack_mods_widget.setVisible(state == 2)

    def toggle_defense_modifiers(self, state):
        """Show/hide defense modifiers section"""
        self.defense_mods_widget.setVisible(state == 2)

    def toggle_special_modifiers(self, state):
        """Show/hide special mechanics section"""
        self.special_mods_widget.setVisible(state == 2)

    def create_graph_options(self):
        """Create graph display options panel"""
        group = QGroupBox("Graph Options")
        layout = QVBoxLayout()

        # Main output "At Least X" toggle
        main_layout = QHBoxLayout()
        main_layout.addWidget(QLabel("<b>Final Output:</b>"))
        self.show_main_at_least = QCheckBox("Show 'At Least X Damage'")
        self.show_main_at_least.setChecked(True)  # On by default
        self.show_main_at_least.stateChanged.connect(self.calculate)
        main_layout.addWidget(self.show_main_at_least)
        main_layout.addStretch()
        layout.addLayout(main_layout)

        # Attack distribution displays
        layout.addWidget(QLabel("<b>Attack Distributions:</b>"))

        attack_layout = QHBoxLayout()

        # Attack Composition
        comp_layout = QVBoxLayout()
        self.show_attack_comp = QCheckBox("Attack Composition")
        self.show_attack_comp.stateChanged.connect(self.calculate)
        comp_layout.addWidget(self.show_attack_comp)
        self.show_attack_comp_at_least = QCheckBox("  └ At Least X")
        self.show_attack_comp_at_least.stateChanged.connect(self.calculate)
        comp_layout.addWidget(self.show_attack_comp_at_least)
        attack_layout.addLayout(comp_layout)

        # 2D Heatmap
        self.show_heatmap = QCheckBox("2D Attack Heatmap")
        self.show_heatmap.stateChanged.connect(self.calculate)
        attack_layout.addWidget(self.show_heatmap)

        attack_layout.addStretch()
        layout.addLayout(attack_layout)

        # Intermediate distributions (following game sequence)
        layout.addWidget(QLabel("<b>Game Sequence:</b>"))

        intermediates_layout = QHBoxLayout()

        # After Cover + Dodges
        cover_dodge_layout = QVBoxLayout()
        self.show_after_cover_dodges = QCheckBox("After Cover + Dodges")
        self.show_after_cover_dodges.stateChanged.connect(self.calculate)
        cover_dodge_layout.addWidget(self.show_after_cover_dodges)
        self.show_cover_dodges_at_least = QCheckBox("  └ At Least X")
        self.show_cover_dodges_at_least.stateChanged.connect(self.calculate)
        cover_dodge_layout.addWidget(self.show_cover_dodges_at_least)
        intermediates_layout.addLayout(cover_dodge_layout)

        # After Armor & Shields (Modify Attack)
        armor_layout = QVBoxLayout()
        self.show_after_armor = QCheckBox("After Armor & Shields")
        self.show_after_armor.stateChanged.connect(self.calculate)
        armor_layout.addWidget(self.show_after_armor)
        self.show_armor_at_least = QCheckBox("  └ At Least X")
        self.show_armor_at_least.stateChanged.connect(self.calculate)
        armor_layout.addWidget(self.show_armor_at_least)
        intermediates_layout.addLayout(armor_layout)

        # After Defense Dice
        defense_layout = QVBoxLayout()
        self.show_after_defense = QCheckBox("After Defense Dice")
        self.show_after_defense.stateChanged.connect(self.calculate)
        defense_layout.addWidget(self.show_after_defense)
        self.show_defense_at_least = QCheckBox("  └ At Least X")
        self.show_defense_at_least.stateChanged.connect(self.calculate)
        defense_layout.addWidget(self.show_defense_at_least)
        intermediates_layout.addLayout(defense_layout)

        intermediates_layout.addStretch()
        layout.addLayout(intermediates_layout)

        group.setLayout(layout)
        return group

    def update_attacker_types(self):
        """Update attacker type dropdown based on selected faction"""
        faction = self.attacker_faction.currentText()
        self.attacker_type.clear()

        for unit_type in UNIT_TYPES:
            units = self.units_by_faction[faction].get(unit_type, [])
            if units:  # Only add types that have units
                self.attacker_type.addItem(unit_type)

    def update_attacker_units(self):
        """Update attacker unit dropdown based on selected type"""
        faction = self.attacker_faction.currentText()
        unit_type = self.attacker_type.currentText()

        self.attacker_unit.clear()
        units = self.units_by_faction[faction].get(unit_type, [])
        for unit_id, unit_name in units:
            self.attacker_unit.addItem(unit_name, unit_id)

    def update_attacker_weapons(self):
        """Update attacker weapon dropdown based on selected unit"""
        if self.attacker_unit.count() == 0:
            return

        unit_id = self.attacker_unit.currentData()
        if unit_id is None:
            return

        self.attacker_weapon.clear()
        weapons = get_unit_weapons(unit_id)
        for i, weapon_name in enumerate(weapons):
            self.attacker_weapon.addItem(weapon_name, i)

        # Auto-populate mini count with unit's default size
        unit = Unit(unit_id)
        self.attacker_minis_spin.setValue(unit.size)

    def update_defender_types(self):
        """Update defender type dropdown based on selected faction"""
        faction = self.defender_faction.currentText()
        self.defender_type.clear()

        for unit_type in UNIT_TYPES:
            units = self.units_by_faction[faction].get(unit_type, [])
            if units:
                self.defender_type.addItem(unit_type)

    def update_defender_units(self):
        """Update defender unit dropdown based on selected type"""
        faction = self.defender_faction.currentText()
        unit_type = self.defender_type.currentText()

        self.defender_unit.clear()
        units = self.units_by_faction[faction].get(unit_type, [])
        for unit_id, unit_name in units:
            self.defender_unit.addItem(unit_name, unit_id)

    def convert_attack_to_wounds(self, attack_distribution):
        """Convert 2D attack distribution (hits, crits) to 1D wound distribution (no defense)"""
        max_wounds = len(attack_distribution) - 1 + len(attack_distribution[0]) - 1
        wound_dist = [0.0] * (max_wounds + 1)

        for i in range(len(attack_distribution)):  # hits
            for j in range(len(attack_distribution[i]) - i):  # crits
                wounds = i + j
                wound_dist[wounds] += attack_distribution[i][j]

        return wound_dist

    def apply_cover_dodges_2d(self, attack_distribution, defender, cover_level, dodges, ignore_dodges=False):
        """
        Apply cover (probabilistic) and dodges (deterministic) to 2D attack distribution.
        Returns 2D distribution [hits][crits].
        """
        from constants import COVER_NONE

        # Apply unit's cover improvement
        cover_level = min(cover_level + defender.cover_improvement, COVER_HEAVY)
        effective_dodges = 0 if ignore_dodges else (dodges + defender.dodges)

        # Determine max dimensions
        max_hits = len(attack_distribution) - 1
        max_crits = max(len(attack_distribution[h]) - h - 1 for h in range(len(attack_distribution)))

        # Initialize output 2D distribution
        result = [[0.0 for _ in range(max_crits + 1)] for _ in range(max_hits + 1)]

        for hits in range(len(attack_distribution)):
            for crits in range(len(attack_distribution[hits]) - hits):
                prob = attack_distribution[hits][crits]
                if prob == 0:
                    continue

                # Apply cover (probabilistic)
                if cover_level == COVER_NONE:
                    cover_dist = [1.0 if i == 0 else 0.0 for i in range(hits + 1)]
                else:
                    cover_dist = Unit.get_cover_cancellation_distribution(hits, cover_level)

                for hits_cancelled, cover_prob in enumerate(cover_dist):
                    if cover_prob == 0:
                        continue

                    remaining_hits = hits - hits_cancelled

                    # Apply dodges (deterministic)
                    remaining_hits = max(0, remaining_hits - effective_dodges)

                    # Add to result distribution
                    if remaining_hits <= max_hits and crits <= max_crits:
                        result[remaining_hits][crits] += prob * cover_prob

        return result

    def apply_armor_shields_1d(self, attack_distribution_2d, defender, shields):
        """
        Apply armor and shields to 2D attack distribution, converting to 1D wounds.
        This is the 'Modify Attack Dice' step.
        """
        effective_shields = shields + defender.shields

        max_wounds = len(attack_distribution_2d) - 1 + max(len(attack_distribution_2d[h]) - h - 1 for h in range(len(attack_distribution_2d)))
        wound_dist = [0.0] * (max_wounds + 1)

        for hits in range(len(attack_distribution_2d)):
            for crits in range(len(attack_distribution_2d[hits]) - hits):
                prob = attack_distribution_2d[hits][crits]
                if prob == 0:
                    continue

                # Apply armor (reduces hits)
                remaining_hits = max(0, hits - defender.armor)

                # Apply shields (cancel crits first, then hits)
                remaining_crits = max(0, crits - effective_shields)
                shields_for_hits = max(0, effective_shields - crits)
                remaining_hits = max(0, remaining_hits - shields_for_hits)

                total_wounds = remaining_hits + remaining_crits
                wound_dist[total_wounds] += prob

        return wound_dist

    def apply_defense_dice_1d(self, wound_distribution_1d, defender, defense_surges, pierce, bypass_immune_pierce=False):
        """
        Apply defense dice rolling to 1D wound distribution.
        This is the 'Roll Defense Dice' and 'Modify Defense Dice' steps combined.
        """
        from math import comb
        from dice import NUM_DEFENSE_DICE_FACES

        max_wounds = len(wound_distribution_1d) - 1
        final_dist = [0.0] * (max_wounds + 1)

        for incoming_wounds, prob_incoming in enumerate(wound_distribution_1d):
            if prob_incoming == 0:
                continue

            # Roll defense dice
            total_dice = incoming_wounds + pierce if defender.impervious else incoming_wounds
            probability_blank = defender.saves[0] / NUM_DEFENSE_DICE_FACES
            probability_block = defender.saves[1] / NUM_DEFENSE_DICE_FACES
            probability_surge = defender.saves[2] / NUM_DEFENSE_DICE_FACES

            for blanks in range(total_dice + 1):
                for blocks in range(total_dice + 1 - blanks):
                    surges = total_dice - blanks - blocks
                    total_blocks = blocks + min(defense_surges + defender.defense_surges, surges)

                    # Apply pierce to blocks (can bypass Immune: Pierce with Makashi Mastery)
                    is_immune_to_pierce = defender.immune_pierce and not bypass_immune_pierce
                    total_blocks = total_blocks if is_immune_to_pierce else max(0, total_blocks - pierce)
                    total_blocks = min(total_blocks, incoming_wounds)

                    save_probability = comb(total_dice, blanks + blocks) * comb(blanks + blocks, blanks) * \
                        (probability_blank ** blanks) * (probability_block ** blocks) * (probability_surge ** surges)

                    wounds = incoming_wounds - total_blocks
                    final_dist[wounds] += prob_incoming * save_probability

        return final_dist

    def apply_cover_and_dodges(self, attack_distribution, defender, cover_level, dodges, ignore_dodges=False):
        """Apply cover, then dodges+armor (deterministic)"""
        # First apply cover
        cover_level = min(cover_level + defender.cover_improvement, COVER_HEAVY)

        max_wounds = len(attack_distribution) - 1 + len(attack_distribution[0]) - 1
        wound_dist = [0.0] * (max_wounds + 1)

        # Add defender's inherent dodges
        effective_dodges = 0 if ignore_dodges else (dodges + defender.dodges)

        for hits in range(len(attack_distribution)):
            for crits in range(len(attack_distribution[hits]) - hits):
                prob = attack_distribution[hits][crits]
                if prob == 0:
                    continue

                # Apply cover
                cover_dist = Unit.get_cover_cancellation_distribution(hits, cover_level)

                for hits_cancelled, cover_prob in enumerate(cover_dist):
                    if cover_prob == 0:
                        continue
                    remaining_hits = hits - hits_cancelled

                    # Apply dodges and armor (deterministic)
                    remaining_hits = max(0, remaining_hits - effective_dodges - defender.armor)

                    total_wounds = remaining_hits + crits
                    wound_dist[total_wounds] += prob * cover_prob

        return wound_dist

    def apply_cover_dodges_shields(self, attack_distribution, defender, cover_level, dodges, shields, ignore_dodges=False):
        """Apply cover, dodges+armor, then shields"""
        cover_level = min(cover_level + defender.cover_improvement, COVER_HEAVY)

        max_wounds = len(attack_distribution) - 1 + len(attack_distribution[0]) - 1
        wound_dist = [0.0] * (max_wounds + 1)

        # Add defender's inherent dodges and shields
        effective_dodges = 0 if ignore_dodges else (dodges + defender.dodges)
        effective_shields = shields + defender.shields

        for hits in range(len(attack_distribution)):
            for crits in range(len(attack_distribution[hits]) - hits):
                prob = attack_distribution[hits][crits]
                if prob == 0:
                    continue

                # Apply cover
                cover_dist = Unit.get_cover_cancellation_distribution(hits, cover_level)

                for hits_cancelled, cover_prob in enumerate(cover_dist):
                    if cover_prob == 0:
                        continue
                    remaining_hits = hits - hits_cancelled

                    # Apply dodges and armor
                    remaining_hits = max(0, remaining_hits - effective_dodges - defender.armor)

                    # Apply shields (cancel crits first, then hits)
                    remaining_crits = max(0, crits - effective_shields)
                    shields_for_hits = max(0, effective_shields - crits)
                    remaining_hits = max(0, remaining_hits - shields_for_hits)

                    total_wounds = remaining_hits + remaining_crits
                    wound_dist[total_wounds] += prob * cover_prob

        return wound_dist

    def get_attack_composition(self, attack_distribution):
        """
        Convert 2D attack_distribution[hits][crits] to 1D with hit/crit composition.

        Returns:
            damage_dist: [prob] for each damage value
            hits_weighted: [weighted_hits] showing expected hits for each damage value
            crits_weighted: [weighted_crits] showing expected crits for each damage value
        """
        max_damage = len(attack_distribution) - 1 + len(attack_distribution[0]) - 2
        damage_dist = [0.0] * (max_damage + 1)
        hits_weighted = [0.0] * (max_damage + 1)
        crits_weighted = [0.0] * (max_damage + 1)

        for h in range(len(attack_distribution)):
            for c in range(len(attack_distribution[h]) - h):
                prob = attack_distribution[h][c]
                damage = h + c
                damage_dist[damage] += prob
                hits_weighted[damage] += h * prob
                crits_weighted[damage] += c * prob

        return damage_dist, hits_weighted, crits_weighted

    def add_attacker(self):
        """Add current attacker selection to the list"""
        if self.attacker_unit.count() == 0:
            return

        unit_id = self.attacker_unit.currentData()
        unit_name = self.attacker_unit.currentText()
        weapon_idx = self.attacker_weapon.currentData()
        weapon_name = self.attacker_weapon.currentText()
        mini_count = self.attacker_minis_spin.value()

        self.attackers.append((unit_id, weapon_idx if weapon_idx is not None else 0, mini_count))
        self.attacker_list.addItem(f"{unit_name} ({weapon_name}) [{mini_count}]")

    def remove_attacker(self):
        """Remove selected attacker from the list"""
        current_row = self.attacker_list.currentRow()
        if current_row >= 0:
            self.attacker_list.takeItem(current_row)
            del self.attackers[current_row]

    def calculate(self):
        """Perform the attack calculation and update the chart"""
        # Validate inputs
        if not self.attackers:
            self.canvas.figure.clear()
            ax = self.canvas.figure.add_subplot(111)
            ax.set_title("Please add at least one attacker")
            self.canvas.draw()
            return

        if self.defender_unit.count() == 0:
            self.canvas.figure.clear()
            ax = self.canvas.figure.add_subplot(111)
            ax.set_title("Please select a defender")
            self.canvas.draw()
            return

        # Get attacker IDs, weapons, and mini counts
        attacker_ids = [unit_id for unit_id, _, _ in self.attackers]
        weapons = [weapon_idx for _, weapon_idx, _ in self.attackers]
        mini_counts = [mini_count for _, _, mini_count in self.attackers]

        # Get defender
        defender_id = self.defender_unit.currentData()

        # Get modifiers
        aims = self.aims_spin.value()
        precise = self.precise_spin.value()
        criticals = self.criticals_spin.value()
        hit_surges = self.hit_surges_spin.value()
        impacts = self.impacts_spin.value()
        pierce = self.pierce_spin.value()
        improvements = self.improvements_spin.value()

        dodges = self.dodges_spin.value()
        cover_text = self.cover_combo.currentText()
        cover = {'None': COVER_NONE, 'Light': COVER_LIGHT, 'Heavy': COVER_HEAVY}[cover_text]
        shields = self.shields_spin.value()
        defense_surges = self.def_surges_spin.value()

        ignore_dodges = self.ignore_dodges_check.isChecked()
        bypass_immune_pierce = self.bypass_pierce_check.isChecked()

        # Calculate using existing logic
        from calculator import SWLegion
        import io
        import contextlib

        # Temporarily capture output (we don't want console output in GUI)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            # We need to modify SWLegion.attack to return the distribution
            # For now, let's calculate it directly
            attackers = [Unit(attacker_id) for attacker_id in attacker_ids]
            defender = Unit(defender_id)

            weapons_list = weapons if weapons else [0] * len(attackers)

            # Join weapons (using mini counts from user input)
            weapon_pool = SWLegion.join_attacker_weapons(attackers, weapons_list, mini_counts, defender.size)

            # Add modifiers
            weapon_pool.aims += aims
            weapon_pool.hit_surges += hit_surges
            weapon_pool.criticals += criticals
            weapon_pool.impacts += impacts
            weapon_pool.precise += precise
            weapon_pool.pierce += pierce
            weapon_pool.improvements += improvements

            # SEQUENTIAL CALCULATION PIPELINE (following game rules)
            # Each step builds on the previous one

            # Step 1: Roll Attack Dice (apply aims, surges, Impact, Critical)
            # This is already done by get_attack_distribution
            attack_dice_2d = Unit.get_attack_distribution(weapon_pool)

            intermediates = {}
            intermediates['attack_dice'] = attack_dice_2d  # 2D distribution

            # Step 2: Apply Cover and Dodges (probabilistic cover + deterministic dodges)
            after_cover_dodges_2d = self.apply_cover_dodges_2d(attack_dice_2d, defender, cover, dodges, ignore_dodges)
            intermediates['after_cover_dodges'] = self.convert_attack_to_wounds(after_cover_dodges_2d)  # Convert to 1D for display

            # Step 3: Modify Attack Dice (apply Armor and Shields)
            after_armor_shields_1d = self.apply_armor_shields_1d(after_cover_dodges_2d, defender, shields)
            intermediates['after_armor_shields'] = after_armor_shields_1d

            # Step 4: Roll Defense Dice (without pierce for intermediate view)
            after_defense_no_pierce_1d = self.apply_defense_dice_1d(after_armor_shields_1d, defender,
                                                                     defense_surges, pierce=0,
                                                                     bypass_immune_pierce=False)
            intermediates['after_defense_dice'] = after_defense_no_pierce_1d

            # Step 5: Modify Defense Dice (apply Pierce) - FINAL OUTPUT
            wound_distribution = self.apply_defense_dice_1d(after_armor_shields_1d, defender,
                                                            defense_surges, weapon_pool.pierce,
                                                            bypass_immune_pierce)

        # Calculate expected damage
        expected_damage = sum(i * prob for i, prob in enumerate(wound_distribution))

        # Update chart
        self.update_chart(wound_distribution, expected_damage, attackers, defender, intermediates, attack_dice_2d)

    def update_chart(self, distribution, expected_damage, attackers, defender, intermediates, attack_distribution):
        """Update the matplotlib chart with new data (with dynamic layout for intermediates)"""
        import numpy as np

        # Clear the old figure
        self.canvas.figure.clear()

        # Build list of graphs to display
        graphs = []  # (title, dist, color, graph_type, extra_data)

        # Attack Composition
        if self.show_attack_comp.isChecked():
            damage_dist, hits_weighted, crits_weighted = self.get_attack_composition(attack_distribution)
            graphs.append(('Attack Composition', damage_dist, 'composition', None, (hits_weighted, crits_weighted)))
            if self.show_attack_comp_at_least.isChecked():
                graphs.append(('Attack Composition (≥X)', damage_dist, 'composition', '≥X', (hits_weighted, crits_weighted)))

        # 2D Heatmap
        if self.show_heatmap.isChecked():
            graphs.append(('2D Attack Heatmap', attack_distribution, 'heatmap', None, None))

        # Main output (always shown)
        graphs.append(('Final Output', distribution, 'steelblue', None, None))
        if self.show_main_at_least.isChecked():
            graphs.append(('Final Output (≥X)', distribution, 'coral', '≥X', None))

        # Game sequence intermediate distributions
        if self.show_after_cover_dodges.isChecked():
            graphs.append(('After Cover + Dodges', intermediates['after_cover_dodges'], 'gold', None, None))
            if self.show_cover_dodges_at_least.isChecked():
                graphs.append(('After Cover + Dodges (≥X)', intermediates['after_cover_dodges'], 'yellow', '≥X', None))

        if self.show_after_armor.isChecked():
            graphs.append(('After Armor & Shields', intermediates['after_armor_shields'], 'purple', None, None))
            if self.show_armor_at_least.isChecked():
                graphs.append(('After Armor & Shields (≥X)', intermediates['after_armor_shields'], 'plum', '≥X', None))

        if self.show_after_defense.isChecked():
            graphs.append(('After Defense Dice', intermediates['after_defense_dice'], 'orange', None, None))
            if self.show_defense_at_least.isChecked():
                graphs.append(('After Defense Dice (≥X)', intermediates['after_defense_dice'], 'peachpuff', '≥X', None))

        # Calculate grid layout (max 3 per row)
        num_graphs = len(graphs)
        cols = min(3, num_graphs)
        rows = (num_graphs + cols - 1) // cols  # Ceiling division

        # Create subplots
        axes_list = self.canvas.figure.subplots(rows, cols)
        if rows == 1 and cols == 1:
            axes_list = [axes_list]
        elif rows == 1 or cols == 1:
            axes_list = axes_list.flatten()
        else:
            axes_list = axes_list.flatten()

        # Plot each graph
        for idx, graph_data in enumerate(graphs):
            title, data, color, graph_type, extra = graph_data
            ax = axes_list[idx]

            # Handle heatmap separately
            if color == 'heatmap':
                # Create 2D grid from attack_distribution
                max_hits = len(data) - 1
                max_crits = max(len(data[h]) - h - 1 for h in range(len(data)))
                grid = np.zeros((max_crits + 1, max_hits + 1))

                for h in range(len(data)):
                    for c in range(len(data[h]) - h):
                        if c <= max_crits and h <= max_hits:
                            grid[c, h] = data[h][c] * 100  # Convert to percentage

                im = ax.imshow(grid, origin='lower', cmap='viridis', aspect='auto')
                ax.set_xlabel('Hits', fontsize=10)
                ax.set_ylabel('Crits', fontsize=10)
                ax.set_title(title, fontsize=10, fontweight='bold')
                self.canvas.figure.colorbar(im, ax=ax, label='Probability (%)')
                continue

            # Handle composition graphs
            if color == 'composition':
                hits_weighted, crits_weighted = extra

                # Filter zero probabilities (except 0 damage)
                non_zero_indices = [i for i, p in enumerate(data) if p > 0 or i == 0]
                damage_values = non_zero_indices
                probabilities = [data[i] * 100 for i in non_zero_indices]

                # Calculate stacked portions
                hits_portions = []
                crits_portions = []
                for i in non_zero_indices:
                    total_prob = probabilities[damage_values.index(i)]
                    if total_prob > 0 and i > 0:
                        hits_portions.append(hits_weighted[i] * 100 / i)  # Weighted average
                        crits_portions.append(crits_weighted[i] * 100 / i)
                    else:
                        hits_portions.append(0)
                        crits_portions.append(0)

                # For "at least" graphs, compute cumulative
                if graph_type == '≥X':
                    cumulative_probs = []
                    for i in range(len(probabilities)):
                        prob_at_least = sum(probabilities[i:])
                        cumulative_probs.append(prob_at_least)
                    probabilities = cumulative_probs

                # Plot stacked bars
                ax.bar(damage_values, hits_portions, color='steelblue', edgecolor='black', label='Hits')
                ax.bar(damage_values, crits_portions, bottom=hits_portions, color='crimson', edgecolor='black', label='Crits')

                # Add percentage labels (total height)
                total_heights = [h + c for h, c in zip(hits_portions, crits_portions)]
                for i, (dmg, height) in enumerate(zip(damage_values, total_heights)):
                    if height > 0.01:
                        ax.text(dmg, height, f'{probabilities[i]:.2f}%', ha='center', va='bottom', fontsize=7)

                ax.set_xlabel('Damage', fontsize=10)
                ax.set_ylabel('Probability (%)', fontsize=10)
                ax.set_title(title, fontsize=10, fontweight='bold')
                ax.grid(axis='y', alpha=0.3)
                ax.set_xticks(damage_values)
                ax.tick_params(labelsize=8)
                ax.legend(fontsize=8)
                continue

            # Handle regular bar graphs
            # Filter zero probabilities (except 0 damage)
            non_zero_indices = [i for i, p in enumerate(data) if p > 0 or i == 0]
            damage_values = non_zero_indices
            probabilities = [data[i] * 100 for i in non_zero_indices]

            # For "at least" graphs, compute cumulative
            if graph_type == '≥X':
                display_probs = []
                for i in range(len(probabilities)):
                    prob_at_least = sum(probabilities[i:])
                    display_probs.append(prob_at_least)
            else:
                display_probs = probabilities

            # Plot bars
            bars = ax.bar(damage_values, display_probs, color=color, edgecolor='black')

            # Add percentage labels
            for i, (bar, prob) in enumerate(zip(bars, display_probs)):
                if prob > 0.01:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{prob:.2f}%',
                           ha='center', va='bottom', fontsize=7)

            # Labels
            ax.set_xlabel('Damage', fontsize=10)
            ax.set_ylabel('Probability (%)', fontsize=10)
            ax.set_title(title, fontsize=10, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            ax.set_xticks(damage_values)
            ax.tick_params(labelsize=8)

        # Hide unused subplots
        for idx in range(num_graphs, len(axes_list)):
            axes_list[idx].set_visible(False)

        # Overall title
        attacker_names = ' + '.join([attacker.name for attacker in attackers])
        title = f"{attacker_names} vs {defender.name} | Expected Damage: {expected_damage:.2f}"
        self.canvas.figure.suptitle(title, fontsize=14, fontweight='bold')

        self.canvas.figure.tight_layout()
        self.canvas.draw()


def main():
    app = QApplication(sys.argv)
    window = LegionCalculatorGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
