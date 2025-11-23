import os
from datetime import date
FILE = "habitprogress.txt"
def load():
    d = {}
    if not os.path.exists(FILE):
        return d
    with open(FILE) as f:
        lines = [x.strip() for x in f if x.strip()]
    i = 0
    while i < len(lines):
        name = lines[i]
        typ = lines[i+1]
        streak = int(lines[i+2])
        total = int(lines[i+3])
        last = lines[i+4]
        start = lines[i+5]
        lastdate = None
        if last:
            y,m,d = map(int,last.split("-"))
            lastdate = date(y,m,d)
        d[name] = {"type":typ,"streak":streak,"total":total,"last":lastdate,"start":start}
        i += 6
    return d
def save(d):
    with open(FILE,"w") as f:
        for name in d:
            h = d[name]
            last = ""
            if h["last"]:
                last = h["last"].strftime("%Y-%m-%d")
            f.write(name+"\n")
            f.write(h["type"]+"\n")
            f.write(str(h["streak"])+"\n")
            f.write(str(h["total"])+"\n")
            f.write(last+"\n")
            f.write(h["start"]+"\n")
def main():
    print("Habit Tracker")
    print("="*40)
    habits = load()
    today = date.today()
    while 1:
        print()
        if habits:
            for i,name in enumerate(habits,1):
                h = habits[name]
                kind = "Good" if h["type"]=="good" else "Bad "
                print(i,name,"(",kind,") Streak:",h["streak"],"Total:",h["total"])
        else:
            print("No habits yet")
        print()
        print("1 Add habit")
        print("2 Log today")
        print("q Quit")
        c = input("Choice: ").lower()
        if c=="q":
            save(habits)
            print("Saved")
            break
        if c=="1":
            name = input("Name fo the habit: ").strip()
            if name in habits:
                print("Already exists")
                continue
            while 1:
                t = input("good or bad: ").lower()
                if t in ["good","bad"]:
                    break
            habits[name] = {"type":t,"streak":0,"total":0,"last":None,"start":today.strftime("%Y-%m-%d")}
            print("Added")
        if c=="2":
            if not habits:
                print("Add habit first")
                continue
            for i,name in enumerate(habits,1):
                print(i,name)
            try:
                n = int(input("Number: "))-1
                name = list(habits.keys())[n]
            except:
                print("Bad number")
                continue
            h = habits[name]
            last = h["last"]
            same = last==today
            if same:
                if input("Already logged today, log again? y/n: ").lower()!="y":
                    continue

            if h["type"]=="good":
                q = "Did you DO "+name+" today? y/n: "
            else:
                q = "Did you AVOID "+name+" today? y/n: "
            a = input(q).lower()
            if a=="y":
                streak = h["streak"]+1 if (last and (today-last).days==1) or not last else 1
                total = h["total"]+1
                if h["type"]=="good":
                    print("Good")
                else:
                    print("Nice resist")
            elif a=="n":
                streak = 0
                total = h["total"]
                if h["type"]=="good":
                    print("Tomorrow")
                else:
                    print("Try again")
            else:
                print("y or n only")
                continue
            h["streak"] = streak
            h["total"] = total
            h["last"] = today
            print("Streak now:",streak)
            if streak>=21: print("21 days!")
            if streak>=66: print("66 days!")
    save(habits)
main()