import random
print("Welcome in UBER app  🚗🚗 ")

word1=["Agra","Aligarh","Allahabad","AmbedkarNagar","Amethi","Amroha","Auraiya","Azamgarh","Auraiya","Bahraich","Ballia","Balrampur","Banda","Barabanki","Bareilly","Bijnor","Mahoba","Kanpur","Jhansi"]
word2=random.choice(word1)
print("Rider1 👳🏻‍♂️:",word2)
word3=["Agra","Aligarh","Allahabad","AmbedkarNagar","Amethi","Amroha","Auraiya","Azamgarh","Auraiya","Bahraich","Ballia","Balrampur","Banda","Barabanki","Bareilly","Bijnor","Mahoba","Kanpur","Jhansi"]
word4=random.choice(word3)
print("Rider2 👳🏻‍♂️:",word4)
word5=["Agra","Aligarh","Allahabad","AmbedkarNagar","Amethi","Amroha","Auraiya","Azamgarh","Auraiya","Bahraich","Ballia","Balrampur","Banda","Barabanki","Bareilly","Bijnor","Mahoba","Kanpur","Jhansi"]
word6=random.choice(word5)
print("Rider3 👳🏻‍♂️:",word6)
sum2=0
round5=0

about=input("Do you want to know about of Riders:")
if about=="yes":
    print("Note:1.If you want to know about only one rider so enter rider1 or rider2 or rider3")
    print("     2.If you want to know about all riders so Enter all")
    which=input("Which rider about you want to know:")
    if which=="rider1":
        print("Rider1 name: Vinod Kumar")
        print("       age:32 years")
        print("       Mobile no:9878675645")
        print("       Address: Sitapur")
        print("       Aadhar number: 2220 7914 1926")
        print("       Email ID: vinodkumar2020@uber.org")
    if which=="rider2":
        print("Rider2 name: Anil Chaurasiya")
        print("       age:35 years")
        print("       Mobile no:8978675645")
        print("       Address: Lakhimpur")
        print("       Aadhar number: 3456 7914 1926")
        print("       Email ID: anilchaurasiya2020@uber.org")
    if which=="rider3":
        print("Rider1 name: Manjunath")
        print("       age:42 years")
        print("       Mobile no:7654775645")
        print("       Address: Sarjapur")
        print("       Aadhar number: 8796 7914 1926")
        print("       Email ID: manjulnath2020@uber.org")
    if which=="all":
        print("Rider1 name: Vinod Kumar")
        print("       age:32 years")
        print("       Mobile no:9878675645")
        print("       Address: Sitapur")
        print("       Aadhar number: 2220 7914 1926")
        print("       Email ID: vinodkumar2020@uber.org")

        print("Rider2 name: Anil Chaurasiya")
        print("       age:35 years")
        print("       Mobile no:8978675645")
        print("       Address: Lakhimpur")
        print("       Aadhar number: 3456 7914 1926")
        print("       Email ID: anilchaurasiya2020@uber.org")

        print("Rider1 name: Manjunath")
        print("       age:42 years")
        print("       Mobile no:7654775645")
        print("       Address: Sarjapur")
        print("       Aadhar number: 8796 7914 1926")
        print("       Email ID: manjulnath2020@uber.org")
        print("Ok Continue your process😇😇😇")



else:
    print("Ok Continue your process😇😇😇")


owner=input("Which rider details you want to see:")

def rider():
    global rider
    time=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Nineth","Tenth"]
    round=[2,3,4,5,6]
    round_1=random.choice(round)
    sum=0
    i=0
    km=0
    while i<round_1:

        #print("Rider1:",word2)
        print("Presss 1 for continue: ")
        print("Press 2 for cancel: ")
        want=int(input("Enter a num="))

        if want==1:
            a=("Thank you Sir 🌸😇🌸")
        else:
            b=("Sorry ,You cancelled the process 😒😒")
            return b
    
        distance=[100,31,72,13,14,34,56,76,45,98,23,65,63,76,98,43,44,87]
        distance1=random.choice(distance)
        km=km+distance1
        if owner==owner:
            user=["Rampur","Mishrikh","Manipur","Sidhauli","Sandana","Gopalpur"]
            from_user=random.choice(user)
            user1=["Mahmoodabad","Raypur","ThakurGanj","Gangoy","Aladadpur","Atariya"]
            from_user1=random.choice(user1)

            print("In",time[i],"round",owner,"went from",from_user,"to",from_user1,"🚗🚗🚗🚗🚗🚗")
            print("Total dictance between",from_user,"to",from_user1,"=",distance1,"km 😇😇😇😇😇")
            total=distance1*5
            sum=sum+total
            print("Passenger payed to",owner,"=",total)
        i=i+1
    bonas=km//100
    bonas1=bonas*20
    print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🌴🌴🌴🌴🌴🌴🌳🌳🌳🌳🌳🌳🌳🌴🌴🌴🌴🌴🌴🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄")
    print("Total round by",owner,"in hole day","=",round_1)
    print("Total kilometers which rides by",owner,"in hole day","=",km)
    print("Total money which earned by",owner, "in hole day=","Rs.",sum)
    print("Except salary",owner,"got Bonas=","Rs.",bonas1,"🏆🏆🏆🏆🏆🏆")
    print("🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹")
    owner2=input("Do you want to see how much money others riders earned...")
    if owner2=="yes":
        if owner=="rider1":
            print("Total money which earned by Rider2 in hole day=","Rs.",sum2)
            print("Total money which earned by Rider3 in hole day=","Rs.",sum2)
        elif owner=="rider2":
            print("Total money which earned by Rider1 in hole day=","Rs.",sum2)
            print("Total money which earned by Rider3 in hole day=","Rs.",sum2)
        elif owner=="rider3":
            print("Total money which earned by Rider1 in hole day=","Rs.",sum2)
            print("Total money which earned by Rider2 in hole day=","Rs.",sum2)
    return a
print(rider())
print("🔴🟠🟡🟢🔵🟣⚫🟤⚪🔴🟠🟡🟢🔵🟣⚫⚪🟤🔴🟠🟡🟢🔵🟣⚫⚪🟤🔴🟠🟡🟢🔵🟣⚫⚪🟤🔴🟠🟡")
print("Please rate this app")

print("Note: Press 1 for 1 star")
print("      Press 2 for 2 star")
print("      Press 3 for 3 star")
print("      Press 4 for 4 star")
print("      Press 5 for 5 star")
star=int(input("Enter a num for rateing this app: "))

if star==1:
    print("          🌟")
    print("****Your feedback helps others make better decisions****")
    print("Thank you Sir for sharing your feedback 🌸😇🌸")
if star==2:
    print("          🌟 🌟")
    print("****Your feedback helps others make better decisions****")
    print("Thank you Sir for sharing your feedback 🌸😇🌸")
if star==3:
    print("          🌟 🌟 🌟")
    print("****Your feedback helps others make better decisions****")
    print("Thank you Sir for sharing your feedback 🌸😇🌸")
if star==4:
    print("          🌟 🌟 🌟 🌟")
    print("****Your feedback helps others make better decisions****")
    print("Thank you Sir for sharing your feedback 🌸😇🌸")
if star==5:
    print("          🌟 🌟 🌟 🌟 🌟")
    print("****Your feedback helps others make better decisions****")
    print("Thank you Sir for sharing your feedback 🌸😇🌸")
else:
    pass