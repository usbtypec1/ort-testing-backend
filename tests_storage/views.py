from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models, serializers


class ReadTestsList(ReadOnlyModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestsSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        section = self.request.query_params.get('section')
        if section is None:
            queryset = models.Question.objects.filter(tests__id=pk)
        else:
            queryset = models.Question.objects.filter(tests__id=pk, section=section)
        return Response(serializers.QuestionSerializer(queryset, many=True).data)


@api_view(['GET'])
def sections_list(request):
    data = [{'id': id, 'name': name} for id, name in models.Question.SECTIONS_CHOICES]
    return Response(data)
