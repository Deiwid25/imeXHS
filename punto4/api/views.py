from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Element
from .serializers import ElementSerializer, ElementUpdateSerializer, ElementGetSerializer

class ElementAPIView(APIView):
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

  def post(self, request):
    """Create a new entry."""
    serializer = ElementSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, *args, **kwargs):
    """Update an existing Element"""
    try:
      element = Element.objects.get(id=kwargs['id'])
    except Element.DoesNotExist:
      return Response({'error': 'Element not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ElementUpdateSerializer(element, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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