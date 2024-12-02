import json
import os #파이썬을 이용해 시스템 내부에 접근이 가능하다.


task_file ='tasks.json'

def load_task(): #파일을 불러오기때문에 매개변수는 필요 없음
    if os.path.exists(task_file):
        with open(task_file,'r',encoding='utf-8')as file:
            return json.load(file)
    return [] #아무것도 없으니 리스트를 그냥 만들어버리자/

def save_task(tasks): #add_task를 통해 전달받은 해야할 일을 파일에 저장하는 기능
    with open(task_file,'w',encoding='utf-8')as file: #file => open(TASK_FILE)
        json.dump(tasks,file,indent=4,ensure_ascii=False)

#1번 함수
def add_task(task_name):
    tasks = load_task()
    task={'name':task_name,"completed":False}
    tasks.append(task)
    save_task(tasks)

#2번 함수- 할 일 목록보기
def view_task():
    tasks = load_task() #파일이 있는 경우 안에 내용물이 tasks에 들어가고 없으면 빈 리스트가 들어감
    if not tasks: #tasks는 if문을 만나면 결과는? 
        print("현재 등록된 작업이 없습니다.")
    else:
        print("작업 목록 : ")
        for i, task in enumerate(tasks, start=1): #리스트 안에 리스트또는 딕셔너리
        #enumerate() 내장 함수/ 자동으로 숫자를 증가시켜줌으로써 데이터 값도 넣어줌 가장 앞 변수 ->i=1,task={name:"파이썬 공부하기"---} 
            status ="완료" if task['completed'] else "미완료" #type은 딕셔너리! key 입력 시-> valus 반환해준다.
            print(f"{i}.{task['name']}-{status}") # -> 1. 파이썬 공부하기 - 미완료.
        #if 문이 거짓일 경우 미완료, 참일 경우 완료를 
            
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