# pydj
A music player that automatically crossfades songs at predetermined points

20% of the work that DJs do is determining what part of what songs should be played at any given point. However, this accounts for 80% of the quality of the performance. Most of the work comes from manually transitioning songs, beat matching, applying filters, etc. Pydj allows users to automate the first 20% of DJing by using a basic queueing function in conjunction with predetermined crossfading points. By adding crossfading points into a csv, users only have to prepare a song once instead of doing it every time they play it. This provides an efficient way to play the best parts of the best songs without having to do any work in real-time.


## Usage
The physical song files in this demo cannot be uploaded to Github because it is copyrighted media. To run this program, song files must be added into a pickle file called soundFiles. These audio files should correspond to the entries in setlist.csv. In this csv, the "Start" column is when the song will start to be faded in, "Fade_in" is the number of seconds the crossfade will take, and "End" is when the song will fade out. This program is designed to run in a linux terminal by using the command "python pydj.py". 

