# needs pick to install on windows run this command:
# python -m pip install pick

from pick import pick

messages = {
    "Matt": "Its been great working with you and i have learnt alot, But good luck in bigger and better things :)",
    "Alomski": "It’s sad to see you go but i guess you need to do what’s best for you. Thank you for all the support you have given throughout my Hyde journey. Without you and Tiz I would not be in the position I’m in. All the best and good luck.",
    "Paresh": "Thanks for your help over the years, good luck in the new job",
    "Adrian": "Congratulations on your new job. It’s been great working with you, all the best",
    "Nick": "Great working with you and thanks for all the knowledge sharing over the years. May your feathers always be bright, and your beard grow ever longer",
    "Sam R": "Thanks for all your help over the years Jay, good luck with your new job",
    "Sara": "Dear Jay,\nWishing you the very best of luck, not that you need it. You’ll be missed round here – who am I going to talk to now?!\nKeep in touch,",
    "Mohammed A": "Thanks for all the support and guidance over the years, good luck on your new venture.",
    "Carole": "Good Luck in your new role Jay, and thanks for all your help and support over the years, it has been great working with you, \nBest Wishes",
    "Stephan": "Thanks a lot for your hard work and passion. I'm sure and hope we will have another opportunity to work together on new technologies. Good luck.",
    "Scott": "Jay, it’s truly been a pleasure working with you these past few years. Your patience and ability to coach technical skill has really made a difference to my time at Hyde and a combination of which the team will not be able to replace.\nPlease don’t be a stranger and good luck with the new adventure, I am sure you'll smash it.",
    "Simon": "Good luck in the new job and stay in touch! We'll see you for a beer in Rochester soon. All the best.",
    "Mantas": "Without new challenges, one stops to grow. Enjoy your new job!",
    "Eugene":"Jay,\nthanks for help and support, especially in the start!\nGood luck at your new place!\nThey are lucky to have you on board!",
    "Dayana":"Thank you so much Jay for all your help to the integration team.\n\nWe truly enjoyed working with you and appreciate you were always available to help us. We wish you much joy, happiness and all the success in everything you do!\n\nAll the best!",
    "": "It's dangerous to go alone! Take this:\n\n       /|________________\nO|===|* >________________>\n       \|",
}

janky = "yes"
options = [*messages]
options.append("Exit")

while janky == "yes":
    title = 'Please choose the message you would like to see: '
       
    option, index = pick(options, title)
    
    if option != "Exit":
        print("\n" * 5, "#" * 100, "\n" * 2)
        print(messages[option])
        if option != "":
            print("     ",option, sep="- ")
        print("\n" * 2, "#" * 100, "\n" * 2)

        input("Press Enter to continue...")
    else:
        janky = "NO"
        print("\n" * 10)
        print("Thanks for all your hard work")
        print("\n" * 3)