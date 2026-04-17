# D&D 5e CR Calculator

## Summary
This is a CR calculator for D&D 5e that doesn't need to use an expected CR.

## Setup
### Step 1

```
sudo apt install python3
```

### Step 2

```
sudo apt install python3-tk
```

### Step 3

```
git clone https://github.com/connor610/dnd-5e-monster-cr-calculator.git
```

### Step 4

```
cd dnd-5e-monster-cr-calculator
```

### Step 5

```
cd source
```

### Step 6

```
python3 main.py
```
or
```
uv run main.py
```

## How to Use
When the window opens, all you have to do is put the values in the right entry boxes, select the right value in the comboboxes, select the right checkbuttons, then click the submit button and see the effective stats, possible scores, and the final CR.

## Reasons For Creating This Project
1. My biggest problem with CR calculators that are publicly available are that they require an expected CR, which can alter the final CR. So I decided to make a CR calculator that calculates the expected CR at the start of the calculation based on the stats given, then updates the CR by recalculating based on the new stats at the end of each step, since the rules on creating a D&D monster requires an expected CR at a few steps.
2. My second reason for making this is because this is my first personal project for Boot.Dev and since I was already reading the rules on monster creation for D&D, it was the perfect opportunity to make this project.

## Reasons For Not Including Some Monster Features
The reasons for not including some monster features are as follows:
1. Not having any effect on the CR:
   * Amorphous
   * Amphibious
   * Antimagic Susceptibility
   * Blind Senses
   * Chameleon Skin
   * Change Shape
   * Charm
   * Damage Absorption
   * Devil Sight
   * Echolocation
   * Etherealness
   * False Appearance
   * Fey Ancestry
   * Flyby
   * Grappler
   * Hold Breath
   * Illumination
   * Illusory Appearance
   * Immutable Form
   * Incorporeal Movement
   * Inscrutable
   * Invisibility
   * Keen Senses
   * Labyrinthine Recall
   * Leadership
   * Life Drain
   * Light Sensitivity
   * Magic Weapons
   * Mimicry
   * Otherworldly Perception
   * Reactive
   * Read Thoughts
   * Reckless
   * Redirect Attack
   * Reel
   * Rejuvenation
   * Shapechanger
   * Siege Monster
   * Slippery
   * Spider Climb
   * Standing Leap
   * Steadfast
   * Sunlight Sensitivity
   * Sure-Footed
   * Teleport
   * Terrain Camouflage
   * Tunneler
   * Turn Immunity
   * Turn Resistance
   * Two Heads
   * Web Sense
   * Web Walker
2. Assumes that the user has already added the damage to the damage entry boxes:
   * Angelic Weapons
   * Breath Weapon
   * Brute
   * Charge
   * Death Burst
   * Dive
   * Elemental Body/Heated Body
   * Enlarge
   * Martial Advantage
   * Pounce
   * Rampage
   * Surprise Attack
   * Swallow
   * Wounded Fury
3. Extremely difficult to calculate due to the wide range of options and possible combos:
   * Innate Spellcasting
   * Spellcasting

Hope you find this calculator as useful as it was for me.
