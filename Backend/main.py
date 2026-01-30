from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# Даные для входа администратора

data = {
    "Name": "Admin",
    "Password": "Admin123"
}

# Все модели данных

class Login(BaseModel):
    username: str
    password: str

# Модель для создания поста
class CreatePost(BaseModel):
    heading: str
    title: str
    photo: str

# Модель для редактирования поста   
class EditPost(BaseModel):
    post_id: int
    heading: str
    title: str
    photo: str

# Модель для создания работника
class CreatePerson(BaseModel):
    name: str
    job_title: int
    person_photo: str


# Вход и выход из аккаунта
@app.post("/login",
          tags=["Аккаунты"],
          summary="Вход",)

def login(credentials: Login):
    if (credentials.username == data["Name"] and
            credentials.password == data["Password"]):
        return {"message": "Успешный вход"}
    else:
        return {"message": "Неверные учетные данные"}

@app.post("/logout",
          tags=["Аккаунты"],
          summary="Выход",)
def logout():
    return {"message": "Успешный выход"}

# Создание, редактирование, удаление постов

# Создание поста
@app.post("/post/create_post",
          tags=["Посты"],
          summary="Создание поста",)
def create_post(post: CreatePost):
    return {
        "heading": post.heading,
        "title": post.title,
        "photo": post.photo,
        "message": "Пост успешно создан"
    }

# Редактирование поста
@app.post("/post/edit_posts", 
          tags=["Посты"],
          summary="Редактирование постов",) 
def edit_posts(post: EditPost):
    return {"message": "Пост успешно отредактирован"}

# Получение постов
@app.get("/post/get_posts",
          tags=["Посты"],
          summary="Получение постов",)
def get_posts():
    return {"message": "Получение постов"}

# Удаление поста
@app.delete("/post/delete_post/{post_id}",
             tags=["Посты"],
             summary="Удаление поста",)
def delete_post(post_id: int):
    return {"message": f"Пост с ID {post_id} успешно удален"}

# Создание, редактирование, удаление работников

# Создание работника

@app.post("/person/create_person",
          tags=["Работники"],
          summary="Создание работника",)
def create_person(person: CreatePerson):
    return {
        "name": person.name,
        "job_title": person.job_title,
        "person_photo": person.person_photo,
        "message": "Работник успешно создан"
    }

# Редактирование работника
@app.post("/person/edit_person",
            tags=["Работники"],
            summary="Редактирование работника",)    
def edit_person(person: CreatePerson):
    return {"message": "Работник успешно отредактирован"}

# Получение работников
@app.get("/person/get_persons",
          tags=["Работники"],
          summary="Получение работников",)
def get_persons():
    return {"message": "Получение работников"}  

# Удаление работника
@app.delete("/person/delete_person/{person_id}",
             tags=["Работники"],
             summary="Удаление работника",)
def delete_person(person_id: int):
    return {"message": f"Работник с ID {person_id} успешно удален"}