#ELIZA.PY
#Created by: Srijan Yenumula            G number: G01045321

#References: [1] Fernando, Luis. "PyEliza: A python bsed implementation of the famous computer therapist (2016)." http://workshop.colips.org/re-wochat/documents/12_Paper_16.pdf
#            [2] Weizenbaum, Joseph. "Computer Logistics (1966)." http://web.stanford.edu/class/cs124/p36-weizenabaum.pdf


#Intro: This Eliza.py is created to play the role of a psychotherapist. It can recognize few of the words defined and respond back accordingly. It can have a conversation with the user and ask a few question to the user based on the user's questions/answers.

#Example of input and output of ELIZA.PY run in the Mac terminal
#Eliza: What is your name?
#User: Srijan
#Eliza: Hello Srijan, How can I help you tody ?
#User: I want to rule the world
#Eliza: How much does it mean to you if you get to rule the world?
#User: Bye
#Eliza: See you soon, It was pleasure talking to you (and terminated)

#Algorithm it follows
#Step 1:  Starts of with a pre-defined question "what is your name"
#Step 2:  Analyzes the name and asks "how are you feeling today"
#Step 3:  Based on the response, it analyzes the string provied by the user
#Step 4:  Search the string for a pattern with the pre-defined statements
#Step 5:  Provides a macthed response for the given string
#Step 6:  Takes Bye/ Quit to end the onversation
#Step 7:  Program is terminated

# importing packages Re for reading regular expression and random is for       getting a random response
import re
import random

# regular expressions used and the responses Eliza would use
expression = [
    [r'[H|h]ello(.*)',
     ["Hello, How can I help you?",
      "Hi there, how are you today?",]],
              
    [r'[I|i] need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]],
 
    [r'[W|w]hy don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],
 
    [r'[W|w]hy can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]],
 
    [r'[I|i] can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],
 
    [r'[I|i] am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]],
 
    [r'[I|i]\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?"]],
 
    [r'[A|a]re you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "Would you prefer it if I were not {0}?",
      "Perhaps you believe I am {0}.",
      "I may be {0} -- what do you think?"]],
 
    [r'[W|w]hat (.*)',
     ["Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],
 
    [r'[H|h]ow (.*)',
     ["How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],
 
    [r'[B|b]ecause (.*)',
     ["Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"]],
 
    [r'(.*) sorry (.*)',
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
 
    [r'[I|i] think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}?"]],
 
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
 
    [r'[Y|y]es',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],
 
    [r'(.*) Eliza(.*)',
     ["Are you really talking about me?",
      "Does it seem strange to talk to me?",
      "How does Eliza make you feel?",
      "Do you feel threatened by me?"]],
 
    [r'[I|i]s it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "It could well be that {0}."]],
 
    [r'[I|i]t is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],
 
    [r'[C|c]an you ([^\?]*)\??',
     ["What makes you think I can't {0}?",
      "If I could {0}, then what?",
      "Why do you ask if I can {0}?"]],
 
    [r'[C|c]an I ([^\?]*)\??',
     ["Perhaps you don't want to {0}.",
      "Do you want to be able to {0}?",
      "If you could {0}, would you?"]],
 
    [r'[Y|y]ou are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"]],
 
    [r'[Y|y]ou\'?re (.*)',
     ["Why do you say I am {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],
 
    [r'[I|i] don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?"]],
    [r'[I|i] feel (.*)',
     ["hmm, tell more about it.",
      "Have spoken about being {0} with anyone else",
      "What do you think about being {0}",
      ]],
 
    [r'[I|i] have (.*)',
     ["What do you think about having {0}",
      "{0},a lot of people are having it."
    ]],
 
    [r'[I|i] would (.*)',
     ["Why would you {0}?",
      "Why would you {0}, can you explain to me more about it"
    ]],
 
    [r'[I|i]s there (.*)',
     ["I am not sure about {0}",
      "What is your opinion ?"
    ]],
    
    [r'[Y|y]ou (.*)',
     ["Why do you say that about me?",
      "We have limited time, so let us stick with you"
    ]],
 
    [r'[W|w]hy (.*)',
     ["The answer is within you",
      "Oh, Why do you think {0}?"
    ]],
 
    [r'[I|i] want (.*)',
     ["Why do you want {0)?",
      "How much does it mean to you if you get {0}?",
      "are you sure, Why do you want {0}?"
    ]],
         
    [r'[B|b]ye',
     ["Thank you, come again",
      "Thank you , will call your mobile soon to find out how you are doing",
      "See you soon, It was pleasure talking to you."]],
    
    [r'[q|Q]uit',
     ["Thank you, come again",
      "Thank you , will call your mobile soon to find out how you are doing",
      "See you soon, It was pleasure talking to you."
    ]],
 
    [r'(.*)',
     ["Can you tell me more.",
      "I didn't quite understand, can you say that another way",
      "Hmm...lets talk about you..So, Tell me more about yourself.",
      "Pardon me, shall we talk about you?",
    ]],
    
    [r'[m|M]y name is (.*)',
       ["{0}!, that is a good name" 
    ]]
] 

# Changing the type of words used by the user in the question to how Eliza would respond back
transform = {
    "am"   : "are",
        "was"  : "were",
            "i"    : "you",
                "i wouldd"  : "you would",
                    "i have"  : "you have",
                        "i will"  : "you will",
                            "my"  : "your",
                                "are"  : "am",
                                    "you have": "I have",
                                        "you will": "I will",
                                            "your"  : "my",
                                                "yours"  : "mine",
                                                    "you"  : "me",
                                                        "me"  : "you"
}
# Defining the function process(), this function accepts  matched response from check() and transforms 
# it with corresponding values from dictionary- transform
def process(data):
    tokens = data.lower().split()
    for i, token in enumerate(tokens):
        if token in transform:
            tokens[i] = transform[token]
    return ' '.join(tokens)
 
 
# Defining the function check, this matches the input string with a pattern/regular expression from the list-expression
def check(string):
    for pattern, responses in expression:
        match = re.match(pattern, string)
        if match:
            response = random.choice(responses)
            return response.format(*[process(g) for g in match.groups()]) # this statement passes the string as well as the index of the characters.
 
#defining the main function which starts the interaction with the user. 
def main():
    print ('What is your name?')
    
    name=input()        # accepting the name as string
    name=re.sub('[M|m]y name is','',name)
    logic=name.isspace() # This checks if the input string 'name' is space or not
    while (logic == True):  # this loop will run as long as the variable has "True" in it
        print ( 'Sorry you must enter a name, leaving blank is not an option')
        name=input()
        name=re.sub('[M|m]y name is','',name)
        logic=name.isspace()
    while (name != ' ' or ''):
        print ('Hello ' + name.rstrip("!@#$%^&*()?") + ', how can I help you today ?')
        break  
    while True:
        statement = input()
        print(check(statement)) # calling function check 
 
        if statement == "quit":
            break
        if statement == "bye":
            break
 
 
if __name__ == "__main__":
    main()
