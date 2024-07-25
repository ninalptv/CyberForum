from time import sleep
print('Я - самая вежливая программа на свете')
sleep(1)
name = input('Как вас зовут?\n(пользовательский ввод)')
def polite_input(qwstn):
    return input(f"{name}, {qwstn}\n(пользовательский ввод)")

school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')
print("Самая вежливая программа завершила свою работу")


