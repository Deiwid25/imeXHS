from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Element
from .serializers import ElementSerializer, ElementUpdateSerializer, ElementGetSerializer

class ElementAPIView(APIView):

  @swagger_auto_schema(
    operation_description="Retrieve a specific entry by ID or list all entries.",
    responses={
      200: ElementGetSerializer(many=True),
      404: 'Not found'
    }
  )
  def get(self, request, id=None):
    """Retrieve a specific entry by ID or list all entries."""
    if id:
      try:
        element = Element.objects.get(id=id)
        serializer = ElementGetSerializer(element)
        return Response(serializer.data, status=status.HTTP_200_OK)
      except Element.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    else:
      elements = Element.objects.all()
      serializer = ElementSerializer(elements, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

  @swagger_auto_schema(
    operation_description="Create a new entry.",
    request_body=ElementSerializer,
    responses={
      201: ElementSerializer,
      400: 'Bad Request'
    }
  )
  def post(self, request):
    """Create a new entry."""
    serializer = ElementSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  @swagger_auto_schema(
    operation_description="Update an existing Element by ID.",
    request_body=ElementUpdateSerializer,
    responses={
      200: ElementUpdateSerializer,
      404: 'Element not found',
      400: 'Bad Request'
    }
  )
  def patch(self, request, *args, **kwargs):
    """Update an existing Element by ID."""
    try:
      element = Element.objects.get(id=kwargs['id'])
    except Element.DoesNotExist:
      return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ElementUpdateSerializer(element, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  @swagger_auto_schema(
    operation_description="Delete an entry by ID.",
    responses={
      204: 'Deleted successfully.',
      404: 'Not found',
      400: 'ID is required for deletion.'
    }
  )
  def delete(self, request, id=None):
    """Delete an entry by ID."""
    if not id:
      return Response({'detail': 'ID is required for deletion.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
      element = Element.objects.get(id=id)
    except Element.DoesNotExist:
      return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    element.delete()
    return Response({'detail': 'Deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
