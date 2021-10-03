from django.shortcuts import render

def index(request):
    dept=['MECHANICAL🔥','CIVIL🏗️','AUTOMOBILE🏎️','EEE💡','CSE🖥️','ECE🔌','IT💻','PRODUCTION⚙️','B.ARCH🌉','FOOD TECH🍱','CHEMICAL🧪']
    name=['mech','civil','am','eee','cse','ece','it','pro','btech','food','chem']
    mylist=zip(dept,name)
    context={'mylist':mylist}
    return render (request,'index.html',context)
    
def mech(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['mech1','mech2','mech3','mech4','mech5','mech6','mech7','mech8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def mech1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def result(request):
    sem1=float(request.GET['v1'])
    ans=sem1
    context={'ans':ans}
    return render(request,'result.html',context)

def mech2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def result2(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    ans=(sem1+sem2)/2
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def mech3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html','https://mohan040102.github.io/b/mech_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def result3(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    sem3=float(request.GET['v3'])
    ans=(sem1+sem2+sem3)/3
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def mech4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html','https://mohan040102.github.io/b/mech_3.html','https://mohan040102.github.io/b/mech_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def result4(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    sem3=float(request.GET['v3'])
    sem4=float(request.GET['v4'])
    ans=(sem1+sem2+sem3+sem4)/4
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def mech5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html','https://mohan040102.github.io/b/mech_3.html','https://mohan040102.github.io/b/mech_4.html','https://mohan040102.github.io/b/mech_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def result5(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    sem3=float(request.GET['v3'])
    sem4=float(request.GET['v4'])
    sem5=float(request.GET['v5'])
    ans=(sem1+sem2+sem3+sem4+sem5)/5
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def mech6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html','https://mohan040102.github.io/b/mech_3.html','https://mohan040102.github.io/b/mech_4.html','https://mohan040102.github.io/b/mech_5.html','https://mohan040102.github.io/b/mech_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def result6(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    sem3=float(request.GET['v3'])
    sem4=float(request.GET['v4'])
    sem5=float(request.GET['v5'])
    sem6=float(request.GET['v6'])
    ans=(sem1+sem2+sem3+sem4+sem5+sem6)/6
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def mech7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html','https://mohan040102.github.io/b/mech_3.html','https://mohan040102.github.io/b/mech_4.html','https://mohan040102.github.io/b/mech_5.html','https://mohan040102.github.io/b/mech_6.html','https://mohan040102.github.io/b/mech_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def result7(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    sem3=float(request.GET['v3'])
    sem4=float(request.GET['v4'])
    sem5=float(request.GET['v5'])
    sem6=float(request.GET['v6'])
    sem7=float(request.GET['v7'])
    ans=(sem1+sem2+sem3+sem4+sem5+sem6+sem7)/7
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def mech8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/mech_2.html','https://mohan040102.github.io/b/mech_3.html','https://mohan040102.github.io/b/mech_4.html','https://mohan040102.github.io/b/mech_5.html','https://mohan040102.github.io/b/mech_6.html','https://mohan040102.github.io/b/mech_7.html','https://mohan040102.github.io/b/mech_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def result8(request):
    sem1=float(request.GET['v1'])
    sem2=float(request.GET['v2'])
    sem3=float(request.GET['v3'])
    sem4=float(request.GET['v4'])
    sem5=float(request.GET['v5'])
    sem6=float(request.GET['v6'])
    sem7=float(request.GET['v7'])
    sem8=float(request.GET['v8'])
    ans=(sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8
    context={'ans':round(float(ans), 2)}
    return render(request,'result.html',context)

def civil(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['civil1','civil2','civil3','civil4','civil5','civil6','civil7','civil8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def civil1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def civil2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def civil3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html','https://mohan040102.github.io/b/civil_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def civil4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html','https://mohan040102.github.io/b/civil_3.html','https://mohan040102.github.io/b/civil_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def civil5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html','https://mohan040102.github.io/b/civil_3.html','https://mohan040102.github.io/b/civil_4.html','https://mohan040102.github.io/b/civil_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def civil6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html','https://mohan040102.github.io/b/civil_3.html','https://mohan040102.github.io/b/civil_4.html','https://mohan040102.github.io/b/civil_5.html','https://mohan040102.github.io/b/civil_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def civil7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7 th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html','https://mohan040102.github.io/b/civil_3.html','https://mohan040102.github.io/b/civil_4.html','https://mohan040102.github.io/b/civil_5.html','https://mohan040102.github.io/b/civil_6.html','https://mohan040102.github.io/b/civil_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def civil8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7 th Sem GPA','Enter the 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/civil_2.html','https://mohan040102.github.io/b/civil_3.html','https://mohan040102.github.io/b/civil_4.html','https://mohan040102.github.io/b/civil_5.html','https://mohan040102.github.io/b/civil_6.html','https://mohan040102.github.io/b/civil_7.html','https://mohan040102.github.io/b/civil_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def am(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['am1','am2','am3','am4','am5','am6','am7','am8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def am1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def am2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html',]
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def am3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html','https://mohan040102.github.io/b/ae_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def am4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html','https://mohan040102.github.io/b/ae_3.html','https://mohan040102.github.io/b/ae_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def am5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html','https://mohan040102.github.io/b/ae_3.html','https://mohan040102.github.io/b/ae_4.html','https://mohan040102.github.io/b/ae_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def am6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html','https://mohan040102.github.io/b/ae_3.html','https://mohan040102.github.io/b/ae_4.html','https://mohan040102.github.io/b/ae_5.html','https://mohan040102.github.io/b/ae_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def am7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html','https://mohan040102.github.io/b/ae_3.html','https://mohan040102.github.io/b/ae_4.html','https://mohan040102.github.io/b/ae_5.html','https://mohan040102.github.io/b/ae_6.html','https://mohan040102.github.io/b/ae_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def am8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ae_2.html','https://mohan040102.github.io/b/ae_3.html','https://mohan040102.github.io/b/ae_4.html','https://mohan040102.github.io/b/ae_5.html','https://mohan040102.github.io/b/ae_6.html','https://mohan040102.github.io/b/ae_7.html','https://mohan040102.github.io/b/ae_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def eee(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['eee1','eee2','eee3','eee4','eee5','eee6','eee7','eee8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def eee1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def eee2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)  

def eee3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html','https://mohan040102.github.io/b/eee_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)  

def eee4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html','https://mohan040102.github.io/b/eee_3.html','https://mohan040102.github.io/b/eee_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)  

def eee5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html','https://mohan040102.github.io/b/eee_3.html','https://mohan040102.github.io/b/eee_4.html','https://mohan040102.github.io/b/eee_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context) 

def eee6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html','https://mohan040102.github.io/b/eee_3.html','https://mohan040102.github.io/b/eee_4.html','https://mohan040102.github.io/b/eee_5.html','https://mohan040102.github.io/b/eee_6.html',]
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context) 

def eee7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html','https://mohan040102.github.io/b/eee_3.html','https://mohan040102.github.io/b/eee_4.html','https://mohan040102.github.io/b/eee_5.html','https://mohan040102.github.io/b/eee_6.html','https://mohan040102.github.io/b/eee_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context) 

def eee8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/eee_2.html','https://mohan040102.github.io/b/eee_3.html','https://mohan040102.github.io/b/eee_4.html','https://mohan040102.github.io/b/eee_5.html','https://mohan040102.github.io/b/eee_6.html','https://mohan040102.github.io/b/eee_7.html','https://mohan040102.github.io/b/eee_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context) 

def cse(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['cse1','cse2','cse3','cse4','cse5','cse6','cse7','cse8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def cse1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def cse2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def cse3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html','https://mohan040102.github.io/b/3rd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def cse4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html','https://mohan040102.github.io/b/3rd_Sem.html','https://mohan040102.github.io/b/4th_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def cse5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html','https://mohan040102.github.io/b/3rd_Sem.html','https://mohan040102.github.io/b/4th_Sem.html','https://mohan040102.github.io/b/5th-Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def cse6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html','https://mohan040102.github.io/b/3rd_Sem.html','https://mohan040102.github.io/b/4th_Sem.html','https://mohan040102.github.io/b/5th-Sem.html','https://mohan040102.github.io/b/6th_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def cse7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html','https://mohan040102.github.io/b/3rd_Sem.html','https://mohan040102.github.io/b/4th_Sem.html','https://mohan040102.github.io/b/5th-Sem.html','https://mohan040102.github.io/b/6th_Sem.html','https://mohan040102.github.io/b/7th_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def cse8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/1st_Sem.html','https://mohan040102.github.io/b/3rd_Sem.html','https://mohan040102.github.io/b/4th_Sem.html','https://mohan040102.github.io/b/5th-Sem.html','https://mohan040102.github.io/b/6th_Sem.html','https://mohan040102.github.io/b/7th_Sem.html','https://mohan040102.github.io/b/8th-Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def ece(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['ece1','ece2','ece3','ece4','ece5','ece6','ece7','ece8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def ece1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def ece2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)  

def ece3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html','https://mohan040102.github.io/b/ece_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def ece4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html','https://mohan040102.github.io/b/ece_3.html','https://mohan040102.github.io/b/ece_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def ece5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html','https://mohan040102.github.io/b/ece_3.html','https://mohan040102.github.io/b/ece_4.html','https://mohan040102.github.io/b/ece_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def ece6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA',"Enter 6th Sem GPA"]
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html','https://mohan040102.github.io/b/ece_3.html','https://mohan040102.github.io/b/ece_4.html','https://mohan040102.github.io/b/ece_5.html','https://mohan040102.github.io/b/ece_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def ece7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA',"Enter 6th Sem GPA",'Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html','https://mohan040102.github.io/b/ece_3.html','https://mohan040102.github.io/b/ece_4.html','https://mohan040102.github.io/b/ece_5.html','https://mohan040102.github.io/b/ece_6.html','https://mohan040102.github.io/b/ece_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def ece8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA',"Enter 6th Sem GPA",'Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/ece_2.html','https://mohan040102.github.io/b/ece_3.html','https://mohan040102.github.io/b/ece_4.html','https://mohan040102.github.io/b/ece_5.html','https://mohan040102.github.io/b/ece_6.html','https://mohan040102.github.io/b/ece_7.html','https://mohan040102.github.io/b/ece_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def it(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['it1','it2','it3','it4','it5','it6','it7','it8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def it1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def it2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def it3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html','https://mohan040102.github.io/b/it_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def it4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html','https://mohan040102.github.io/b/it_3.html','https://mohan040102.github.io/b/it_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def it5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html','https://mohan040102.github.io/b/it_3.html','https://mohan040102.github.io/b/it_4.html','https://mohan040102.github.io/b/it_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def it6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html','https://mohan040102.github.io/b/it_3.html','https://mohan040102.github.io/b/it_4.html','https://mohan040102.github.io/b/it_5.html','https://mohan040102.github.io/b/it_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def it7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html','https://mohan040102.github.io/b/it_3.html','https://mohan040102.github.io/b/it_4.html','https://mohan040102.github.io/b/it_5.html','https://mohan040102.github.io/b/it_6.html','https://mohan040102.github.io/b/it_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def it8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/it_2.html','https://mohan040102.github.io/b/it_3.html','https://mohan040102.github.io/b/it_4.html','https://mohan040102.github.io/b/it_5.html','https://mohan040102.github.io/b/it_6.html','https://mohan040102.github.io/b/it_7.html','https://mohan040102.github.io/b/it_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def pro(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['pro1','pro2','pro3','pro4','pro5','pro6','pro7','pro8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def pro1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def pro2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def pro3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html','https://mohan040102.github.io/b/pe_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def pro4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html','https://mohan040102.github.io/b/pe_3.html','https://mohan040102.github.io/b/pe_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def pro5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html','https://mohan040102.github.io/b/pe_3.html','https://mohan040102.github.io/b/pe_4.html','https://mohan040102.github.io/b/pe_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def pro6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html','https://mohan040102.github.io/b/pe_3.html','https://mohan040102.github.io/b/pe_4.html','https://mohan040102.github.io/b/pe_5.html','https://mohan040102.github.io/b/pe_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def pro7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html','https://mohan040102.github.io/b/pe_3.html','https://mohan040102.github.io/b/pe_4.html','https://mohan040102.github.io/b/pe_5.html','https://mohan040102.github.io/b/pe_6.html','https://mohan040102.github.io/b/pe_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def pro8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem  GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/pe_2.html','https://mohan040102.github.io/b/pe_3.html','https://mohan040102.github.io/b/pe_4.html','https://mohan040102.github.io/b/pe_5.html','https://mohan040102.github.io/b/pe_6.html','https://mohan040102.github.io/b/pe_7.html','https://mohan040102.github.io/b/pe_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def btech(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['btech1','btech2','btech3','btech4','btech5','btech6','btech7','btech8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def btech1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/arch_1.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def btech2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def btech3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html','https://mohan040102.github.io/b/arch_3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def btech4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html','https://mohan040102.github.io/b/arch_3.html','https://mohan040102.github.io/b/arch_4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def btech5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html','https://mohan040102.github.io/b/arch_3.html','https://mohan040102.github.io/b/arch_4.html','https://mohan040102.github.io/b/arch_5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)


def btech6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html','https://mohan040102.github.io/b/arch_3.html','https://mohan040102.github.io/b/arch_4.html','https://mohan040102.github.io/b/arch_5.html','https://mohan040102.github.io/b/arch_6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def btech7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html','https://mohan040102.github.io/b/arch_3.html','https://mohan040102.github.io/b/arch_4.html','https://mohan040102.github.io/b/arch_5.html','https://mohan040102.github.io/b/arch_6.html','https://mohan040102.github.io/b/arch_7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)


def btech8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/arch_1.html','https://mohan040102.github.io/b/arch_2.html','https://mohan040102.github.io/b/arch_3.html','https://mohan040102.github.io/b/arch_4.html','https://mohan040102.github.io/b/arch_5.html','https://mohan040102.github.io/b/arch_6.html','https://mohan040102.github.io/b/arch_7.html','https://mohan040102.github.io/b/arch_8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def food(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['food1','food2','food3','food4','food5','food6','food7','food8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def food1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def food2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def food3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html','https://mohan040102.github.io/b/food3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def food4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html','https://mohan040102.github.io/b/food3.html','https://mohan040102.github.io/b/food4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def food5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter the 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html','https://mohan040102.github.io/b/food3.html','https://mohan040102.github.io/b/food4.html','https://mohan040102.github.io/b/food5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def food6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter the 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html','https://mohan040102.github.io/b/food3.html','https://mohan040102.github.io/b/food4.html','https://mohan040102.github.io/b/food5.html','https://mohan040102.github.io/b/food6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def food7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter the 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html','https://mohan040102.github.io/b/food3.html','https://mohan040102.github.io/b/food4.html','https://mohan040102.github.io/b/food5.html','https://mohan040102.github.io/b/food6.html','https://mohan040102.github.io/b/food7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def food8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter the 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/food2.html','https://mohan040102.github.io/b/food3.html','https://mohan040102.github.io/b/food4.html','https://mohan040102.github.io/b/food5.html','https://mohan040102.github.io/b/food6.html','https://mohan040102.github.io/b/food7.html','https://mohan040102.github.io/b/food8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

def chem(request):
    sem=['Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8',]
    name=['chem1','chem2','chem3','chem4','chem5','chem6','chem7','chem8']
    mylist=zip(sem,name)
    context={'mylist':mylist}
    return render(request,'mech.html',context)

def chem1(request):
    ques=['Enter 1st Sem GPA']
    name=['v1']
    url=['https://mohan040102.github.io/b/2nd_Sem.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech1.html',context)

def chem2(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA']
    name=['v1','v2']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech2.html',context)

def chem3(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA']
    name=['v1','v2','v3']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html','https://mohan040102.github.io/b/chem3.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech3.html',context)

def chem4(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA']
    name=['v1','v2','v3','v4']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html','https://mohan040102.github.io/b/chem3.html','https://mohan040102.github.io/b/chem4.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech4.html',context)

def chem5(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA']
    name=['v1','v2','v3','v4','v5']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html','https://mohan040102.github.io/b/chem3.html','https://mohan040102.github.io/b/chem4.html','https://mohan040102.github.io/b/chem5.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech5.html',context)

def chem6(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html','https://mohan040102.github.io/b/chem3.html','https://mohan040102.github.io/b/chem4.html','https://mohan040102.github.io/b/chem5.html','https://mohan040102.github.io/b/chem6.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech6.html',context)

def chem7(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html','https://mohan040102.github.io/b/chem3.html','https://mohan040102.github.io/b/chem4.html','https://mohan040102.github.io/b/chem5.html','https://mohan040102.github.io/b/chem6.html','https://mohan040102.github.io/b/chem7.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech7.html',context)

def chem8(request):
    ques=['Enter 1st Sem GPA','Enter 2nd Sem GPA','Enter 3rd Sem GPA','Enter 4th Sem GPA','Enter 5th Sem GPA','Enter 6th Sem GPA','Enter 7th Sem GPA','Enter 8th Sem GPA']
    name=['v1','v2','v3','v4','v5','v6','v7','v8']
    url=['https://mohan040102.github.io/b/2nd_Sem.html','https://mohan040102.github.io/b/chem2.html','https://mohan040102.github.io/b/chem3.html','https://mohan040102.github.io/b/chem4.html','https://mohan040102.github.io/b/chem5.html','https://mohan040102.github.io/b/chem6.html','https://mohan040102.github.io/b/chem7.html','https://mohan040102.github.io/b/chem8.html']
    mylist=zip(ques,name,url)
    context={'mylist':mylist}
    return render(request,'mech8.html',context)

