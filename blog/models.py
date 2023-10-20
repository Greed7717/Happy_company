from django.db import models

class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


    TYPE_BOOK = (
        ('Фантастика', 'Фанатастика'),
        ('Художественная', 'Художественная'),
        ('Хоррор', 'Хоррор'),
        ('Фентези', 'Фентези')
    )

    title = models.CharField(max_length=100, verbose_name='Название книги', null=True)
    image = models.ImageField(upload_to='', verbose_name='Загрузите фото')
    description = models.TextField(blank=True, null=True, verbose_name='Дайте описание')
    type_book = models.CharField(max_length=100, choices=TYPE_BOOK, null=True, verbose_name='выебрите жанр')
    cost = models.PositiveIntegerField(verbose_name='Укажите цену', null=True)
    director = models.CharField(max_length=100, verbose_name='Укажите имя автора', null=True )
    number_of_page = models.IntegerField(null=True, verbose_name='Укажите колличество страниц')
    date_start = models.DateField(verbose_name='Укажите дату издания', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'Название книги {self.title}- \n'
                f'Цена книги {self.cost}')

