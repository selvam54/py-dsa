class student:
    
    def __init__(self,name,mark,classes,age):
        self.name=name
        self.mark=mark
        self.classes=classes
        self.age=age
        
    def answer(self):
        print("the student age is :",self.name)
        print("student mark :",self.mark)
        print("student classes :",self.classes)
        print("student age :",self.age)
        
students=student("selvam",220,"bsc it",20)
students.answer()
