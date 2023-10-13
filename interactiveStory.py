batt = 5
print("\033[1mThe Dark Cave")
print       ("_____________\033[0m")
name = input("\nWhat is your name? > ")
print("\nYou find yourself in front of a dark cave in the middle of a deep, dark forest.")
print("It is storming outside, and you choose to venture into the cave to shield yourself from the rain.")
print("It is exceptionally dark inside the cave, luckily you have a flashlight.")
print("""As you wander deeper into the cavern, you notice two reasonably large holes on top of each other, each large enough to allow you enough room to stand.
      The top hole seems hard to ger into, and seems quite slippery, while the bottom hole is much more dry, but seems to contain more stalagtites and stalagmites.""")

stages = {
    1: {
        'q': "Do you go in the upper hole or the lower hole?",
        'r': {
            'u': """After some effort, you manage to climb into the upper hole. It seems to slope in an upward direction and there is a distinct lack of stalagtites and stalagmites.
            As you continue forward, you eventually see a large hole in the ground and a small crevice ahead of you.
            The hole is dark, but you think you can see the glint of water at the bottom.""",
            'd': """You meander through the tunnel, eventually hearing more and more water droplets.
            You stumble, but it is easy to regain your balance, however, as you look behind you, you see that the dry path which seemed so inviting had collapsed behind you, trapping you indefinitely."""
        }
    },
    2: {
        'q': "Do you jump across the gap or take a chance at falling into it?",
        'r': {
            'u': """You take a few steps back, and leap across the gap.
            Your heart drops as you begin to fall, and your mind begins to run wild with what could happen if you fell.
            Just as soon as your life flashed before your eyes, you felt your foot make contact with the hard rock on the other side.
            As you rolled over on the other side into the fetal position, you finally breath a sigh of relief.
            
            When you finally recover, you shine your flashlight over a hole in the ground, shooting straight down and just managing to fit you widthwise. Just above this hole on the wall in front of you is a thin crevice, which seems to go up at an angle""",
            'd': """You take a leap of faith into the deep hole, but as you get closer to the supposed pool of water, it turns out to merely be a puddle. 
            You break both of your legs and begin to realize that there is no other exit."""
        }
    },
    3: {
        'q': "Do you climb through the upper crevice or go in the lower hole?",
        'r': {
            'u': """You were eventually, after some effort, able to get through the crevice.
            As you kept on crawling, it began to get tighter and tighter, until eventually you got stuck.
            Trying to get out got you nowhere, and you eventually suffocated.""",
            'd': """"""
        }
    } 
}

correctAns = ["u", "u", "d", "d", "l", "r", "l", "r", "a", "b", "start"]

def questions(temp):
    print(temp)

for i in range(7):
    print("temp")