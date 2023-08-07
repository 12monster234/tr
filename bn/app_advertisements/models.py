from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html

User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField( "title", max_length=100)
    description = models.TextField('opisanie')
    price = models.DecimalField('cena',max_digits=10, decimal_places=2)
    auction = models.BooleanField('torg', help_text='уместность торга')
    createdat = models.DateTimeField(auto_now_add= True)
    updateat = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='user',
                             on_delete=models.CASCADE)
    image = models.ImageField("image",
                              upload_to="bn/")

    # @admin.display(description='Date')
    # def created_date(self)
    #     from django.utils import timezone
    #     if self.createdat.date() == timezone.now.date():
    #         created_time = self.createdat.time().strftime("%H:%M:%S")
    #         return format_html(
    #             '<span style ="color: green; font-weight: bold;">
    #             Today'
    #         )

    def __str__(self) -> str:
        return f"Advertisements(id={self.id} title =" \
               f"{self.title} price = {self.price}"


    class Meta:
        db_table = 'advertisemets'



# Create your models here.

