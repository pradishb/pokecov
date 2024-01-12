# pokecov

Tool to check the effectiveness and coverage of your pokemon attacks

Data parsed from https://pokemondb.net/type/old and https://pokemondb.net/type

## Installation

You can install the package via pip:

```bash
pip install pokecov
```

## Usage

```
pokecov fire water grass electric
```

```
Your attacks are super effective to Fire, Water, Grass, Ice, Ground, Flying, Bug, Rock, Steel (9).
Your attacks have normal effectiveness to Normal, Electric, Fighting, Poison, Psychic, Ghost, Dark (7).
Your attacks are not very effective to Dragon (1).
Your attacks have no effect to none (0).
```

## Generation Support

```
pokecov --gen 1 normal
```

```
Your attacks are super effective to none (0).
Your attacks have normal effectiveness to Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Dragon (13).
Your attacks are not very effective to Rock (1).
Your attacks have no effect to Ghost (1).
```

## Search

Search for type combination that has 100% coverage.

```
pokecov-search --gen 3 --min-count 6 --max-count 7 --ignore dragon --must-have fire --cant-have psychic
```

```
Water, Flying, Fighting, Dark, Electric, Ground, Fire
Water, Flying, Fighting, Electric, Ground, Ghost, Fire
Flying, Fighting, Ice, Dark, Electric, Ground, Fire
Flying, Fighting, Ice, Dark, Grass, Ground, Fire
Flying, Fighting, Ice, Electric, Ground, Ghost, Fire
Flying, Fighting, Ice, Grass, Ground, Ghost, Fire
Flying, Fighting, Dark, Electric, Grass, Ground, Fire
Flying, Fighting, Dark, Grass, Rock, Ground, Fire
Flying, Fighting, Electric, Grass, Ground, Ghost, Fire
Flying, Fighting, Grass, Rock, Ground, Ghost, Fire
```

## License

This project is licensed under the terms of the MIT license.

## Contact

If you want to contact me you can reach me at pradishbijukchhe@gmail.com.
