#-------------------------------При открытие бота------------------------------
start = """
Добро пожаловать в админку
"""


rasl_message = """
Введите текст для рассылки
"""


rasl_two_step_message = """
{} юзеров забанили бота
{} не забанило
"""


qiwi_setting = """
Выберите, что вы хотите сделать
"""


add_qiwi_message = """
Отправьте киви кошельки пачкой
<i>номер:токен</i>
"""

add_qiwi_not_valid_two_step_message = """
Невалидный киви

номер: <code>{}</code>
токен: <code>{}</code>
"""


add_qiwi_two_step_message = """
Успешно добавлено {} кошельков.
"""


del_qiwi_message = """
Выберите кошелёк, который нужно удалить.
"""

del_qiwi_two_step_message = """
Киви кошелёк успешно удалён!
"""


del_qiwi_not_data_two_step_message = """
Кошелёк не обнаружен!
Повторите выбор.
"""


delete_wallets = """
Все кошельки успешно удалены.
"""


statistic_message = """
<b>Всего юзеров:</b> {}
<b>Активных юзеров за 24 часа:</b> {}
<b>Баланс киви кошельков:</b> {}
<b>Баланс coinbase:</b> {}
"""
