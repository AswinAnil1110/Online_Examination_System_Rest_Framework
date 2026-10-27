from rest_framework import serializers
from ExamApp.models import SubmissionDb,QuestionDb

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=100)
    option_a = serializers.CharField(max_length=100)
    option_b = serializers.CharField(max_length=100)
    option_c = serializers.CharField(max_length=100)
    option_d = serializers.CharField(max_length=100)
    correct_answer = serializers.CharField(max_length=100)
    
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionDb
        fields = "__all__"
        read_only_fields = ["id,status"]
    def validate(self,validated_data):
        question_id = validated_data.get("question_id")
        if not QuestionDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exists...!")
        return validated_data
