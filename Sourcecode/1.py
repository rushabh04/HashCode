import os
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def checkcompletedproj(projects,day):
    for proj in projects:
        if(proj[0].Days <= day - proj[1]):
            ppl = proj[2]
            for i in ppl:
                i[0].flag = True

def free_emply(employe):
    count =0
    for emply in employe:
        if(emply.flag == True): count +=1
    print(count)
##########################################################################################3

class Contributers:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.flag = True           #if True contributer is free and if false busy


class Project:
    def __init__(self, name, D, S, Bd, R, skills):
        self.name = name
        self.Days = D
        self.Score = S
        self.Bd = Bd
        self.Roles = R
        self.skills = skills
############################################################################################3

f = open('../Input/e_exceptional_skills.in.txt')
lines = f.readlines()
line = lines[0]
Con_proj = line.split()
i = 1
Cont = []
for x in range(int(Con_proj[0])):
    skills = {}
    line = lines[i].split()
    name = line[0]
    skil = int(line[1])
    for j in range(int(skil)):
        skill = lines[j+i+1].split()
        skills[skill[0]] = skill[1]
    Cont.append(Contributers(name, skills))
    i = i+skil+1
################################################################################################
Proj = []
for x in range(int(Con_proj[1])):
    try : 
        skills = {}
        line = []
        line = lines[i].split()
        # print(line)
        name = line[0]
        Day = int(line[1])
        Score = int(line[2])
        Bd = int(line[3])
        roles = int(line[4])
        for j in range(int(roles)):
            skill = lines[j+i+1].split()
            skills[skill[0]] = skill[1]
        obj = Project(name, Day, Score, Bd, roles, skills)
        Proj.append(obj)
    except:
        continue
    i = i+roles+1
################################################################################################
prioritydic = []
Priorityproj = []
for obj in Proj:
    Priorityproj.append([obj, obj.Bd])
Prioritydic = Sort(Priorityproj)
###############################################################################################
if os.path.exists("../OutPut/2.txt"):
    os.remove("../OutPut/2.txt")
r = open("../OutPut/2.txt", "a")
##############################################################################################3
count = 0
day = 0
executingproj = []
while len(Prioritydic) != 0 :
    for obj in Prioritydic:
        obj1 = obj[0]
        person = []
        ob1 = obj1.skills
        Roles = obj1.Roles
        for skill in ob1:
            for ob in Cont:
                obj2 = ob.skills
                try:
                    if(int(obj2[skill]) >= int(ob1[skill]) and ob.flag):
                        Roles -=1
                        ob.flag = False
                        person.append([ob,skill])
                        obj2[skill] = str(int(obj2[skill]) + 1)
                        break
                except:
                    continue
        if(Roles == 0):
            r.write(obj1.name)
            r.write("\n")
            # print(obj1.name)
            executingproj.append([obj1,day,person])
            Prioritydic.remove(obj)
            temp =""
            for x in person:
                temp+=x[0].name+" "
            # print(temp)
            r.write(temp)
            r.write("\n")
            count +=1
            print(count)
        else :
            for x in person:
                x[0].skills[x[1]] = str(int(x[0].skills[x[1]])-1)
                x[0].flag = True
    checkcompletedproj(executingproj,day)
    # free_emply(Cont)
    print("###########   ",day,"    ##########")
    day+=50000


f.close()
