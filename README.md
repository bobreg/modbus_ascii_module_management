# modbus_ascii_module_management
Программа для управления свч модулями по каналу RS-485 и стандарту modbus ascii.

Програма позволяет управлять и считывать параметры свч модулей для систем радиолокации изготовленные для ПАО НПО Алмаз. Для управления модулями между НПО Алмаз и изготовителями модулей был составлен и утверждён универсальный протокол обмена на основе modbus ascii. В данном протоколе описаны команды запросов и ответов для одноканальных, двухканальных и многоканальных модулей.
На основе данных команд из универсального протокола основана работа данной программы.

Программа написана на языке python и может быть запущена на os windows и с некоторыми условиями на os linux. Для работы программы в компьютере должен быть определён com-порт, настроенный на стандарт rs-485 (например MOXA uPort 1150).

При запуске программа определяет com-порты на компьютере, опрашивает весь диапазон адресов из универсального протокола и определяет наличие в канале модулей и их тип (одноканальный, двухканальный, многоканальный). И затем сохраняет данные в scv файле.
После поиска модулей программа строит окно соответствующее количеству найденых модулей.
