from django.db import models

class Answer(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'ответы'
        verbose_name_plural = 'ответы'
        ordering = ['id']

        

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="категория")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категории'
        ordering = ['id']


