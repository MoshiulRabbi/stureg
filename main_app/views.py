from django.shortcuts import render
from django.http import HttpResponse
import json


def home_view(request):
    return render(request, "home.html")


def show_info(request):
    return render(request, "add_reg.html")


def search_info(request):
    return render(request,"search_info.html")

def about_us(request):
    return render(request,"about_us.html")



def search_by_id(request):
    def read_file():
        try:
            with open("info.json", "r") as project_json:
                file = project_json.read()
                info_list = json.loads(file)
                project_json.close()
                return info_list

        except:
            return []

    
    ID = request.GET["id"]
    file = read_file()
    id_list = []
    for item in file:
        id_list.append(item["ID"])
    if ID in id_list:
        for item in file:
            if item["ID"] == ID:
                msg=item
    else:
        msg="Student not Registered or Invalid ID."
    return render(request,"single_info.html",{"info":msg,"id_list":id_list,"id":ID})


def show_all_student(request):
    def read_file():
        try:
            with open("info.json", "r") as project_json:
                file = project_json.read()
                info_list = json.loads(file)
                project_json.close()
                return info_list

        except:
            return []

    all_student=read_file()
    num_of_students=len(all_student)


    return render(request,"show_all_student.html",{"all_student":all_student,"num_of_students":num_of_students})



def student_info(request):

    if request.method == "POST":


        def read_file():
            try:
                with open("info.json", "r") as project_json:
                    file = project_json.read()
                    info_list = json.loads(file)
                    project_json.close()
                    return info_list

            except:
                return []


        def write_file(array):
            with open("info.json", "w+") as project_json:
                content = json.dumps(array, indent=4)
                project_json.writelines(content)
                project_json.close()


        file = read_file()
        id_list = []
        for item in file:
            id_list.append(item["ID"])

        name = request.POST["name"]   
        ID = request.POST["id"] 
        section = request.POST["section"]
        dep=request.POST["department"]
        payment=request.POST["payment"]

        info_dic = {
            "Name": name,
            "ID": ID,
            "Section": section,
            "Department":dep,
            "Payment_Status":payment,
        }
        if ID in id_list:
            msg="ID already Registered !"
        else:
            if name=="" or ID=="" or section=="":
                msg="Please Enter Name, ID and Section"
            else:
                student_info = read_file()
                student_info.append(info_dic)
                write_file(student_info)

                msg = "Registration Complete !! "
        return render(request, "add_reg.html", {"msg": msg})
    else:
        return render(request, "add_reg.html")

                


def del_registration(request):
    
    return render(request,"del_registration.html")

def del_reg_main(request):
    def read_file():
        try:
            with open("info.json", "r") as project_json:
                file = project_json.read()
                info_list = json.loads(file)
                project_json.close()
                return info_list

        except:
            return []

    def write_file(array):
        with open("info.json", "w+") as project_json:
            content = json.dumps(array, indent=4)
            project_json.writelines(content)
            project_json.close()

    ID=request.GET["id"]
    my_file=read_file()
    id_list=[]
    new_data=[]

    for item in my_file:
        id_list.append(item["ID"])
    
    if ID== "":
        msg="Please Enter an ID!!"
    else:
    
        if ID not in id_list:
            msg="ID Not Registered"
        else:
            
            for item in my_file:
                if item["ID"] == ID:
                    deleted=item
                    continue
                else:
                    new_data.append(item)
            write_file(new_data)
            msg="Information Deleted Successfully !!"
        
    return render(request,"del_reg_main.html",{"msg":msg})
