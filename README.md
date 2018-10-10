#Simple Fate/Grand Order summon simulator

## Introduction
This is a simple Fate/Grand Order summon simulator, and a interface to [pandolia/qqbot](https://github.com/pandolia/qqbot) . The summon will only return golden servants and star-5 crafts. The algorithm is helpfully referred by the project [konatasick/test_simulator](https://github.com/konatasick/test_simulator) and the database is obtained from [Mooncell](https://fgo.wiki)

## Installation
One can simply copy all file in ~/.qqbot-tmp/plugins folder and use it by qqbot.
Or, one can use the python file: fgosummon_simu_module.py. The class **pool** served many method to simulate a ordinate fgo card pool.

## Database structure:
- Every row has the servants database as below:
  |ID|Rarity|Name| Class ID | Limit |
  |--|--|--|--|--|
  Where the Rarity follow the mapping:
  $$i \rightarrow \star \ \text{i} $$
  And the Class ID follow the mapping:
  |1|2|3|4|5|6|7|8|9|
  |-|-|-|-|-|-|-|-|-|
  |Saber|Archer|Lancer|Rider|Caster|Assasin|Berserker|Shield|Ruler|

  |10|11|12|13|14|15|16|17|18|
  |-|-|-|-|-|-|-|-|-|
  |Avenger|Mooncancer|AlterEgo|Foreigner|Beast|
  And the Limit follow the mapping:
  |Number|Limit Type|
  |-|-|
  |0|Unsummonable|
  |1|no-limit|
  |2|Story Only|
  |3|Event Only|
  |4|Friend Only|

- Craft index has the meaning as:
  Where in Mooncell, it is named as "type_marker" in csv file.  
  |Number|Limit Type|
  |-|-|
  |2|From DaVince shop|
  |4|kizuna|
  |9|St. Valentine|
  |16|Event Memory|
  |32|Craft exp|
  |64 and 65|Any pool (including friend)|
  |128 and 129|free to Get in Event|
  |256 and 257|Get from pool|
  |512|Story pool only|
  Where \(2^n+1\) type is effective in event.
  In my file, it is 1 for any pool and 2 for pick up one.
