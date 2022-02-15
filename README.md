Краткое пояснение.

Для выполнения задания я выбрал язык Python с фреймворком Flask. В качестве базы данных я использовал PostgreSQL.

Реализовал RESTful API с двумя GET-запросами. 
Один возвращает информацию о пользователе по номеру договора, другой - баланс пользователя с указанным договором, на указанную дату.

Большее затруднение вызвал поиск баланса. Мои размышления были следующими:

Мы знаем когда и какой тариф был подключен клиенту. 
Предположим, что фиксированная сумма списывается ежемесячно.
В случае недостатка средств - баланс уходит в минус (насколько я помню, у вас оно работает именно так).
Таким образом, мы можем просчитать сумму, которая была списана у пользователя за использование услуг.
Также имеется таблица, в которой указаны зачисления средств на счет. 
Находим сумму зачислений за нужный промежуток времени и вычитаем списанную сумму за использование услуг за тот же промежуток времени.
Получаем нужный нам результат.

При реализации мог где-то ошибиться, потому решил описать ход своих мыслей. 
При проверке с фиктивными договорами результат был похож на правду.

По фронтенду:

Flask имеет встроенный шаблонизатор, однако использовать я его не стал, т.к. суть задания в работе с API.
Всю логику фронта писал на JS, отправлял запрос через fetch, далее полученные данные выводил на страницу.