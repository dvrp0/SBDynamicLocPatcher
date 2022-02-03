# SBLocPatcher
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/dvrp0/SBLocPatcher)](https://github.com/dvrp0/SBLocPatcher/releases) [![GitHub license](https://img.shields.io/github/license/dvrp0/SBLocPatcher)](https://github.com/dvrp0/SBLocPatcher/blob/main/LICENSE)

Localization patcher for Windows version of [Stormbound](https://paladinstudios.com/stormbound/)

## Why
First, Stormbound's translation is pretty poor from the very beginning of the game. For example, Korean name of Stoic Protectors was changed to `덱 준비 완료(All Deck Fits)` almost a year ago, and it has not been corrected yet. Even more shockingly, the descriptions of some early quests(`폭풍 탐험(Exploring the Storm)`, `압도적인 힘(Power Overwhelming)`) were changed to totally wrong ones, causing new players to have trouble completing them. There's `#translation-suggestions` channel on the official Discord server that users correct such mistranslations. However, these suggestions are rarely applied to the game recently, although they are literally ruining players' gameplay experience.

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
     <details>
       <summary><i>I have a lot more to say about ancients...</i></summary>
 
       **Unclear concept and faction inconsistency** are the biggest problems of ancients. Sheepyard said ancients are like felines, but I think they are not. These two are similar in that they are multi-themed. But they differ in how smooth the introduction of the race was and how unified and reasonable the concept is. Felines were released in two batches - **Housecats and Wildcats** - and cards in each batch share a core concept. Housecats have abilities that apply or use confusion. Wildcats have abilities that adapt based on positioning and gain speed. Also players can feel the consistency in the concept of felines, because all of them are basically the cat family.
 
       However, ancients are different. Egyptian-themed Stoic Protectors was released. Then temples that don't match Egypt as well as kingdoms were released. And suddenly spirit-like ancients were released. Also almost a year after the release of Stoic Protectors, the core identity of the race changed to 'before moving'. This is in contrast to felines which were made with two concepts from the very beginning.

       Besides, we know very little about the world of Stormbound. We only know that about 70 years ago, 'the shattering' took place and kingdoms appeared. We don't even know what the world looked like when it was whole. In this world of Stormbound, the position and meaning of ancients are so ambiguous. I've seen so many players in the community asking what the theme of ancient is, but I couldn't answer. Because I don't know either.

       The existing races of Stormbound have very distinct concepts. Constructs that labor for rodents, undeads that intelligent but cursed beings with deer-like features... Honestly, the more cards are released, the more I feel that Sheepyard is not grasping the concept of Stormbound. **Blizzard Bombs and Headless Hotheads** are good examples. These two deviate too much from the concept of frostlings and constructs. In particular, Headless Hotheads resembles knights rather than constructs, and even its ability has nothing related to constructs. I'm not condemning Sheepyard's new attempts. I just hope Sheepyard to **keep the established concept of Stormbound.**

       Back to ancients - the current state of ancients feels messy. There is no clear concept. There is no reasonable connection between Stoic Protectors and other ancients. The abilities of temples do not match each kingdom. There is still only one card that has the disable ability. Ancients **do need a main concept** like felines. At the very least, a few more ancients similar to Stoic Protectors should be released to understand that ancients are multi-themed and build apparent concept.
     </details>

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
