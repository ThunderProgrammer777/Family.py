def read_member_name():
    with open('member_name', 'r') as file:
        info_list = (file.read())
        info_list = info_list.split(',,')
        try:
            info_list.remove('\n\n')
        except:
            pass
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
        for mem in particular_mem:
            try:
                if mem == name:
                    mem_info = read_member_info()
                    for member in mem_info:
                        mem = member.split(",")
                        if mem[0] == name:
                            print(
                                f"\nName: {mem[0]}.\nAge: {mem[1]}.\nHeight: {mem[2]}.\nWeight: {mem[3]}.\nGender: {mem[4]}.\nBirth Date: {mem[5]}.\nProfession: {mem[6]}\n")
                        pass
            except:
                pass


def add():
    family_leader = input("Enter the family head name: ")
    mem_name = input("Enter the name of the member you wanna add: ")
    families = read_member_name()
    age = int(input("Enter the age: "))
    height = float(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    gender = str(input("Enter the gender: "))
    birthday = input("Enter the birthdate in dd/mm/yyyy form: ")
    profession = input("Enter the profession: ")
    mem_info = read_member_info()
    mem_info.append((f"{mem_name},{age},{height},{weight},{gender},{birthday},{profession}"))
    try:
        mem_info.remove("\n\n")
    except:
        pass
    with open("info", "w")as file:
        file.write(str(",,".join(mem_info)))
    for fam in families:
        fam_list = (str(fam)).split(",")
        for famm in fam_list:
            if famm == family_leader:
                fam_list.append(mem_name)
                families.append(",".join(fam_list))
                families.remove(fam)
                with open("member_name", 'w') as file:
                    file.write(str(",,".join(families)))
                return "Yeah"


Choice = (
    """f = Find any member information\na = Add member to a particular family\nr = Remove member from a particular family\nq = Quit\nEnter your choice: """)
choice = str(input(Choice))
while choice != 'q':
    if choice == 'f':
        name = input("Enter the name of the member you want to find: ")
        find(name)
    if choice == 'a':
        add()
    choice = str(input(Choice))
