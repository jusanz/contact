from django.db import models


class Contact(models.Model):
    json = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if not "email" in self.json:
            return super().__str__()
        return "{}".format(self.json["email"])
