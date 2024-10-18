

class PhoneBook:
    def __init__(self):
        self.phone = {}

    def Num_insert(self):
        name = input("이름 입력: ")
        phoneNumber = input("전화번호 입력(xxx-xxxx-xxxx): ")
        self.phone[name] = phoneNumber

    def View_Num(self):
        name = input("조회할 이름 입력: ")
        if name not in self.phone:
            print("존재하지 않는 이름입니다.")
            return
        print(self.phone[name])

    def Delete_Num(self):
        name = input("삭제할 이름 입력: ")
        if name:
            del self.phone[name]

    def Update_Num(self):
        name = input("전화번호를 수정할 이름 입력: ")
        if name:
            phoneNumber = input("전화번호 입력(xxx-xxxx-xxxx): ")
            self.phone[name] = phoneNumber

    def View_All(self):
        for name, phoneNumber in self.phone.items():
            print(f"{name}: {phoneNumber}")


def load_phonebook(file):
    for line in file:
        name, phoneNumber = line.strip().split()
        Sample1.phone[name] = phoneNumber

def save_phonebook(file):
    file.seek(0)
    file.truncate()
    for name, phone in Sample1.phone.items():
        file.write(f"{name} {phone}\n")

Sample1 = PhoneBook()

with open("Phon.txt", "r+", encoding='UTF8') as file:
    load_phonebook(file)
    
    while True:
        sel = input("1. 전화번호 추가 2. 전화번호 조회 3. 전화번호 삭제 4. 전화번호 수정 5. 저장 안하고 종료 6. 전체 조회 7. 저장 (취소하려면 엔터): ")
        
        if sel == "1":
            Sample1.Num_insert()
        elif sel == "2":
            Sample1.View_Num()
        elif sel == "3":
            Sample1.Delete_Num()
        elif sel == "4":
            Sample1.Update_Num()
        elif sel == "5":
            break
        elif sel == "6":
            Sample1.View_All()
        elif sel == "7":
            save_phonebook(file)
            break
        print("-----------------------------------\n")


