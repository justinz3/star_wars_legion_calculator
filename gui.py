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
    def __init__(self, parent=None, width=8, height=6, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes_left, self.axes_right = fig.subplots(1, 2)
        # Maintain backward compatibility: axes points to left subplot
        self.axes = self.axes_left
        fig.tight_layout()
        super(MplCanvas, self).__init__(fig)


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

        # Bottom: Chart
        self.canvas = MplCanvas(self, width=10, height=6, dpi=100)
        main_layout.addWidget(self.canvas)

        # Initialize with empty chart
        self.canvas.axes.set_xlabel('Damage')
        self.canvas.axes.set_ylabel('Probability (%)')
        self.canvas.axes.set_title('Select units and click Calculate')
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
        """Create modifiers input panel"""
        group = QGroupBox("Modifiers")
        layout = QGridLayout()

        row = 0

        # Attack modifiers
        layout.addWidget(QLabel("<b>Attack Modifiers</b>"), row, 0, 1, 2)
        row += 1

        self.aims_spin = QSpinBox()
        self.aims_spin.setRange(0, 10)
        layout.addWidget(QLabel("Aims:"), row, 0)
        layout.addWidget(self.aims_spin, row, 1)
        row += 1

        self.precise_spin = QSpinBox()
        self.precise_spin.setRange(0, 10)
        layout.addWidget(QLabel("Precise:"), row, 0)
        layout.addWidget(self.precise_spin, row, 1)
        row += 1

        self.criticals_spin = QSpinBox()
        self.criticals_spin.setRange(0, 10)
        layout.addWidget(QLabel("Criticals:"), row, 0)
        layout.addWidget(self.criticals_spin, row, 1)
        row += 1

        self.hit_surges_spin = QSpinBox()
        self.hit_surges_spin.setRange(0, 10)
        layout.addWidget(QLabel("Hit Surges:"), row, 0)
        layout.addWidget(self.hit_surges_spin, row, 1)
        row += 1

        self.impacts_spin = QSpinBox()
        self.impacts_spin.setRange(0, 10)
        layout.addWidget(QLabel("Impacts:"), row, 0)
        layout.addWidget(self.impacts_spin, row, 1)
        row += 1

        self.pierce_spin = QSpinBox()
        self.pierce_spin.setRange(-5, 10)
        layout.addWidget(QLabel("Pierce:"), row, 0)
        layout.addWidget(self.pierce_spin, row, 1)
        row += 1

        self.improvements_spin = QSpinBox()
        self.improvements_spin.setRange(0, 10)
        layout.addWidget(QLabel("Improvements:"), row, 0)
        layout.addWidget(self.improvements_spin, row, 1)
        row += 1

        # Defense modifiers
        layout.addWidget(QLabel("<b>Defense Modifiers</b>"), row, 0, 1, 2)
        row += 1

        self.dodges_spin = QSpinBox()
        self.dodges_spin.setRange(0, 10)
        layout.addWidget(QLabel("Dodges:"), row, 0)
        layout.addWidget(self.dodges_spin, row, 1)
        row += 1

        self.cover_combo = QComboBox()
        self.cover_combo.addItems(['None', 'Light', 'Heavy'])
        layout.addWidget(QLabel("Cover:"), row, 0)
        layout.addWidget(self.cover_combo, row, 1)
        row += 1

        self.shields_spin = QSpinBox()
        self.shields_spin.setRange(0, 10)
        layout.addWidget(QLabel("Shields:"), row, 0)
        layout.addWidget(self.shields_spin, row, 1)
        row += 1

        self.def_surges_spin = QSpinBox()
        self.def_surges_spin.setRange(0, 10)
        layout.addWidget(QLabel("Defense Surges:"), row, 0)
        layout.addWidget(self.def_surges_spin, row, 1)
        row += 1

        # Special flags
        layout.addWidget(QLabel("<b>Special Mechanics</b>"), row, 0, 1, 2)
        row += 1

        self.ignore_dodges_check = QCheckBox("Ignore Dodges (High Velocity)")
        layout.addWidget(self.ignore_dodges_check, row, 0, 1, 2)
        row += 1

        self.bypass_pierce_check = QCheckBox("Bypass Immune Pierce (Makashi)")
        layout.addWidget(self.bypass_pierce_check, row, 0, 1, 2)
        row += 1

        # Calculate button
        calc_btn = QPushButton("CALCULATE")
        calc_btn.setStyleSheet("QPushButton { font-size: 16px; font-weight: bold; padding: 10px; }")
        calc_btn.clicked.connect(self.calculate)
        layout.addWidget(calc_btn, row, 0, 1, 2)

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
            self.canvas.axes.clear()
            self.canvas.axes.set_title("Please add at least one attacker")
            self.canvas.draw()
            return

        if self.defender_unit.count() == 0:
            self.canvas.axes.clear()
            self.canvas.axes.set_title("Please select a defender")
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

            # Get attack distribution
            pooled_attack_distribution = Unit.get_attack_distribution(weapon_pool)

            # Apply defense
            wound_distribution = defender.defend(pooled_attack_distribution, dodges=dodges, cover=cover,
                                                shields=shields, defense_surges=defense_surges,
                                                pierce=weapon_pool.pierce, ignore_dodges=ignore_dodges,
                                                bypass_immune_pierce=bypass_immune_pierce)

        # Calculate expected damage
        expected_damage = sum(i * prob for i, prob in enumerate(wound_distribution))

        # Update chart
        self.update_chart(wound_distribution, expected_damage, attackers, defender)

    def update_chart(self, distribution, expected_damage, attackers, defender):
        """Update the matplotlib chart with new data"""
        self.canvas.axes_left.clear()
        self.canvas.axes_right.clear()

        # Create damage values and probabilities
        damage_values = list(range(len(distribution)))
        probabilities = [prob * 100 for prob in distribution]  # Convert to percentages

        # Calculate reverse cumulative probabilities (at least X damage)
        cumulative_probs = []
        for i in range(len(probabilities)):
            # Probability of dealing i or more damage
            prob_at_least = sum(probabilities[i:])
            cumulative_probs.append(prob_at_least)

        # LEFT SUBPLOT: Regular probability distribution
        bars_left = self.canvas.axes_left.bar(damage_values, probabilities, color='steelblue', edgecolor='black')

        # Add percentage labels to left subplot
        for i, (bar, prob) in enumerate(zip(bars_left, probabilities)):
            if prob > 0.01:  # Only show label if probability > 0.01%
                height = bar.get_height()
                self.canvas.axes_left.text(bar.get_x() + bar.get_width()/2., height,
                                          f'{prob:.2f}%',
                                          ha='center', va='bottom', fontsize=8)

        self.canvas.axes_left.set_xlabel('Damage', fontsize=12)
        self.canvas.axes_left.set_ylabel('Probability (%)', fontsize=12)
        self.canvas.axes_left.set_title('Probability Distribution', fontsize=12, fontweight='bold')
        self.canvas.axes_left.grid(axis='y', alpha=0.3)
        self.canvas.axes_left.set_xticks(damage_values)

        # RIGHT SUBPLOT: Cumulative probability distribution
        bars_right = self.canvas.axes_right.bar(damage_values, cumulative_probs, color='coral', edgecolor='black')

        # Add percentage labels to right subplot
        for i, (bar, cum_prob) in enumerate(zip(bars_right, cumulative_probs)):
            if cum_prob > 0.01:  # Only show label if cumulative probability > 0.01%
                height = bar.get_height()
                self.canvas.axes_right.text(bar.get_x() + bar.get_width()/2., height,
                                           f'{cum_prob:.2f}%',
                                           ha='center', va='bottom', fontsize=8)

        self.canvas.axes_right.set_xlabel('Damage', fontsize=12)
        self.canvas.axes_right.set_ylabel('Probability (%)', fontsize=12)
        self.canvas.axes_right.set_title('At Least X Damage', fontsize=12, fontweight='bold')
        self.canvas.axes_right.grid(axis='y', alpha=0.3)
        self.canvas.axes_right.set_xticks(damage_values)

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
