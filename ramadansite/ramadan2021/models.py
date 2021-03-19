from django.db import models

class Answer(models.Model):
    answer_text = models.CharField(max_length=200, verbose_name="Ответ")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.answer_text

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'ответы'
        verbose_name_plural = 'ответы'
        ordering = ['id']

        

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="категория")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категории'
        ordering = ['id']


