<div align="center">
  <img src="https://media.discordapp.net/attachments/815214884920098817/938631878263574548/SBLocPatcherLogo.png" width=200 height=200/>

  # SBLocPatcher

  Localization Patcher for Windows Version of [Stormbound](https://paladinstudios.com/stormbound/)

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/dvrp0/SBLocPatcher)](https://github.com/dvrp0/SBLocPatcher/releases)
  [![GitHub license](https://img.shields.io/github/license/dvrp0/SBLocPatcher)](https://github.com/dvrp0/SBLocPatcher/blob/main/LICENSE)
</div>

## Why

First, Stormbound's translation is pretty poor from the very beginning of the game. For example, Korean name of Stoic Protectors was changed to `덱 준비 완료(All Deck Fits)` almost a year ago, and it has not been corrected yet. Even more shockingly, the descriptions of some early quests(`폭풍 탐험(Exploring the Storm)`, `압도적인 힘(Power Overwhelming)`) were changed to totally wrong ones, causing new players to have trouble completing them. There are so many mistranslations that explains card's ability in the wrong way. `#translation-suggestions` channel in the official Discord server plays a role in refining translations. However, these suggestions are rarely applied to the game recently, although they are literally ruining players' gameplay experience.

Second, Sheepyard's card descriptions are wordy and weird. As you can see below, wording and formatting is too different from Paladin's descriptions. The main reason for this problem may be that Sheepyard's main language is not English. But I think it's also because the card designs have become more complicated than necessary by [random additions of new keywords](https://discord.com/channels/293674725069029377/447484918801629195/899744998310948884) and [too many drawbacks or incidental effects](https://discord.com/channels/293674725069029377/447676050726453248/915670519376924724).

![](https://media.discordapp.net/attachments/815214884920098817/938627361233055744/unknown.png)

Loading screen lores also show the wordiness. Sheepyard's lore is more than twice as long as that of Paladin's. When this patch is applied, the average length of lore becomes almost the same as Paladin's.

## Problems
### English
 - Too long sentences
   - `...card in your hand, **then** destroy the weakest confused unit`
   - `...non-legendary unit on the side, **then** deal the same damage to the first enemy in front`
   - Splitting sentences like `...card in your hand. Destroy the weakest confused unit` feels more natural.
   - Temples' lores are reallllllllllllly long to be in loading screen.
 - Inconsistence text formatting
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927613588410105936/unknown.png)  
     Sheepyard made bold texts with `<b></b>` tags. Generally, bold texts should be made with `*` syntax. I have zero idea why Sheepyard used tags 😕
   - Keywords like confuse, vitalize, etc. should be bold.
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927609032116678737/unknown.png)  
     Flameless Lizards' and Eternal Ethereals' description should be `{no-ability}` like other vanilla cards, not blank strings.
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927607083937976350/unknown.png)  
     The amount of abilities Stoic Protectors disable is raw value, not variable like other cards. Card's variables such as how much damage it deals or how much units it summons should be expressed with `{<variable name>}` syntax.  
     ![](https://cdn.discordapp.com/attachments/815214884920098817/927607004355244053/unknown.png)  
     I looked up the registry(`MIRAGE_CONFIG_JSON`) and found Stoic's variable. So Stoic Protectors' description should be `...disable abilities of {targets}...`.
   - There should be no period at the end of sentence.
 - Inconsistence text expressions
   - Hand should be called `your hand`.
   - Unit types should be started with uppercase, like `Pirate`, `Satyr`.
   - There's two expressions referring to pass - `PREMIUM PASS` or `PASS PREMIUM`. Names should be unified.
   - There's two expressions referring to the unit or structure itself - `this` or `itself`.
   - `Before attacking` and `When attaking` have the same meaning.
 - Weird expressions
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927608727438241872/unknown.png)  
     Temple of the Heart has a new-line character at the middle of its description.
   - Earyn's description should be `card` or `cards` depend on level, not `card/s`.
   - Minion Launchers' description should be `...non-Hero unit on the side...`, not `non-legendary`. The `non` prefix should come before the unit type.
 - Vague expressions
   - Book of Chaos' description should be specified like `x cards that have 'random' word in description`, not just `x RNG cards`.
   - `...on the side` wording should be clarified like `...on a tile to the side`. Many people are confusing the meaning the word `side`.
 - Wordy expressions
   - `...split its strength equally into a unit` can be simplified to `...split this`.
 - etc.
   - I changed Temple of Focus' description to `...deconfuse all friendly units in front and command them forward`. I know this change is controversial, but I did it for the clarity of the kingdom's concept. `Give additional move` works exactly the same way as `command forward`, which is the identity of Swarm of the East. I don't understand why Sheepyard made it like that while harming consistency and clarity. I guess it's because the temples are ancient structures, but we don't know anything about ancients. I doubt that ancients were more valuable than the definite concept and consistency of the kingdom.

### Korean
 - Many mistranslations

## How It Works
Windows version of Stormbound caches localization file on `AppData/LocalLow` folder and uses this file when launches. So modifications made to this file will be applied to the game.

## Usage

 1. Download `.zip` file from [releases.](https://github.com/dvrp0/SBLocPatcher/releases)
 2. Extract it and run `SBLocPatcher.exe`.

## Miscellaneous
You can check full changelist [here](https://www.diffchecker.com/S44C37cG). You can also download patched English file in [`/localization`](https://github.com/dvrp0/SBLocPatcher/tree/main/localizations). Please note that it is encrypted.

Patched localization files are all made by me. Since I'm not an English-speaking person, there might be awkward expressions. If you find such things or have a better idea to improve descriptions, please leave [an issue.](https://github.com/dvrp0/SBLocPatcher/issues) Contributions are highly appreciated 😀

## TODO
 - [ ] GUI
 - [ ] More languages
 - [ ] Mac/Linux?
 - [x] Provide the fix list
