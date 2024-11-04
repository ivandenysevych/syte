from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template_string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

# Определение модели пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Создание всех таблиц перед первым запуском
with app.app_context():
    db.create_all()

# Главная страница с HTML-шаблоном
@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>4х4</title>
    <style>
        body {
            background-color: #6d8f78;
            font-family: Arial, sans-serif;
            color: #fff;
            padding: 20px;
        }
        h3 {
            color: #f0f0f0;
        }
        button a {
            color: #fff;
            text-decoration: none;
        }
        form {
            margin: 20px 0;
        }
        input {
            margin: 5px 0;
            padding: 10px;
            width: 100%;
        }
    </style>
</head>

<body>
    <p>Запчастини до квадроциклів.</p>
    <a href="https://www.google.com" target="_blank">Перейти на Google</a>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy4WRKpNK5eDZTjASKd3DowCorFDSMwMor3g&s" alt="авто" width="300">

    <button><a href="https://www.olx.ua/d/uk/obyavlenie/kavovarka-franke-spectra-fm-IDUvEbm.html?reason=seller_profile" target="_blank">Кавоварка</a></button>

    <h3>Запчастини</h3>
    <ol>
        <li><a href="https://www.olx.ua/d/uk/obyavlenie/honda-trx-350-500-schtki-startera-dlya-kvadrotsikla-IDOrIFH.html" target="_blank">Щітки квадроцикла</a></li>
        <li><a href="https://www.olx.ua/d/uk/obyavlenie/honda-accord-rezinov-nakladki-na-pedal-galma-scheplennya-dlya-IDT9nHM.html?reason=seller_profile" target="_blank">Накладки на педалі</a></li>
        <li><a href="https://www.olx.ua/d/uk/obyavlenie/tormozn-kolodki-na-kvadrotsikl-honda-trx-500-trx680-IDWX0XY.html?reason=seller_profile" target="_blank">Тормозні колодки</a></li>
        <li>TRX 500 Rubicon</li>
    </ol>
</body>
</html>
    ''')

if __name__ == "__main__":
    app.run()
