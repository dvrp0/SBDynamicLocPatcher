# SBLocPatcher
![GitHub release (latest by date)](https://img.shields.io/github/v/release/dvrp0/SBLocPatcher) ![GitHub license](https://img.shields.io/github/license/dvrp0/SBLocPatcher)

Localization patcher for Windows version of [Stormbound](https://paladinstudios.com/stormbound/)

## Why
First, Stormbound's translation is pretty poor from the very beginning of the game. For example, Korean name of Stoic Protectors was changed to `덱 준비 완료(All Deck Fits)` almost a year ago, and it has not been corrected yet. Even more shockingly, the descriptions of some early quests(`폭풍 탐험(Exploring the Storm)`, `압도적인 힘(Power Overwhelming)`) were changed to totally wrong ones, causing new players to have trouble completing them. There's `#translation-suggestions` channel on the official Discord server that users correct such mistranslations. However, these suggestions are rarely applied to the game recently, although they are literally ruining players' gameplay experience.

![](https://media.discordapp.net/attachments/815214884920098817/928644018294894623/unknown.png)

Second, Sheepyard's card description is too wordy. Common cards made by Sheepyard have longer descriptions than existing legendaries. Of course, another reason for this wordiness is that Sheepyard's card designs are too different from the direction this game pursues. [Random additions of new keywords](https://discord.com/channels/293674725069029377/447484918801629195/899744998310948884) and [too many drawbacks or incidental effects](https://discord.com/channels/293674725069029377/447676050726453248/915670519376924724) are good examples.

As you can see above, Sheepyard's text is longer than Paladin's. Even considering that they are simple averages, Sheepyard's lore is more than twice as long as Paladin's. When the patch is applied, the average length of lore becomes almost the same as Paladin's. And the average length of the card description is reduced by three characters. This difference looks very small, but I couldn't reduce it more because the design of the cards was complicated. I also focused not only on shortening the descriptions but on fixing the problems below.

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
     The amount of abilities Stoic Protectors disable is raw-value, not variable like other cards. Card's variables such as how much damage it deals or how much units it summons should be expressed with `{<variable name>}` syntax.  
     ![](https://cdn.discordapp.com/attachments/815214884920098817/927607004355244053/unknown.png)  
     I looked up the registry(`MIRAGE_CONFIG_JSON`) and found Stoic's variable. So Stoic Protectors' description should be `...disable abilities of {targets}...`.
   - There should be no period at the end of sentence.
 - Inconsistence text expressions
   - Hand should be called `your hand`.
   - Unit types should be started with uppercase, like `Pirate`, `Satyr`.
   - There's two expressions referring to pass - `PREMIUM PASS` or `PASS PREMIUM`. Names should be unified.
   - There's two expressions reffering to the unit or structure itself - `this` or `itself`.
   - `Before attacking` and `When attaking` have the same meaning.
 - Weird expressions
   - ![](https://cdn.discordapp.com/attachments/815214884920098817/927608727438241872/unknown.png)  
     Temple of the Heart has a new-line character at the middle of its description.
   - Earyn's description should be `card` or `cards` depend on level, not `card/s`.
   - Minion Launchers' description should be `...non-Hero unit on the side...`, not `non-legendary`. The `non` prefix should come before the unit type.
 - Vague expressions
   - Book of Chaos description should be specified like `x cards that have 'random' word in description`, not just `x RNG cards`.
   - `...on the side` wording should be clarified like `...on a tile to the side`. Many people are confusing the meaning the word `side`.
 - Wordy expressions
   - `...split its strength equally into a unit` can be simplified to `...split this`.
 - etc.
   - I changed Temple of Focus' description to `...deconfuse all friendly units in front and command them forward`. I know this change is controversial, but I did it for the clarity of the kingdom's concept. `Give additional move` works exactly the same way as `command forward`, which is the identity of Swarm of the East. I don't understand why Sheepyard made it like that while harming consistency and clarity. I guess it's because the temples are ancient structures, but we don't know anything about ancients. I doubt that ancients were more valuable than the definite concept and consistency of the kingdom.  
     <details>
       <summary><i>I have a lot more to say about ancients...</i></summary>
 
       **Unclear concept and faction inconsistency** are the biggest problems of ancients. Sheepyard said ancients are like felines, but they are completely different. Felines have been released in two batches - **Housecats and Wildcats** - and cards in each batch share core concepts. Housecats have abilities that apply or use confusion. Wildcats have abilities that adapt based on positioning and gain speed. Above all, players can feel the consistency in the concept of felines, because they are all the cat family.
 
       However, ancients are being released in a completely different way. Egyptian-themed Stoic Protectors released. Then temples that don't match Egypt as well as kingdoms released. And suddenly spirit-like ancients released. I've seen so many players in the community asking what the theme of ancient is, but I couldn't answer. Because **I don't know either.**

       We know very little about the world of Stormbound. We only know that about 70 years ago, 'the shattering' took place and kingdoms appeared. We don't even know what the world looked like when it was whole. In this world of Stormbound, the position and meaning of ancients are so ambiguous. Also there is no main concept of the race so we can't figure out what Sheepyard wants to deliver to us at all.

       The existing races of Stormbound have very distinct concepts. Constructs that labor for rodents, undeads that intelligent but cursed deer-like humanoids... Honestly, the more cards are released, the more I feel that Sheepyard is not grasping the concept of Stormbound. **Blizzard Bombs and Headless Hotheads** are good examples. These two deviate too much from the concept of frostlings and constructs. In particular, Headless Hotheads resembles knights rather than constructs, and even its ability has nothing related to constructs. I'm not condemning Sheepyard's new attempts. I just hope Sheepyard to **keep the established concept of Stormbound.**

       Back to ancients - ancients do not have a clear concept. The abilities of temples do not match each kingdom. There is still only one card that has the disable ability. The current state of ancients feels just [messy](https://discord.com/channels/293674725069029377/447484918801629195/813443743206080523). We **DO need a main concept** for ancients... like felines.
     </details>

### Korean
 - Many mistranslations

## Miscellaneous
You can check full changelist [here](https://www.diffchecker.com/S44C37cG). You can also download patched English file in [`/localization`](https://github.com/dvrp0/SBLocPatcher/tree/main/localizations). Please note that it is encrypted.

Patched localization files are all made by me. Since I'm not an English-speaking person, there might be awkward expressions. If you find such things or have a better idea to improve descriptions, please leave [an issue.](https://github.com/dvrp0/SBLocPatcher/issues) Contributions are highly appreciated 😀

## TODO
 - [ ] GUI
 - [ ] More languages
 - [ ] Mac/Linux?
 - [x] Provide the fix list
