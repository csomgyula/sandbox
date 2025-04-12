class Shell:
    """
    - Role: 
        - manage console
        - mediate between user/display and network/web socket server    
    
    Display
    =======
    The shell implements a ChatGPT-like prompt-based text UI where the prompt is a separate UI block from the message outputs:

        ------------------------------------
                    title ($mode)
        ------------------------------------
        messages



        ------------------------------------
        prompt        
        ------------------------------------
    
    The communication with the server, how messages appear is controled by shell's mode. The mode can be in either of two modes: Dialogue or Monologue:

    Monologue
    ---------
    
        ------------------------------------
                    title (dialogue)
        ------------------------------------
        user:   command_1
        server: message_1
        user:   command_2
        server: message_2


        ------------------------------------
        prompt        
        ------------------------------------

    The Dialogue is a shell mode when the application executes user commands and displays responses.	
    
    Listen
    ------

        ------------------------------------
                    title (listen)
        ------------------------------------
        server: last message



        ------------------------------------
        prompt        
        ------------------------------------
    
    In Listen mode the application listens to the connected Web Socket server and automatically displays server responses
          
    Reference
    ---------
    - mode
    - title
    - messages
    - dialogue_messages
    - listen_messages
    - prompt

    The application uses the Open Source [Textual](https://github.com/textualize/textual/) library.
        
        
    Functions
    =========
    - /process
        1. /manage/start -> /serve
        2. /serve -> /disconnected
            1. connect -> /connected
            2. (send|listen|close -> /disconnected)*
            3. quit -> /manage/stop
            - /serve/log
        3. /manage/stop
        - error: TODO    
    - /manage
        - begin start [args]: Application -> . -> ?
        - log....
        - end stop
    - /serve 
        - connect [args] server: prompt -> . -> network
            - result normal connected | error: -> messages
            - set connected to false
            - forward to network
        - send [args] [server] message: prompt -> . -> network
            - result normal (sent | sent-received) | error: network -> . -> messages
        - listen [args] [server]: prompt -> . -> network:
            - callback? received args: messages <- . <- network   
        - close
        - quit -> /manage/stop      
        - log -> /manage/log
    
    Network  
    =======
    - -> network: Network
        - address: String
        - connected: boolean
    """
        
    class mode:    
        """
        The shell can be in either of two modes: Dialogue or Monologue:

        - In the dialogue mode the console acts like a shell: the application executes user commands and displays responses.	  
        - In the listen mode, the application listens to the connected Web Socket server and automatically displays server responses

        The Dialogue is the default mode, when the application is started. So by default the user can use the TUI as a shell and issue command to the application, such as e.g. can connect to the WebSocket server, send
        message to it and receive response. 

        The TUI switches to listen mode when the user issues the `listen` command. (Note that `listen` can be only executed when the server is already connected). Then TUI switches to the monologue mode of the server, which means server messages are automatically displayed in the Messages widget, more specifically in the Monologue Messages widget. Issuing other command than listen switches back the TUI to normal.

        Reference
        ---------
        - Name: mode
        - Role: Displays the shell mode, which can be either Dialogue or Monologue
        - Memory:
            - Relations:
                - title: Title
            - Children:
                - state: Dialogue | Monologue
        - Processes:        
            - Reactions: 
                - init state=Dialogue, title: Title -> . -> state, title: 
                - set new_state: Parent -> . -> state, title: TODO
        """
        
    class title:
        """
        Reference
        ---------
        - Name: title
        - Widget: https://textual.textualize.io/widgets/label/
        - Role: Displays title of the application and mode, e.g. "WebSocket Shell (dialogue mode)"
        """
        
    class messages:
        """
        The CLI uses two different displays depending on the Mode:

        - Dialogue Messages: displays user commands and responses to them
        - Monologue Messages: automatically displays server responses

        Hence the Messages block is a switch between these two Messages views.

        Reference
        ---------
        - Name: messages
        - Role: display messages according to the current mode
        - Memory:
            - current: the current Messages view, either Dialogue Messages or Monologue Messages
              (Note this is inherited from the Textualize widget)
        - Reactions: 
            - init -> . : TODO
            - Mode -> . -> current:
                - switch current Messages block according to mode
        - Base widget: https://textual.textualize.io/widgets/content_switcher/    
        """
        
        class dialogue:
            """
            display commands and server responses in dialogue mode
            """
            
        class listen:
            """
            automatically display server messages when in monologue mode
            """
        
    class prompt:
        """
        where user types in command
        """
    
    