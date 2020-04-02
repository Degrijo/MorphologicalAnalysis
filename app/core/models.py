from django.db import models


class PartOfSpeech(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=30)


class ProposalMember(models.Model):
    name = models.CharField(max_length=200)
    parts_of_speech = models.ManyToManyField(PartOfSpeech, related_name='proposal_members')

