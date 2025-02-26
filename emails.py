import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

text = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

text = text.replace("%website%", "https://dvmn.org/profession-ref-program/stepandssss/VDUR4/")
text = text.replace("%friend_name%", "Иван")
text = text.replace("%my_name%", "Степан")
letter = """From: stephan.nn@yandex.ru
To: stephan.nn@yandex.ru
Subject: Попробуй себя в программировании!
Content-Type: text/plain; charset="UTF-8";

{text}""".format(text = text)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
email = "stephan.nn@yandex.ru"
login=os.environ['LOGIN']
password=os.environ['PASSWORD']
server.login(login, password)
server.sendmail(email, email, letter) 