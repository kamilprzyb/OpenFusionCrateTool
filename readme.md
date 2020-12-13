# Introduction
This is a tool for easily modifying mob drops and crates data for [OpenFusion], a reverse-engineered server for FusionFall. The tool consists of an example xlsx file used for adjusting values, and a python script which converts it to a json format used by OpenFusion server.
# Usage
Modify values input.xlsx and run `main.py`
New file `drops.json` will be created, which must be put in OpenFusion's tdata folder in order to work
**DO NOT** rename input.xlsx file or the script will not work!

## How to use input.xlsx
The file contains of 5 data sheets, containing different types of collumns. It is important that you **DON'T** modify sheets' or collumns' names, as they must correspond to names in OF's server code.

Collumns starting with a `/` character are marked as comments, and will be ignored by the script. Collumns ending with a `+` character contain number lists, separated by `;`
### Mob Drops
* **DropType** is a value assigned to the enemies in game. Enemy drop types can be checked in xdt file 
* **CrateIDs** contain a list of ids of all possible crates that can be received from this drop type
* **DropChance** indicates probability of whether you should get a crate or not. Because these are shared among many drop types, we use a foreign key to an entry in MobDropChances sheet
* **Taros**, **FM** and **Boosts** indicate amount of taros fm and boosts awarded for the kill
### Mob Drop Chances
* **Type** is a key used in MobDrops sheet
* **DropChance** is a value between 0-1000 indicating your chances of getting a crate award or not (For example entering 333 means player has 33.3% of getting a crate)
* **CratesRatio** indicates crates' "weights" for the process of choosing a random crate. 
Let's say we have CrateIds `5;1;2;3;4` and CratesRatio `25;40;20;10;5` 
25 + 40 + 20  + 10 + 5 = 100, so our total pool is 100
this means we have 25/100 of getting the first crate in the list (id 5)
40/100 of getting second crate (id 1), 20/100 for id 2 and so on...
Number of weight values here must be the same as number of crate ids!
### Crates
* **Id** means crate's ingame Id
* **ItemSets** contains a list of Ids of one or more item sets corresponding to this crate *(See items table)* If there is more than one set, it will be chosen randomly upon opening, and all sets have an equal chance
* **RarityRatio** is a foreign key to an entry in *RarityRatios* informing us what are the odds of getting items of certain rarity from the crate
### Rarity Ratios
* **Type** is a key used by *Crates* table
* **Ratio** is a list of weights for item rarities.
Let's say we have `50;40;10;0`, 50+40+10+0 = 100 so our total pool is 100.
Upon opening a crate we have 50/100 of getting rarity 1 item, 40/100 for rarity 2, 10/100 for rarity 3 and we will never get a rarity 4
`65;35` means we have 65/100 for rarity 1, 35/100 for rarity 2 and we will never get 3 or 4
`1` means we will always get rarity 1 item
Some item sets don't include items of all rarities, so the server eliminates them from the draw. It means that if we have `50;40;10;0` as a base ratio, but the crate doesn't contain a single rarity 2 item it's value is ignored as if we had `50;0;10;0`
### Items
* **ItemSet** is a key used to link items to correct crates
* **Rarity** **Type** and **Id** corresponding to ingame values





[OpenFusion]: <https://github.com/OpenFusionProject/OpenFusion>