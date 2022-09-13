# Mads lib Generator
# game words by reader to create story can relate to silly sories as fun

# words request from user
adjective1 = input("Enter an Adjective : ").lower()
game = input("Enter the name of an outdoor game :").lower()
adjective2 = input("Enter another adjective 2 : ").lower()
friend = input("Enter the name of a friend: ").capitalize()
verb = input("Enter a verb : ").lower()
adjective3 = input("Enter one more adjective: ").lower()

# story template
story = f"It was a {adjective1} summer day at the beach. My friends and I were in the water playing {game}. As a {adjective2} wave came closer, my friend {friend} yelled, Look! there's a jellyfish {verb}! As we got closer, we saw that the jellyfish was indeed {verb}! {friend} ran out of the water and onto the sand. {friend}  the rest of us stayed in the water playing {game} because {verb} jellyfish are {adjective3}."
print(story)
