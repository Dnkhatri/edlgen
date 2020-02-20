# edlgen

Generate edl files with timings for intro and outro for kodi with manual input

This is just a command line python script to generate edl files when you know how long the intro and outro are in a series
It can be run from terminal and will take as inputfile seconds(To skip for intro) seconds(To skip for outro) > 

# example

</b> edlgen.py "inputfile" 30 70 > outputfile.edl

or this for all mp4 files in a directory

for i in 	&#42;.mp4; do edlgen.py "$i" 30 70 >"${i%.*}.edl"; done

The script will read the total runtime of the video file and generate an edl as below with the 2608.48 being the total runtime of the video

0.0 30.0 3
2538.48 2608.48 3


Currently I am using option 3 for Commercial Break as stable version of kodi does not support intro and outro yet.
Once it does will change accordingly

0 - Cut 
1 - Mute 
2 - Scene Marker
3 - Commercial Break
4 - Intro
5 - Outro
