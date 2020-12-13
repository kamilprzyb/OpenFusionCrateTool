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
* **DropType** is a value assigned to the enemies in game. When you kill an enemy you will be awarded mob drops with corresponding type. Enemy drop types can be checked via xdt file 
* **CrateIDs** contain a list of ids for all possible crates that can be received
* **DropChance** indicates probabilities of receiving crates. Because these are shared among many drop types, we put a key to an entry in MobDropChances sheet
* **Taros** and **FM** indicate amount of taros and fm awarded
* **Boosts** indicate amount of possible nano and weapons boosts awarded. You have 33% of getting nano boost and also 33% for weapon boosts (They are randomized independently but amount is the same) 
### Mob Drop Chances
* **Type** is a key used in MobDrops sheet
* **DropChance** is a value between 0-1000 indicating your chances of getting a crate award or not (For example entering 333 means player has 33.3% of getting a crate)
* **CratesRatio** indicates crates' "weights" for the process of choosing a random crate. 
Let's say we have CrateIds `5;1;2;3;4` and CratesRatio `25;40;20;10;5` 
25 + 40 + 20  + 10 + 5 = 100, so our total pool is 100
this means we have 25/100 of getting the first crate in the list (id 5)
40/100 of getting second crate (id 1), 20/100 for id 2 and so on...





[OpenFusion]: <https://github.com/OpenFusionProject/OpenFusion>