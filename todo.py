#1번 함수
def add_task(task_name):
    todo_list=list(task_name)
    print(f"할 일 목록에 '{todo_list}'가 추가되었습니다!")
    
    pass

#2번 함수
def view_task():
    
    pass

#3번 함수
def complete_task(task_number):

    pass

#4번 함수
def delete_task(task_number):
    pass


#기능의 메뉴 함수
def show_menu():
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

#메인 & 선택지
def main():
    while True: #while이 있기에 하나의 선택지가 끝나도 계속 입력됨.
        show_menu()
        choice= input("원하는 작업을 선택해주세요.(1번~5번) \n-> ")

        if choice == "1":
            task_name=input("추가할 작업을 입력해주세요.")
            add_task(task_name)
            
        elif choice == "2":
            view_task()

        elif choice == "3": #완료할 목록의 숫자로 입력해주고 
            task_name=int(input("완료를 원하는 작업의 번호를 입력해주세요."))
            complete_task(task_name)

        elif choice == "4":
            task_name=int(input("삭제를 원하는 작업의 번호를 입력해주세요."))
            delete_task(task_name)

        elif choice == "5":
                print("시스템이 종료되었습니다.")
                break
        
        else:
            print("다시 입력해주세요")
            


main()