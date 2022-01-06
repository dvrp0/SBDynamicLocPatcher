# SBLocPatcher
![GitHub release (latest by date)](https://img.shields.io/github/v/release/dvrp0/SBLocPatcher) ![GitHub license](https://img.shields.io/github/license/dvrp0/SBLocPatcher)

Localization Patcher for Window version of [Stormbound](https://paladinstudios.com/stormbound/)

## Why
First, Stormbound's translation is pretty poor. For example, Korean description of Counselor Ahmi still says **bordering**, not surrounding. On the official Discord server, there's `#translation-suggestions` channel that users correct such mistranslations. However, these suggestions are rarely applied to the game, although they are literally ruining players' gameplay experience.

![](https://media.discordapp.net/attachments/815214884920098817/928644018294894623/unknown.png)

Second, Sheepyard's card description is too wordy. Common cards made by Sheepyard have longer descriptions than legendaries. Of course, another reason for this wordiness is that Sheepyard's card designs are too different from the direction this game pursues. [Random additions of new keywords](https://discord.com/channels/293674725069029377/447484918801629195/899744998310948884) and [too many drawbacks or incidental effects](https://discord.com/channels/293674725069029377/447676050726453248/915670519376924724) are good examples.

As you can see above, Sheepyard's text is longer than Paladin's. Even considering that they are simple averages, Sheepyard's lore is more than twice as long as Paladin's. When the patch is applied, the average length of lore becomes almost the same as Paladin's. And the average length of the card description is reduced by three characters. This difference looks very small, but I couldn't reduce more because the design of the cards was complicated. I also focused not only on shortening the descriptions, but on fixing the problems below.

## How It Works
Window version of Stormbound caches localization file on `AppData/LocalLow` folder and uses this file when launches. So modifications made to this file will be applied to the game.

## Problems
### English
 - Too long sentences
   - `...card in your hand, **then** destroy the weakest confused unit`
   - `...non-legendary unit on the side, **then** deal the same damage to the first enemy in front`
   - Splitting sentences like `...card in your hand. Destroy the weakest confused unit` feels more natural.
   - Temples' lores are reallllllllllllly long to be in loading screen.
 - Inconsistence text formatting
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927613588410105936/unknown.png)  
     Sheepyard made bold texts with `<b></b>` tags. Generally, bold texts are made with `*` syntax. I have zero idea why Sheepyard used tags 😕
   - Keywords like confuse, vitalize, etc. should be bold.
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927609032116678737/unknown.png)  
     Flameless Lizards' and Eternal Ethereals' description should be `{no-ability}` like other vanilla cards, not blank strings.
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927607083937976350/unknown.png)  
     Stoic Protectors' disable amount is raw-value, not variable like other cards. Card's variable like strength it gives, damage it deals should be expressed with `{<variable name>}` syntax.  
     ![](https://cdn.discordapp.com/attachments/815214884920098817/927607004355244053/unknown.png)  
     I looked up the registry(`MIRAGE_CONFIG_JSON`) and found Stoic's variable. So Stoic Protectors' description should be `...disable abilities of {targets}...`.
 - Inconsistence periods at the end of sentence
   - There should be no period at the end of sentence.
 - Inconsistence text expressions
   - Hand should be called `your hand`.
   - Unit types should be started with uppercase, like `Pirate`, `Satyr`.
   - There's two expressions that call pass - `PREMIUM PASS` or `PASS PREMIUM`. Names should be unified.
 - Weird expressions
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927608727438241872/unknown.png)  
     Temple of the Heart has a new-line character at the middle of its description.
   - Earyn's description should be `card` or `cards` depend on level, not `card/s`.
   - Book of Chaos description should be specified like `x cards that have 'random' word in description`, not just `x RNG cards`.
   - Minion Launchers' description should be `...non-Hero unit on the side...`, not `non-legendary`. The `non` prefix should come before the unit type.
 - Vague expressions
   - `...on the side` wording should be clarified like `...on a tile to the side`. Many people are confusing the meaning the word `side`.
 - Wordy expressions
   - `...split its strength equally into a unit` can be simplified to `...split this`.

### Korean
 - Many mistranslations

## Miscellaneous
You can check all changelist [here](https://www.diffchecker.com/e0aclYKM). You can also download patched English file in [`/localization`](https://github.com/dvrp0/SBLocPatcher/tree/main/localizations). Please note that it is encrypted.

Patched localization files are all made by me. Since I'm not an English-speaking person, there might be awkward expressions. If you find such things or have a better idea to improve descriptions, please leave [an issue.](https://github.com/dvrp0/SBLocPatcher/issues) Contributions are highly appreciated 😀

## TODO
 - [ ] GUI
 - [ ] More languages
 - [ ] Mac/Linux?
 - [x] Provide the fix list
