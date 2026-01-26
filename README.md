Terreria ML Write Up

The goal of this project is to produce an AI that is capable of beating the first boss in Terraria. The algorithm will be written with a reward system that enforces certain steps in a Terraria playthrough via a reward system. This will produce an AI that is capable of surviving, moving, obtaining upgrades, and obtaining tools capable of defeating the Eye of Cthulhu.

Progress Tracking:
 Screen Capture and Input [X]
Simple movement from AI. []
Breaking blocks. []
Reward System. []
Ground Detection. []
Reinforcement of reward system. []
Accelerating game run time and AI training. []
Observation and continued updates. []
Error fixing. []
Niche Action Pathing (Spawners, potions, reforging?) []
 Arena Assembly. []
Training against the eye. []
Increased Testing. []
Full Run Attempts []

The bot used to complete these attempts will be named KidBot#, each iteration of him shall be for a new form of testing. Consider the following to be a graveyard with the latest bot being the newest living of them.

KidBot1-2: Miscreated bots.
KidBot3: Journey Mode Bot for simple movement from Python and screen capture testing.


The following are the most simple and needed items for an AI to be able to beat the Eye of Cthulhu. This should be seen as a no more situation. These are the minimal items a player has to have to beat this boss, and what I would consider the least needed for a successful defeat in normal mode.

4-6 Heart Crystals
Armor preferable, full tier 2 metal or cactus should be sufficient.
Hermes Boots/Variant Boots (aglet, anklet)
Cloud in a bottle/Variant bottle items
A (good) chest weapon.
Bonuses (Shackle, Band of regen, fledgling wings)


Reforging?
Many accessories are useful for things such as mobility and survivability. We can reward the AI on equipping these tools but we would want to have a tier system so that the AI prefers better accessories. Hermes boots are a must for easier eyekills. If the AI manages to kill the goblin army and find the goblin tinkerer, the ability to reforge and mix accessories with the tinkerer’s workshop would be possible. This is a very broad, possibly very difficult system for an AI to consistently train on given how niche the conditions are for something like this. It has to break shadow orbs/crimson hearts to even get the conditions for a goblin army to occur. It is very likely the AI would get a weapon capable of defeating the Eye of Cthulhu from just breaking the orbs. Therefore, this will be a process we don’t focus on right now.


Point Management
Now making this reinforcement based system succeed requires on point rewards and even deductions. I will now give a brief summary of what is planned for the AI to be rewarded on. 

Rewards
Movement gives 0.01p per second.
Jumping gives 0.01p.
Breaking dirt gives 0.02
Breaking stone gives 0.2p (reward deep caving more than random dirt breaking)
Breaking T1 ore (tin and copper) gives 0.2p)
Breaking T2 ore (silver and tungsten) gives 0.4p
Breaking T3 ore (gold and platinum) gives 1p. These ores are immensely rewarding because they allow us to get the best armor)
Break life crystal gives 5p.
Opening a chest gives 10p. It’s worth noting the AI will need its own chest storage and we can’t give points on opening a chest over and over again. We will need a way to only give these rewards once. One idea is to only reward chests that contain certain items.
Equipping accessories gives points. The points depend on what accessory.
 Using an eye spawner gives 20p but only when on the surface. We could try to string rewards to force this by making the ai warp home, then pop it for them.
Attacks that hit enemies are rewarded. Hitting a boss even moreso. Missed attacks may be decremented but this may scare the AI from trying to attack.
Killing the eye of Cthulhu will give 1000 points. This is the final goal of the program so this will be a highly rewarded solution.
This may be complicated but giving the AI points for going deeper is a good idea.

Decrements
Idling gives -0.01p per full second of no input.
Damage gives -0.1p per hit.
Death gives -2p
Unequiping a good accessory takes the points that were given by having it equipped.
Trashing a good weapon is -50p
The inventory space, if maxed out, will decrease 0.1p per second when it is full.
Dropping a good item will decrease points.

It is worth noting a lot of this is due to change. Tweaks will need to be made, issues will be encountered, etc. This is just "the plan."




	

