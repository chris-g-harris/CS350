# participants.py
# A simple python program to print the participants from the class.
# Intended as an example of updating code on GitHub.

def main():
    numPeople = 13 # number of students + instructor

    # Add your name to the list below to the right of any other names.  
    # I have added my name plus a placeholder for your name. Replace the placeholder with your name.
    # The last person to push the file to the repository should ensure the <your name here> placeholder is removed.

    people = ["Christopher Harris", "Evan Minor", "Lauren Simms", "Vandiver David", "<your name here>"]

    # don't change anything below this line\n",

    for i in range(len(people)):
        print("{0:2d}. {1}".format(i+1, people[i]))
              
    print("\nNumber of People: %2d" %(i+1))
    print("Percentage of People: {:.1%}".format((i+1)/numPeople))
