from rest_framework.serializers import ModelSerializer

from . import models


class TestsSerializer(ModelSerializer):
    class Meta:
        model = models.Test
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id', 'title', 'image_url', 'section', 'correct_answer',
                  'wrong_answer_1', 'wrong_answer_2', 'wrong_answer_3', 'wrong_answer_4')
