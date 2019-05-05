Title: Tunebook Modernisation with LaTeX and ABC
Date: 2017-11-19 10:01
Modified: 2017-11-19 12:30
Slug: tunebook-modernisation
Authors: Tom Catling
Tags: music, .abc, automation
template:article
gallery:tunebook

I've been doing some calling and playing with the UCLU Ceilidh Band recently. Our tunebook is a much-edited PDF that has been handed down through generations of students. Some pages are scans of photocopies, annotated by hand and becoming fairly illegible. PDF doesn't understand music so it's impossible to edit notes or transpose things. I am also forever losing pages and entire copies because I normally print it out in a rush and don't have time to bind it. When I do have a copy it's normally mixed up and very difficult to find a certain tune...

<p align="center">
<img src="{static}/images/messy_tune.png" alt="Messy tune image" width="80%"/>
</p>

Enter ABC notation! This is a pretty old-school text format for music, and many of the tunes in our book are already written out in ABC on sites like thesession.org. ABC was introduced in the early 90s and has since become pretty sophisticated. It's designed to be human readable (some musicians can sight read ABC as fluently as sheet music) and is more than sufficient for transcribing tunes with chords and a couple of different parts.

```
X: 1
T: Cooley's
R: reel
​M: 4/4
L: 1/8
K: Edor
|:GF | "Em"EBBA B2 EB |"Em"B2 AB "G"dBAG |"D"FDAD "G"BD"D"AD|"D"FDAD "Bm7"dAFD |
       "Em"EBBA B2 EB |"Em"B2 AB "G"defg |"Bm"afec "Bm7"dBAF|"D"DEFD "Em"E2   :|
 gf |:"Em"eB ~B2 efge |"Em"eB ~B2 "G"gedB|"D"A2 FA DAFA     |"D"A2 FA "Bm"defg |
       "Em"eB ~B2 eBgB|"Em"eB ~B2 "G"defg|"Bm"afec "Bm7"dBAF|"D"DEFD "Em"E2   :|
```

<p align="center">
<img src="{static}/images/cooleys.png" alt="Cooleys" width="80%"/>
</p>

Combining this with LaTeX and the CTAN ABC package to generate sheet music allows me to create a tunebook that can be rebuilt with a single command. Here it is on GitHub! (still a work in progress)

All tune sets are stored in ABC format in separate files to allow for easy editing, and it's even possible to transpose pieces easily with tools like mandolintab. The table of contents at the start is automatically regenerated, images inserted etc. LaTeX is great.

I found original high-resolution images where possible and even touched up the front cover. I intend to make five or so hardcover copies to keep with the band so we always have decent music to read from. 

I had to do some experimenting with gluing a printed cover onto mounting board. Final copies will be printed double-sided, but the above images give you an idea of what it will look like. Very satisfying!
