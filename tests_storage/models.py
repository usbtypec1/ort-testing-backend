from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'Test: {self.name}'


class Question(models.Model):
    MATH_PART_1 = 2
    MATH_PART_2 = 3
    ANALOGIES = 0
    SENTENCES_COMPLETION = 1
    READING = 4
    GRAMMAR = 5
    SECTIONS_CHOICES = (
        (0, 'Analogies'),
        (1, 'Sentences completion'),
        (2, 'Math part 1'),
        (3, 'Math part 2'),
        (4, 'Reading'),
        (5, 'Grammar'),
    )

    title = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    tests = models.ManyToManyField(Test)
    section = models.PositiveSmallIntegerField(choices=SECTIONS_CHOICES)
    correct_answer = models.TextField()
    wrong_answer_1 = models.TextField()
    wrong_answer_2 = models.TextField()
    wrong_answer_3 = models.TextField()
    wrong_answer_4 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Question: {self.title}'
