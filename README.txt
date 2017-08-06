Project description:

	This instant messenger application was written by Mathews Fazza and Nickolas Ramos for the class CS4390-0U1 Computer Networks.  The application written in Python receives requests from users and authenticates them into the server.  The server manages chat requests, history logs, and the chat relaying.
	We were able to coordinate the coding collaboration through github.  Mathews focused on Server.py and Client.py, while Nickolas focused on the Functions.py and and everything realted to fileIO.



Project architecture:

	The application was designed with three files in mind: Server.py, Client.py, and Functions.py.  The functions file contains all the functions that are used across the other files.  That was done in order for us to work on different files without influencing what the other was doing. 
	The way used to authenticate users is comparing the user id of the client requesting a connection to a preset list of authorized users.   In order to log users into the system, a new entry is created in the “online” dictionary.  Online has the following form: ‘user’: chatnumber.  If the user is online, its id shows in online. The chatnumber field is an integer that has the number of the chat session that user is engaged in. If the number is zero, that means the user is online, and available for a new chat session.  Users are also identified with their respective sockets.  An online user will have an entry in a dictionary of sockets in the following format: ‘user’: socket.
	The server uses a listening socket that indefinitely accepts connections from users.  The listening happens in its own thread called backgroundtask.  That thread is never terminated unless the user shuts the server down.  Once a user connects to the system, the background task will spraw a new thread for that user (called individualtask).  All the interaction between the client and the server is going to be managed by this new thread.
	The individualtask receives the user’s id as an argument.  That is useful in order to identify the user in the list of online users, and in order to identify the socket relating to that user.  Every time a client sends a message, that message has a protocol attached to it.  The protocol is checked by the server (inside individualtask) that in turn determines what to do with the request.  That request can be for a chat session to start, a chat session to end, history logs to be displayed, messages to be displayed between clients, etc.  All the protocols are described below.
	On the client side, the client connects to the server, makes requests, and logs out when all the activity is to be ceased.





Project directions:
	In order to run the project.  All three files must be in the same folder.  Server.py should be run first and Client.py should be run later.  Nothing needs to be done in order for the servide to run, however, terminating the server requires manually terminating the program (with control + z).
	The Client.py will prompt the user to enter a user name.  There’s a validation in place to make sure the user name is in the correct format.  Once the user name is accepted, all the user needs to do is type “log on”.  If the user is in the list of authorized users, the client will connect to the server.  Once connected, you may type HELP at anytime to read instructions on how to run the program.  
	In order to initiate a chat with another user, simply type CHAT_REQUEST(user1-user2).  The server will check the availability of the users and if they are available, it will create a chat session.  Once in chat mode, all that needs to be done is typing is pressing enter to send and receive messages to/from the other user engaged in the same chat session.  To end a session, just type END_REQUEST(session number).  Other things that can be done by the user include requesting history logs(HISTORY_REQ(user1-user2), asking for help (HELP), asking for the current chat session number (SNUM), and logging out (just type ‘log out’).
