import json

number = input("Введите номер квалификации: ")
find = False


with open("dump.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == number: 
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")
                code = skill["fields"].get("specialty")
                find = True
            
                for profession in data:
                    if profession.get("model") == "data.specialty":
                        specialty_code = profession["fields"].get("code")
                        if specialty_code in number:
                            specialty_code1 = profession["fields"].get("code")  
                            specialty_title = profession["fields"].get("title")
                            specialty_educational = profession["fields"].get("c_type")
                            
                break  

if not find:
    print("=============== Не Найдено ===============") 
    

else:
    print("=============== Найдено ===============") 
    print(f"{specialty_code1} >> Специальность '{specialty_title}' , {specialty_educational}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")