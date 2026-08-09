from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
app=FastAPI()
students=[]
class Student(BaseModel):
    name: str
    year: int
    branch:str
    cgpa:float
@app.post('/student')
def register(student:Student):
    students.append(student)
    return {'message': 'student registered successfully'}
@app.get('/student')
def info():
    return students
@app.get('/student/{index}')

def getinfo(index:int):
    if index>=0 and index<=len(students)-1:
        return students[index]
    else:
        raise HTTPException(status_code=404,detail='student not found')
class Updatecgpa(BaseModel):
    cgpa:float

@app.patch('/student/{index}')
def update(index:int,new:Updatecgpa):
    students[index].cgpa=new.cgpa
    return students[index]
@app.delete('/student/{index}')
def dele(index:int):
    students.remove(students[index])
    return students
    


