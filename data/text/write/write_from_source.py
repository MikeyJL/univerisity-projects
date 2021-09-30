input_path = input("\nEnter INPUT file path\n>>> ") or "../read/quotes.txt"
output_path = input("\nEnter OUTPUT file path\n>>> ") or "output.txt"

try:
    with open(input_path, "r") as file:
        lines = file.readlines()
except IOError:
    print("ERROR: Please specify a valid input path.")

try:
    with open(output_path, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print("The data has been written to the file.")
except IOError:
    print("ERROR: Please specify a valid output path.")

"""
** Input **

None for both prompts
"""

"""
** Txt output **

No one has ever become poor by giving. [Anne Frank]

What’s in a name? A rose by any other name would smell as sweet. [Shakespeare]

Let the beauty of what you love be what you do. [Rumi]

The time is always right to do what is right. [Martin Luther King, Jr.]

Few are those who see with their own eyes and feel with their own hearts. [Einstein]

In a gentle way, you can shake the world. [Gandhi]

Feet, what do I need you for when I have wings to fly? [Frida Kahlo]

What is done cannot be undone, but one can prevent it happening again. [Anne Frank]

Wherever you are, and whatever you do, be in love. [Rumi]

I paint flowers so they will not die. [Frida Kahlo]

Only from the heart can you touch the sky. [Rumi]

I hear and I forget. I see and I remember. I do and I understand. [Confucius]

"""