import os

class BinTreeElementType:
    def __init__(self, code, recNo):
        self.code = code
        self.recNo = recNo

class BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def CreateBST():
    return None

def BSTEmpty(Root):
    return Root is None

def RecBSTInsert(Root, Item):
    if Root is None:
        return BinTreeNode(Item)
    else:
        if Item.code < Root.data.code:
            Root.left = RecBSTInsert(Root.left, Item)
        elif Item.code > Root.data.code:
            Root.right = RecBSTInsert(Root.right, Item)
        return Root

def RecBSTSearch(Root, KeyValue):
    if Root is None:
        return None
    if KeyValue.code < Root.data.code:
        return RecBSTSearch(Root.left, KeyValue)
    elif KeyValue.code > Root.data.code:
        return RecBSTSearch(Root.right, KeyValue)
    else:
        return Root

def RecBSTInorder(Root, records):
    if Root is not None:
        RecBSTInorder(Root.left, records)
        PrintStudent(records[Root.data.recNo])  
        RecBSTInorder(Root.right, records)

def menu():
    print("\n                  MENU                  \n")
    print("-------------------------------------------------")
    print("1. Insert new student")
    print("2. Search for a student")
    print("3. Print all students (Traverse Inorder)")
    print("4. Print students with a >= given grade")
    print("5. Quit")
    choice = int(input("Choice: "))
    return choice

def BuildBST():
    if not os.path.exists("students_Sample.dat"):
        print("Can't open students_Sample.dat")
        return None, 0
    with open("students_Sample.dat", "r") as fp:
        records = fp.readlines()
        Root = CreateBST()
        size = 0
        for line in records:
            student_info = line.strip().split(", ")
            if len(student_info) == 6:
                code = int(student_info[0])
                indexRec = BinTreeElementType(code, size)
                Root = RecBSTInsert(Root, indexRec)
                size += 1
    return Root, size, records

def PrintStudent(record):
    print(record.strip())

def printStudentsWithGrade(records):
    theGrade = float(input("Give the grade: "))
    for record in records:
        student_info = record.strip().split(", ")
        if len(student_info) == 6:
            grade = float(student_info[5])
            if grade >= theGrade:
                PrintStudent(record)

def main():
    Root, size, records = BuildBST()
    while True:
        choice = menu()
        if choice == 1:
            with open("students_Sample.dat", "a") as fp:
                student_code = int(input("Give student's AM: "))
                while student_code < 0:
                    print("Code can't be a negative number")
                    student_code = int(input("Give student's AM: "))
                
                indexRec = BinTreeElementType(student_code, size)
                if RecBSTSearch(Root, indexRec) is None:
                    surname = input("Give student name: ")
                    name = input("Give student surname: ")
                    year = int(input("Give student's registration year: "))
                    grade = float(input("Give student's grade(0-20): "))
                    while grade < 0 or grade > 20:
                        grade = float(input("Give student's grade(0-20): "))
                    sex = input("Give student sex F/M: ").upper()
                    while sex not in ['F', 'M']:
                        sex = input("Give student sex F/M: ").upper()
                    
                    record = f"{student_code}, {name}, {surname}, {sex}, {year}, {grade}\n"
                    fp.write(record)
                    records.append(record)
                    size += 1
                    Root = RecBSTInsert(Root, indexRec)
                else:
                    print("A student with the same code is already in the tree")
        
        elif choice == 2:
            student_code = int(input("Give student's code: "))
            indexRec = BinTreeElementType(student_code, 0)
            result = RecBSTSearch(Root, indexRec)
            if result is not None:
                PrintStudent(records[result.data.recNo])
            else:
                print("There is no student with this code")

        elif choice == 3:
            print("Printing all students:")
            RecBSTInorder(Root, records)  
            print()

        elif choice == 4:
            print("Print students with a >= given grade:")
            printStudentsWithGrade(records)

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
