class studentform:
    def __init__(self,name,age,classes):
        self.name=name
        self.age=age
        self.classes=classes
        
    def stpass(self):
        print("student are pass all subject")
        

student1=studentform("selvam",20,"bsc it")
student2=studentform("vamsel",21,"bca")
student1.stpass()

print(student1.name)
print(student1.age)
print(student1.classes)


print(student2.name)
print(student2.age)
print(student2.classes)

