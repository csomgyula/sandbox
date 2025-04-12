# wsurl

A vibe which is in spirit similar to cURL:

- shall run a snippet
- should avoid interaction (if possible)


something like this:

```bash
wsurl [-H header] ([--send message] [--wait wait_args]])* server
```

## samples

### connect

connect and do nothing else:

```
wsurl --send "ping" wss://...
```

problem:

- to discover what? we can 
	- connect

### send

connect, send a message (such as e.g. ping) do not read:

```
wsurl --send "ping" wss://...
```

problem:

- to discover what? we can 
	- send

idea:
- ping is builtin wss command so we may provide an abbreviation:

```
wsurl --ping wss://...
```


### listen

listen, do not send

```
wsurl --listen wss://...
```

problem:

- to discover what? we can 
	- receive	
		- if 
			- the server sends without client request (poll, noti)
			- or we trigger such in another window
		- question:
			- will this lead to a double (multiple) client scenario? in vasmegyer?
- without timeout it requires interaction, a better one is:
	```
	wsurl --listen --till 10s wss://... > out.txt
	```
	- and `till` has a `1-10s` default
		- because 
			- beyond 10s it is too much for a non-interactive app to wait	
				  or
				- it it may be too much messages 
			- below 1s the server may have nothing to send.
	- problem:
		- even `4-10s` can be much in a monitoring app such as vasmegyer, which polls every 2 secs and sends large volume of datan, a better one is:	
		```
		wsurl --listen --till 10s --messages 2 wss://... > out.txt
		```
			- and `messages` has `1` as default
			- question: 
				- such a bounded form of listen may well receive a name which better fits it, such as receive that is: would not it be better to call it `receive`


### more complex


```
- wsurl --listen --till 10s --for "xxx" wss://...
```

so we have to implement response processing, such as regexp or even more complex...

```
wsurl --send "ping" --listen --till 5s wss://...
wsurl --send "ping" --listen --for "pong" wss://...
wsurl --send "ping" --listen --for "pong" --till 5s wss://...
```

so we have to implement a mini shell-like programming langue out of program arguments...