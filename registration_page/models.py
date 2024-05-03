from project.settings import DB

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(30), nullable = False)
    email = DB.Column(DB.String(70), nullable = False)
    password = DB.Column(DB.String(30), nullable = False)

    def __repr__(self):
      return f"id користувача - {self.id}; Ім'я користувача - {self.name}; Email користувача {self.email}; Пароль користувача {self.email}"