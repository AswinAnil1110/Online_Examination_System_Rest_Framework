from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionDb,SubmissionDb
from ExamApp.serializers import QuestionSerializer,SubmissionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs = QuestionDb.objects.all()
        serializer_instance = QuestionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance= QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response({"message":"Question added successfully"})
        else:
            return Response(data=serializer_instance.errors)

class QuestionRetriveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs = QuestionDb.objects.get(id=pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**original_data)
            return Response({"Message":"Question Updated Successfully"})
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response({"Message":"Question Deleted Successfully"})

class SubmissionListCreateView(APIView):
    def get(self,request):
        qs = SubmissionDb.objects.all()
        serializer_instance = SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"Submission Added successfully"})
        else:
            return Response(data=serializer_instance.errors)
class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs = get_object_or_404(SubmissionDb,id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk):
        form_data = request.data
        submission_object = get_object_or_404(SubmissionDb,id=pk)
        serializer_instance = SubmissionSerializer(data=form_data,instance=submission_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"Submission Updated Successfully"})
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        submission_object = get_object_or_404(SubmissionDb,id=pk)
        submission_object.delete()
        return Response({"Message":"Submission Deleted Successfully"})

class SubmissionEvaluate(APIView):
    def put(self,request,pk):
        form_data = request.data
        SubmissionDb.objects.filter(id=pk).update(**form_data)
        return Response({"Message":"Submission Updated Successfully"})