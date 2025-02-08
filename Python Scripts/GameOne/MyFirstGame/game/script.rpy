default Josh = Character('Josh', color="#1E90FF")
default Megan = Character('Megan', color="#FF69B4")

label start:
    "A new beginning..."
    "Josh" "Wow... I can't believe it. Grand Rapids, my new home."
    "Josh" "The house is perfect, and guess what? I adopted two puppies!"
    
label home:
    scene bg house with fade
    show josh happy
    "Josh" "Megan, come see them! They're already running around like crazy."
    show megan smile
    "Megan" "They're adorable! What are their names?"
    "Josh" "I was thinking Max and Luna. What do you think?"
    "Megan" "I love it!"
    
label travel:
    scene bg airport with fade
    "Josh" "We’ve traveled so much already. But come spring..."
    "Megan" "Charleston is next!"
    show josh excited
    "Josh" "I can't wait for the beaches, the food, and the history."
    
label choices:
    Josh "Are you excited for Charleston?"
menu:
    "Yes!":
        jump excited_response
    "I'm not sure yet":
        jump unsure_response

label excited_response:
    Megan "Me too! It'll be another adventure."
    jump trip_common

label unsure_response:
    Megan "Well, I promise it'll be worth it!"
    jump trip_common

label trip_common:
    Josh "Either way, it's happening. Get ready for some fun!"
    return
