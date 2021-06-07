def read_member_name():
    with open('member_name', 'r') as file:
        info_list = (file.read())
        info_list = info_list.split(',,')
        info_list.remove('\n\n')
        return info_list


def read_member_info():
    with open('info', 'r') as file:
        info_list = (file.read())
        info_list = info_list.split(',,')
        return info_list


def find(name):
    family_list = read_member_name()
    for family in family_list:
        particular_mem = family.split(',')
        n = -1
        while True:
            n = n + 1
            try:
                if particular_mem[n] == name:
                    mem_info = read_member_info()
                    for mem in mem_info:
                        mem = mem.split(",")
                        if mem[0] == name:
                            print(
                                f"\nName: {mem[0]}.\nAge: {mem[1]}.\nHeight: {mem[2]}.\nWeight: {mem[3]}.\nGender: {mem[4]}.\nBirth Date: {mem[5]}.\nProfession: {mem[6]}")
                        pass
            except:
                pass


def add():
    family_leader = input("Enter the family head name: ")
    mem_name = input("Enter the name of the member you wanna add: ")
    age = int(input("Enter the age: "))
    height = float(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    gender = str(input("Enter the gender: "))
    birthday = input("Enter the birthdate in dd/mm/yyyy form: ")
    profession = input("Enter the profession")


Choice = (
    """f = Find any member information\na = Add member to a particular family\nr = Remove member from a particular family\nq = Quit\nEnter your choice: """)
choice = str(input(Choice))
while choice != 'q':
    if choice == 'f':
        name = input("Enter the name of the member you want to find: ")
        find(name)
    if choice == 'a':
        add()
