import random

funny_facts = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and it said 'no problem, I’ll go to sleep.'",
    "My AI brain is 99% jokes and 1% functionality.",
    "Did you know? Sloths can hold their breath longer than dolphins!",
    "Fun fact: You blink 20 times per minute… unless you're watching Netflix.",
    "Why was the robot so bad at soccer? It kept kicking up sparks!",
    "Programmers don’t have bugs, they have unexpected features.",
    "I was going to tell you a joke about time travel… but you didn’t like it.",
    "The best way to get a programmer’s attention is to say 'free pizza'."
]

def get_random_fact():
    return random.choice(funny_facts)
