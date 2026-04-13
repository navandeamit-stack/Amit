# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def say_hacked():
#     return{"dhanraj":"your mobile number:- 9763154785",
#            "dhanraj":"1.25,500rs"
#         }


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def say_mobile_number():
#     return{"amit":"phone number",
#            "01":8767446218,}

# from fastapi import FastAPI # FastAPI = A fast framework to build APIs using Python

# app = FastAPI() #API (Application Programming Interface)

# @app.get("/")
# def say_check():
#     return{"patient":"amit"}


# @app.get("/second")
# def say_checkok():
#     return{"patient":"2 Ajay"}

# @app.get("/third")
# def say_allok():
#     return["everything ok"]

# @app.get("/patient/{name}")
# def get_patient(name: str):
#     return {"patient": name}

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/patient/{name}")
# def get_patient(name:str,age:int,mobile_number:int,DOB:str,diceses:str):
#     return{"name":name,
#            "age":age,
#            "mobile_number":mobile_number,
#            "DOB":DOB,
#            "diceses":"fiver"
#     }

from fastapi import FastAPI
app = FastAPI()

@app.get("/student_admission/{name}")
def get_student(name:str,ssc_markes:str,ssc_hallticket_number:str,mother_name:str):
    return{"name":name,
           "ssc_markes":ssc_markes,
           "ssc_hallticket_number":ssc_hallticket_number,
           "mother_name":mother_name
    }