from django.db import models


COMPETITORS = (
    ('m', 'Magticom'),
    ('s', 'Silknet'),
    ('o', 'სხვა'),
)
APPLICATION_STATUS = (
    ('new', ' ახალი'),
    ('processed', ' მუშაობაში')
)
CALL_STATUS = (
    ('connected', ' ჩართულია'),
    ('declined', ' უარი თქვა'),
    ('call me later', ' მოგვიანებით დამიკავშირდით'),
    ('didn\'t answer', ' არ მიპასუხა')
)
DECLINED_REASONS = (
    ('not interested', ' არ არის დაინტერესებული'),
    ('no internet', ' არ აქვს ინტერნეტი'),
    ('no device', ' არ აქვს Android/Smart TV'),
    ('too expensive', 'ძვირია')
)
PACKETS = (
    ('1', '1 თვე'),
    ('3', '3 თვე'),
    ('6', '6 თვე'),
)
UNSUBSCRIBE_REASON = (
    ('too expensive', "ძვირია"),
    ('a lot of channels doesn\'t work', "ბევრი არხი არ მუშაობს"),
    ('rewind function ', "გადახვევა არ მუშაობს"),
    ('freezes ', "უჭედავს"),
)


class Application(models.Model):
    name_surname = models.CharField(max_length=50, verbose_name=" სახელი გვარი")
    phone_number = models.CharField(max_length=50, verbose_name=" ტელეფონის ნომერი")
    town = models.CharField(max_length=50, verbose_name=" ქალაქი")
    competitor = models.CharField(max_length=50, choices=COMPETITORS, blank=True, verbose_name=' პროვაიდერი')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=" ანკეტის შემოსვლის დრო")
    updated_at = models.DateTimeField(auto_now=True, verbose_name=' ცვლილება')

    application_status = models.CharField(max_length=50, choices=APPLICATION_STATUS, default='new', verbose_name=' ანკეტის სტატუსი')
    call_status = models.CharField(max_length=50, choices=CALL_STATUS, blank=True, verbose_name=' ზარის სტატუსი')
    declined_reason = models.CharField(max_length=50, choices=DECLINED_REASONS, blank=True, verbose_name=' უარის მიზეზი')
    other_comment = models.TextField(blank=True, verbose_name=' დამატებითი კომენტარი')

    class Meta:
        verbose_name = ' ანკეტა'
        verbose_name_plural = ' ანკეტები'

    def __str__(self):
        return self.name_surname


class Client(models.Model):
    application = models.OneToOneField(Application, on_delete=models.PROTECT, primary_key=True, verbose_name=' ანკეტა')
    email = models.EmailField(unique=True)
    client_password = models.CharField(max_length=50, verbose_name=' პაროლი')
    phone_number = models.CharField(max_length=50, verbose_name=' ტელეფონის ნომერი')
    status = models.BooleanField(default=True, verbose_name=' სტატუსი')
    town = models.CharField(max_length=50, verbose_name=' ქალაქი')
    hosts = models.IntegerField(default=1, verbose_name=' მოწყობილობების რაოდენობა')
    comment = models.TextField(blank=True, verbose_name=' კომენტარი')
    first_payment_date = models.DateField(auto_now_add=True, verbose_name=' პირველი გადახდის თარიღი')
    payed_until = models.DateField(null=True, verbose_name=' მომდევნო გადახდა')
    packets = models.CharField(max_length=50, choices=PACKETS, verbose_name=' პაკეტები')
    packet_plus = models.TextField(blank=True, verbose_name=' დამატები პაკეტი')
    unsubscribe_reason = models.CharField(max_length=30, choices=UNSUBSCRIBE_REASON, blank=True, verbose_name=' გაუქმების მიზეზი')

    class Meta:
        verbose_name = ' კლიენტი'
        verbose_name_plural = ' კლიენტები'

    def __str__(self):
        return self.application.name_surname


class Payments(models.Model):
    payment_time = models.DateField(auto_now_add=True, verbose_name=' გადახდის თარიღი')
    amount = models.IntegerField(verbose_name=' თანხა')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name=' კლიენტი')

    class Meta:
        verbose_name = ' გადახდა'
        verbose_name_plural = ' გადახდები'

    def __str__(self):
        return str(self.client.application.name_surname)


# KZ MODELS ======================================================================================

# KZ SETS
APPLICATION_STATUS_KZ = (
    ('new', 'Новая'),
    ('processed', 'Обработанная')
)
CALL_STATUS_KZ = (
    ('connected', 'Подключен'),
    ('declined', 'Отказ'),
    ('call me later', 'Позвонить позже'),
    ('didn\'t answer', 'Не ответил на звонок')
)
DECLINED_REASONS_KZ = (
    ('not interested', 'Не заинтересован'),
    ('no internet', 'Нету интернета'),
    ('no device', 'Нету устройства Android/Smart TV'),
    ('too expensive', 'Дорого')
)
PACKETS_KZ = (
    ('1', '1 мес'),
    ('3', '3 мес'),
    ('6', '6 мес'),
)
UNSUBSCRIBE_REASON_KZ = (
    ('too expensive', "Дорого"),
    ('a lot of channels doesn\'t work', "Множество каналов не работают"),
    ('rewind function ', "Не работает перемотка"),
    ('freezes ', "Застревают каналы"),
)


class ApplicationKZ(models.Model):
    name_surname = models.CharField(max_length=50, verbose_name=" Имя Фамилия")
    phone_number = models.CharField(max_length=50, verbose_name=" Номер телефона")
    town = models.CharField(max_length=50, verbose_name=" Город")
    competitor = models.CharField(max_length=50 , blank=True, verbose_name=' Интернет провайдер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=" Время получения заявки")
    updated_at = models.DateTimeField(auto_now=True, verbose_name=' Время изменения заявки')

    application_status = models.CharField(max_length=50, choices=APPLICATION_STATUS_KZ, default='new', verbose_name=' Статус анкеты')
    call_status = models.CharField(max_length=50, choices=CALL_STATUS_KZ, blank=True, verbose_name=' Статус звонка')
    declined_reason = models.CharField(max_length=50, choices=DECLINED_REASONS_KZ, blank=True, verbose_name=' Причина отказа')
    other_comment = models.TextField(blank=True, verbose_name=' Доп. комментарий')

    class Meta:
        verbose_name = ' Анкетка'
        verbose_name_plural = ' Анкеты'

    def __str__(self):
        return self.name_surname


class ClientKZ(models.Model):

    application = models.OneToOneField(ApplicationKZ, on_delete=models.PROTECT, primary_key=True, verbose_name=' Анкета')
    email = models.EmailField(unique=True)
    client_password = models.CharField(max_length=50, verbose_name=' Пароль')
    phone_number = models.CharField(max_length=50, verbose_name=' Номер телефона')
    status = models.BooleanField(default=True, verbose_name=' Статус')
    town = models.CharField(max_length=50, verbose_name=' Город')
    hosts = models.IntegerField(default=1, verbose_name=' Кол-во устройств')
    comment = models.TextField(blank=True, verbose_name=' Комментарий')
    first_payment_date = models.DateField(auto_now_add=True, verbose_name=' Дата первого пополнения')
    payed_until = models.DateField(null=True, verbose_name=' Дата следующей оплаты')
    packets = models.CharField(max_length=50, choices=PACKETS_KZ, verbose_name=' Пакеты')
    packet_plus = models.TextField(blank=True, verbose_name=' Доп. пакеты')
    unsubscribe_reason = models.CharField(max_length=30, choices=UNSUBSCRIBE_REASON_KZ, blank=True, verbose_name=' Причина отписки')

    class Meta:
        verbose_name = ' Клиент'
        verbose_name_plural = ' Клиенты'

    def __str__(self):
        return self.application.name_surname


class PaymentsKZ(models.Model):
    payment_time = models.DateField(auto_now_add=True, verbose_name=' Дата оплаты')
    amount = models.IntegerField(verbose_name=' Сумма')
    client = models.ForeignKey(ClientKZ, on_delete=models.PROTECT, verbose_name=' Клиент')

    class Meta:
        verbose_name = ' Оплата'
        verbose_name_plural = ' Оплаты'

    def __str__(self):
        return str(self.client.application.name_surname)
