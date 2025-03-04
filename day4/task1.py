import random
def fun(names):
   # for name in sorted(names): 
   #     print(random.randint(1, 21), name)
    d = {name: random.randint(1, 21) for name in names}
    for name in sorted(d.keys(), key=lambda k: k):
        print(d[name], name)
        
names = [
    "Chris Harry K",
    "Siddartha Kommu",
    "Mayank Pathak",
    "Balaji Pappala",
    "Sumanth Kumar Valluru",
    "Japa Harish",
    "Lakshmi Sahithi Vanga",
    "G.VANI",
    "Indukuru Sravani",
    "Sirneni Pavan Sai",
    "Suman Kumar Ghorai",
    "Yugesh Karoti",
    "Chundi Vishnu Priya",
    "Sri Sanjana Indugula",
    "G Santosh Kumar",
    "Gangiredla Karthik",
    "Venkata Naidu Punnana",
    "Pedapalli Suresh",
    "Prathamesh Pahune",
    "Venkata Krishna Kolli",
    "Ram Mishra"
]


fun(names)