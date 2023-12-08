from django.db import models







# Create your models here.
class Musician(models.Model):
    firs_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    nickname = models.CharField(max_length=25, blank=True)
    is_group = models.BooleanField(default=False)
    group_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if self.is_group:
            return self.group_name
        elif self.nickname:
            return self.nickname
        else:
            return f'{self.firs_name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='songs')
    feat = models.ForeignKey(Musician, on_delete=models.SET_NULL, related_name='feat', null=True, blank=True)
    poster = models.ImageField(upload_to='image')
    year = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} ft. {self.feat}'
        return f'{self.author} - {self.title}'


class Grammy(models.Model):
    owner = models.OneToOneField(Musician, on_delete=models.CASCADE)
    year = models.DateField()
    song = models.OneToOneField(Song, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.owner} -> Grammy {self.year.strftime("%Y")}'

    class Meta:
        verbose_name = 'grammy'
        verbose_name_plural = 'grammies'
