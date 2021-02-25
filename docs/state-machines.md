# State Machines
## Core State Machine
The Single Responsibility of the Core State Machine is to keep the event pump alive (so the OS doesn't report the app unresponsive), handle high-level events (window resize, app exit), keep the render pump alive, and forward input events (keyboard, controller) to the current state.

It will achieve these goals by containing the central game loop (`while true...`). It will capture keyboard, OS, and controller events - handling OS.QUIT and CONTROLLER.CONNECT/DISCONNECT locally, and forwarding the rest onto the current active state. It will call a `tick()` method on the active state, with time passed as an arugment, to power the logic side of things, and separately call a `render()` method on the active state, passing in the current displayable `Surface`. [^1]

[^1]: Do we need different loops/timings on `tick` and `render`, so we're not constraining logic updates to the framerate?

There are two states at this level - the menu tree and gameplay.

## Menu Tree
The Menu Tree is mostly what currently exists outside of game modes in Kroz. It will need an extra layer in some menus to account for new behaviors - players can switch which set of dungeons (classic Kroz game) they will play through, rather than exiting and starting another app. Additionally, once they finish a level, they will unlock single-level play from the Menu Tree, so they can replay that level with the best starting stats (so finishing different runs with a focus on gem, whip, teleport, score, or key management will produce many reply options for each level).

The Shareware and Marketing screens will also need some adjustment - it's a fun thought to think we can leave them in for legacy's sake, but they contain financial promises that the referenced parties may not want to fulfill. We should definitely keep the history sections for each game.

Finally, this project has its own dependencies, which the original Kroz could assume with no mention (fonts and pygame itself, for instance). We need a page that clearly lists the credit required for these dependencies. Also, Kroz source is GPL - meaning, this source must also be available, since this source is direclty derived from that (though little to no original code will remain, the level layouts in particular are part of code, not content or data, in the original - so to support the original content is to adopt GPL for this project as well).

### Page Sets
The Sets determine the basic flow of related menus. They carry navigation context and respond to Page events. These events are:

* HOME - returns to the parent
  * Returning to the parent, in any of these commands, abandons the context
* PREVIOUS - returns to the previous page (the parent if at the beginning of the set)
* NEXT - advances to the next page in the set (or triggers the Output if there are no more pages)
* CHOICE (Input Command value) - supplies data to the Set context and advances to the next page in the set (or triggers the Output if there are no more pages)
* CLEAR - removes the Page's data from the Set context
* PREVIOUS + CLEAR - removes the Page's data from the Set context and navigates backward in the Page order (which is the parent if there are no previous pages)
* SUB (Page Set name) - stores the current context (data and page) and passes control to another Page Set. When that Page Set completes, it might contribute to the parent Set's data context
* SWITCH (Page Set name) - abandons the current Page Set and switches control to the given Page Set instead.
  * This may allow replacement of the base (unparented) Page Set, effectively switching menus but staying in menu mode

_A Page Set needs:_
* Optional Parent set
* Input data and routine (transform logic object to page-command mapping)
  * Default to "empty"
  * Needs to interact with logic layer - code-driven
* Data context
  * Individual Pages or Sets may require parts of this as their Input data
* Page context (which page is active)
* Pages (with implied ordering)
  * Each Prompt Page is associated with a mapping. Non-Prompt Pages are not.
* Output routine (transform page-command mapping to logic object, put the logic object somewhere)
  * Needs to interact with logic layer - code-driven

### Pages
A Page is a displayable unit. They render content - potentially animated on a frame-by-frame basis - and respond to input events. However, the meaning of those events is handled by their containing Set, so other than passing information on to their Set, they do very little.

_All Pages need:_
* Their containing Set
  * Maybe used to capture context
  * Definitely used to report Page commands

#### Static Page
Most menus in the Menu Tree are static - they render a set of text (using the current font and theme) according to a well-defined prescription, then wait for input before proceeding. They should be allowed to specify a `header` which follows a known pattern. However, the body may include different indentation, special characters, and animation (blinking) so it's non-trival to make it purely data-driven. Additionally, the prompt text (`press any key to continue`) changes colors at a moderate-to-high speed.

_Static Pages need:_
* A Mapping of Input Command to Page Command
> Default:
> * MENU -> HOME
> * BACK -> PREVIOUS
> * MOVE_WEST -> PREVIOUS
> * Other Movement -> Ignore
> * All Others -> NEXT 

Static Pages capture and issue the following commands:
* PREVIOUS
* HOME
* NEXT

#### Prompt Page
A Prompt Page is part of a sequence of Pages. Each explains one choice, and presents commands for the user to make that choice. The aggregate of these choices is a data object - generally, App or Game setup (choose theme, choose speed, choose difficulty). In addition to a `header` and some static (but possibly animated) text explaining the options, Prompt menus need to be able to list the acceptable commands. Outside of navigation (MENU, BACK), there are 8 commands, which is a pretty wide array of options. The ATTACK command should be used to power through default values. There is a non-command result - CLEAR - which will empty a previous response from the field which the current prompt fills. The BACK command may issue both BACK and CLEAR, or CLEAR might be set to a spearate command.

_Prompt pages need:_
* A list of supported Commands to capture
  * Excludes MENU, BACK
* Configuration on:
  * Whether to apply PREVIOUS or PREVIOUS + CLEAR
  * Optional Input Command map to CLEAR
  * The combination of these two means it's possible to make a required (unclearable) value

Prompt Pages capture and issue the following commands:
* HOME
* PREVIOUS
* CLEAR
* PREVIOUS + CLEAR
* CHOICE (Input Command)

#### Menu Page
A Menu Page presents the user with a selection of new Page Sets to navigate. Each selection might be a SUB (returning back to this Page when complete) or a SWITCH (signaling to the base menu state machine that a new Page Set should take control as the root). Like with a Prompt Page, there is a mapping of input commands to page commands, but in this case the change is to underlying state, rather than the Page Set data context.

_Menu Pages need:_
* A mapping of Input Commands to Page Sets
  * Includes whether each Input Command is a SUB or SWITCH
  * Excludes MENU and BACK

Menu Pages capture and issue the following commands:
* HOME
* PREVIOUS
* SUB (Page Set name)
* SWITCH (Page Set name)

## Gameplay
Gameplay is the most exciting and highest-usage state. It's also the most complex and the most demanding. Part of the goal of the complexity of the gameplay state machine is to recreate some of the quirks of working on a single-threaded 12 MHz system. Code that was written to count to 100 to block execution, and did not have to report liveliness to an OS while it did so, produces a specific feel that is difficult to duplicate. Processing a batch of monster and player movements was intertwined with visual updates.

### Play
The Play state handles most gameplay, and is the window into the game logic layer. While in the Play state, the game is counting timers down, responding to player input, calculating and implementing monster movement, and handling map automata (such as lava flow and forest growth). Each frame of the Play state, we check the Move Queue to see if anyone gets to move. We check the player input queue to see if there is any input which can be translated to Gameplay commands - if so, we consume that and add it to the Move Queue.

_The Play State has:_
* A Command Queue
  * Commands issued while in Play state wait in this queue to be turned into Player Moves (or handled more immediately, in the case of system commands like Pause, Reload, or Quit)
* A Move Queue
  * May be nested queues - one for player, one for monsters, one for environment? - with a single 'next' output
* A SkipTime Timer
  * Counts down while the queues are empty
  * Resets on player providing input into the Move Queue
  * On Reset, advances Monster Sets
* A Monster Set per monster type

_A Monster Set has:_
* A list of active monsters
* An internal countdown
  * When the countdown reaches 0, every active monster gets added to the Move Queue

#### Idle
The Idle state handles the case where there are no Moves in the Move Queues. If at any point a Move gets added, Idle transitions; the destination state depends on which Move Queue is populated. It counts down a timer (SkipTime) - at zero, the game timers are incremented (Monster Sets; Player Effects like Invisibility; World Effects like Speed, Slow, and Freeze). There is a high probability that this populates the Move Queues - if not, the timer simply resets and counts down again.

#### Player Move
The Player Move state is very short-lived. It takes the Move off the Move Queue and turns it into one of the following:
* A No-op - for instance, the player asked to Whip but had no Whips
* A playfield state change - for instance, the player took a step, or had a Whip in the previous case
* A mode change - for instance, the player pressed pause, or entered a long-running animation (teleport, tunnel), or died

#### Monster Moves
Each timer tick is an opportunity for a type of monster (Slow, Medium, or Fast) to queue up their moves. If the moster countdown reaches 0 for a monster type, every monster of that type queues up its moves in the Move Queue and the timer is reset. Each Monster Move applies to one monster, and has several possible results:
* A No-op - for instance, the monster is up against terrain they cannot cross
* A playfield state change - for instance, the monster took a step, or took a step onto something it's allowed to consume, like a whip or gem
* A destructive state change - for instance, the monster took a step onto the player or a mutually-destructive space
  * This may cause player state changes - player death, for instance - which in turn will cause game state changes

Each Monster Move also has a random chance (depending on the monster which is moving) of consuming a Command Queue command, adding a new Player Move to the Move Queue. Naturally, this means the Idle state will transition to the Player Move state once it regains control.

### Animate
The Animate state pauses the main gameplay in order to focuse on an important or dramatic event. This is usually a combination of visual changes (colors flashing or cycling, symbols being rendered or removed), sounds, and logic changes. Visual effects should continue to advance (such as monsters swapping 'poses' and stairs blinking) in addition to the animation being played, but no game logic should process.

### Prompt / Pause
The Prompt state pauses the main gameplay in order to present an interaction with the player directly. This is either a 'Press any key' prompt explaining some new thing the player interacted with, or the Save and Restore flows that alter the state of the game.