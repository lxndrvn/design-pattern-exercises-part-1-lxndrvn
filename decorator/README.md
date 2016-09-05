
## 2. Decorator

Extend the LogSocket (what we used in the examples) with an "Obscene word filter functionality", so the name can be ObsceneFilterSocket.

Detect when the server sends obscene words through the socket, as the following:

* Define a list of obscene words (5-10 is enough, not necessary to list all of them :-))
* If the data (to the client) contains any obscene word, filter these words out and put only * (star) signs.
* If you want to make your solution nice, you can use the Regular Expression functions in Python.

Apply the Decorator design pattern!
