from tkinter import *
root = Tk()
root.geometry("1000x800")
root.title("Bottle Cap")
frame=Frame(root)
root.minsize(40,70)

def resetwindow():
    for widget in root.winfo_children():
        widget.destroy()


def A7():
    resetwindow()
    t20="You and your friends picked the right door. You enter the room.It is pitch black. You are trapped. And you never see the light again!"
    Label(root,text=t20).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()

def B7():
    resetwindow()
    t21="You and your friends picked the left door. Congratulations! You find your way to the back door. You are all relieved and run back to your camps with some memories you will never forget!"
    Label(root,text=t21).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()


def A6():
    resetwindow()
    t18="You chose the left door! Congratulations! You eventually find the back door. You call out to your friends in the other group.\nBut to your horror, you can hear them scream,'You guys run for your lives! This thing won't leave us!'"
    Label(root,text=t18).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()

def B6():
    resetwindow()
    t19="You choose the right door. You enter the room. It is pitch black. You are trapped. And you never see the light again!"
    Label(root,text=t19).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()

def A5():
    resetwindow()
    t14="You have split up and now have to decide which door to pick. What do you do?"
    Label(root,text=t14).grid(row=0,column=0,sticky=W)
    t15="A. Your group decides to pick the left door and the other group decides to pick the right door.\nB. Your group decides to pick the right door and the other group decides to pick the left door."
    Label(root,text=t15).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A6).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B6).grid(row=4, column=0)

def B5():
    resetwindow()
    t16="You have decided to stick together. Which door do you pick?"
    Label(root,text=t16).grid(row=0,column=0,sticky=W)
    t17="A. You pick the right door.\nB. You pick the left door."
    Label(root,text=t17).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A7).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B7).grid(row=4, column=0)



def B4():
    resetwindow()
    t11="All of your efforts are in vain. Your screams and cries are futile. The rooms are getting very dark. You friend turns on their flashlight.\nYou suddenly hear confused screams. They are all pointing at you. Your friend has broken down into hysterical sobs. You wonder what's wrong! You look down and see a bow sticking right through your heart. And you slowly feel your eyes close and the next thing you see is darkness!"
    Label(root,text=t11).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()

def A4():
    resetwindow()
    t12="You go around searching for a back door. You walk down the dark hallways and as you all pass by statues of various Gods, you murmer a silent prayer.\nYou hear some whispers once in a while and all your friends confirm that they can hear it as well. All of you are terrified.\nYou reach a dead end and see two doors, one on the left and one on the right. What do you do?"
    Label(root,text=t12).grid(row=0,column=0,sticky=W)
    t13="A. You decide to split into two groups with one group going through the left door and one group going through the right door.\nB. You decide to stay together and go with your instinct to pick a door."
    Label(root,text=t13).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A5).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B5).grid(row=4, column=0)

def A3():
    resetwindow()
    t8="You look around but see everything in it's place. You start walking back to your group but then see something you just cannot believe.\nAmongst the statues, you see a stunning white marble statue of your mother. You freeze at this sight and your spine runs cold as you see the mouth of the staue opening slowly. You hear her say, ' Come with me, my child!' And the next thing you see is darkness!"
    Label(root,text=t8).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()

def B3():
    resetwindow()
    t9="You've all walked for a long time. A friend suggests that you head back because everyone was getting hungry. You all agree and turn back to get out.\nSuddenly, you hear the door of the temple slam shut! You and your friends rush to the nearby windows to try and open them but in vain!\nWhat would you do next?"
    Label(root,text=t9).grid(row=0,column=0,sticky=W)
    t10="A. You and your friends turn on your phone flashlights and decide to go in search of a back door.\nB. You and your friends decide to stay wherever you are and try and break down the front door."
    Label(root,text=t10).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A4).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B4).grid(row=4, column=0)

def A2():
    resetwindow()
    t5="Shortly after you made your wish, you get a call from your manager.\nThe money you invested in stocks just touched the peak and you had earned a billion dollars!\nJust when you couldn't believe your luck, your manager hits you with the harsh news. Immediately after that happened, the stocks took such a dip that you ran into a huge loss.\nYou are asked to immediately return home. Tough luck!"
    Label(root,text=t5).grid(row=0,column=0,sticky=W)
    Button(root, text="Exit", command=root.quit).pack()

def B2():
    resetwindow()
    t6="You wait there with a pounding heart, but nothing seems to be happening. Your friends comfort you but you laugh it out thinking about how you actually expected something to happen.\nYou decide to keep exploring. You are in awe of the beautiful white marble statues that pave the way to the entrance.\nYou suddenly hear something and from your peripheral vision, you think you saw one of the statues move ever so slightly. You turn back but find everything still. What do you do next?"
    Label(root,text=t6).grid(row=0,column=0,sticky=W)
    t7="A. You decide to slowly separate from the group to investigate on your own.\nB. You think that it was just your imagination and keep walking with your friends."
    Label(root,text=t7).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A3).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B3).grid(row=4, column=0)


def A1():
    resetwindow()
    t3="\nWow! That was courageous of you! Once you get into the premises of the temple, you find an old well, all covered in creepers.\nThere is a half bent sign stuck beside it. You look closely to see what it reads. 'Be careful what you wish for. Because here, the wishes do come true.\nYour friends find it hilarious. They coax you into making a wish to see if it would come true. Pick your choice:"
    Label(root,text=t3).grid(row=0,column=0,sticky=W)
    t4="\nA. As a joke, you wish to become a billionaire.\nB. Your heart suddenly makes a strong desire. Your mother had passed away when you were a child. You miss her terribly and you wish for her return."
    Label(root,text=t4).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A2).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B2).grid(row=4, column=0)

def B1():
    resetwindow()
    t="Uh Oh! Looks like you are not very adventurous. But it's okay! We hope you enjoyed the rest of your evening in your camps.\nGoodbye!"
    Label(root, text=t).grid(row=0,column=0)
    Button(root, text="Exit", command=root.quit).pack()

def intro():
    resetwindow()
    t1="You decide to camp out with your friends outside a very old and deserted village.\nIt is all fun and games until you guys decide to explore the area.\nIt is only 6:00 pm but the clouds are getting darker by the minute.\nYou come across a poorly maintained structure.\nYou and your friends find the place very mysterious.\nSo you look up the place on Google to find out that it used to be a very famous temple but with a paranormal history.\nWhat will you do next?"
    Label(root,text=t1).grid(row=0,column=0,sticky=W)
    t2="\n\nA. You decide that there is nothing better than an adventure with your friends in a mysterious temple.\nYou climb over the giant, heavy gates and sneak into the temple property.\n\nB. You think that it's too risky to go in. So you decide to head back to your camps and spend the rest of your evening there."
    Label(root,text=t2).grid(row=2,column=0,sticky=W)
    Button(root, text="A", width=20,command=A1).grid(row=3, column=0)
    Button(root, text="B", width=20,command=B1).grid(row=4, column=0)


def firstclick():
    text = e.get()
    e.delete(0,END)
    resetwindow()
    Label(root, text='Welcome '+text+'! We hope youre up for some adventure! lets begin!').grid(row=4, column=0,sticky=W)
    Button(root,text="Continue",width=20,command=intro).grid(row=5,column=0)



Label(root,text="Welcome! Enter your name:",bg="black",fg="white", font = "none 14 bold").grid(row =1, column=0, sticky=W)

e = Entry(root, width = 45, borderwidth=4)
e.grid(row=2, column=0, sticky=W)
Button(root, text="Click to Continue", width=17, command=firstclick).grid(row=4, column=0, sticky=W)

root.mainloop()
