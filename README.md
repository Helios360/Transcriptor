# Transcriptor
A simple script that log in to discord via a browser (geckodriver) then records the sinked output with a record sink  

Don't forget to setup the my-venv python environment with the requirement
Don't forget to set the correct geckodriver path
The server also needs a screen and a mouse+kb I think
When launching from ssh don't forget to change the display fowarding, the start.sh should do this itself

To launch the program from one ssh command you can :

ssh -Y user@[ServerIP] "cd [PATH TO START.SH] && ./start.sh"

Have fun with it
