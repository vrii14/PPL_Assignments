In this assignment we executed two C programs(recursive-factorial & stack smashing) and made stack frame diagrams for the same.
This helped to learn about the internal working of the program and the way reqisters and IP adresses play the role. I did the 
following in this assignment:-
1. First is a simple recursive program of a factorial, which I executed using gdb and adding break points in the same and
I made a stack frame for it.
2. Second was to performing stack smashing in a program.I tried it both ways using and not using a stack protextor while running
it. I basically created two functions other than the main and called one of the functions(overflow) inside main. And then performed
stack smashing in the overflow function and manually replaced the rip register by the IP address of the third function so that
instead of returning back to main it goes into the third function(virus) and then at its end gives a segmentation fault since 
it does not know where to return.
