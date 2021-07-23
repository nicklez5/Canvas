from django.db import models
from core.models import TimestampedModel

class Profile(TimestampedModel):
    # There is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'myapi.User', on_delete=models.CASCADE
    )

    # Each user profile will have a field where they can tell other users
    # something about themselves. This field will be empty when the user
    # creates their account, so we specify blank=True.
    bio = models.TextField(blank=True)

    # In addition to the `bio` field, each user may have a profile image or
    # avatar. This field is not required and it may be blank.
    image = models.URLField(blank=True)

    # A timestamp representing when this object was created.
    #created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    #updated_at = models.DateTimeField(auto_now=True)

    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )

    favorites = models.ManyToManyField(
        'articles.Article',
        related_name='favorited_by'
    )

    def favorite(self,article):
        self.favorites.add(article)

    def unfavorite(self,article):
        self.favorites.remove(article)

    def has_favorited(self,article):
        return self.favorites.filter(pk=article.pk).exists()

    
    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.follows.add(profile)

    def unfollow(self, profile):
        self.follows.remove(profile)
    
    def is_following(self,profile):
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self,profile):
        return self.followed_by.filter(pk=profile.pk).exists()

    