d1="01.01.2025"
d2="02.01.2025"
d3="03.01.2025"
d4="04.01.2025"
d5="05.01.2025"
d6="06.01.2025"


d7="02.01.2025"
d8="08.01.2025"
d9="09.01.2025"
d10="1.01.2025"

l=[d1,d2,d3,d4,d5,d6]
l2=[d7,d8,d9,d10]


def Buchbar():
    buchbar=0
    for i in l:
        if i in l2:
            buchbar+=1

        else:
            buchbar+=0

    print(buchbar)

        
