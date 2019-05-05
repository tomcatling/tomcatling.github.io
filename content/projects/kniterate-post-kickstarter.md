Title: Kniterate Post KickStarter
Date: 2017-08-21 10:01
Modified: 2017-08-21 12:30
Slug: kniterate-post-kickstarter
Authors: Tom Catling
Tags: kniterate, china, kickstarter, update
gallery:kniterate-post-kickstarter

Well, I have been back in China again making knitting machines with Kniterate.

We concluded our Kickstarter campaign in May and raised a whopping $636k! We have since redesigned the electronics of the machine to be a bit more industrial and I took a few weeks away from work in the UK in August to go over to the factory near Shanghai and integrate the new boards into the prototype. I have also rewritten the firmware to be a lot faster and more modular/manageable. I learned a lot about RS485, acceleration profiles, interrupts and various board-board communication standards during this process!

I'm not supposed to post any pictures of the machine innards here, so here is a small collection of pictures summarising my time in China instead. 

My next task will be to work on the backend algorithms which allow us to go between a user-intelligble design file and machine code - what we call 'k-code.' The electronics and firmware are both now in a state where it makes sense to hand them over to new people to spread the knowledge around. 

I have already written some basic slicing algorithms which we used in the campaign to make the garments shown below. On the left is our first six-colour sample with the corresponding technical face, and on the right are some garments we made in a collaboration with the very cool Lindsay Degen.

Slicing for knitting is a really interesting problem and potentially very complex. The examples given below are about as simple as it gets: flat double-knit with minimal shaping and no fancy stitches. Initially we must limit the users freedom to make it manageable, but in the future I would love to work on some kind of generalised solution (similar to [this](https://www.disneyresearch.com/publication/machine-knitting-compiler/) awesome paper from Disney Research).
