# **Приложение для контроля финансов**

Данное *приложение* было создано в рамках курсовой работы (ознакомиться с поставленной задачей можно в файле Курсовая Скворцов А.А.docx). Первоначально проект был создан с использованием *фреймворка PySide6*, но в дальнейшем перенесен на *фреймворк PyQt5* с целью проверки кроссплатформенности последнего.

Основной функционал:
+ Регистрация и авторизация пользователей
+ Учет доходов и расходов
+ Формирование отчётности за заданный период по доходам и расходам в виде диаграммы

Для работы с данными использована встроенная в Python библиотека *Sqlite3*.

## **Авторизация**
![](https://github.com/AlexSkvorz/FinanceProject/blob/main/ScreensForREADME/Авторизация_Ошибка.png)

Чтобы начать работу с приложением необходимо авторизоваться. Для этого необходимо создать аккаунт/войти в него. При входе осуществляется проверка существования пользователя с введеными данными с помощью sql-запроса. В случае ошибки предусмотрено поле, которое проифнормирует пользователя о том, что такого пользователя/пароля не существует. 

В этом же окне есть кнопки регистрации и восставновления пароля, при нажатии на которые откроются соответствующие окна. 