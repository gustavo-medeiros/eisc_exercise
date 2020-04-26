from django.db import models


class Artist(models.Model):
    Name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "artiste"
        ordering = ['id']

    def __str__(self):
        return self.Name


class Album(models.Model):
    Title = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Album"
        ordering = ['id']

    def __str__(self):
        return self.Title


class Track(models.Model):
    Name = models.CharField(max_length=100)
    Composer = models.CharField(max_length=100)
    Milliseconds = models.IntegerField()
    Bytes = models.IntegerField()
    UnitPrice = models.IntegerField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Track"
        ordering = ['id']

    def __str__(self):
        return self.Name

