from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from users.models import User
from .models import FeedEvent, NoteEvent
from .serializers import FeedEventSerializer
from django.db.models import Q
from rest_framework.permissions import AllowAny
import logging

logger = logging.getLogger(__name__)


class FeedEventPagination(PageNumberPagination):
    page_size = 10


class FeedEventListView(generics.ListAPIView):
    serializer_class = FeedEventSerializer
    pagination_class = FeedEventPagination
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("Пользователь с указанным ID не найден")

        try:
            queryset = self.filter_queryset(self.get_queryset())
        except Exception as e:
            logger.error(f"Ошибка при получении queryset: {e}")
            raise

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            custom_response = {
                "user": {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "feed": self.get_paginated_response(serializer.data).data,
            }
            return Response(custom_response)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        title_query = self.request.query_params.get("title", None)

        queryset = FeedEvent.objects.filter(
            Q(noteevent__note__user_id=user_id)
            | Q(achievementevent__achievement__user_id=user_id)
            | Q(advertisementevent__advertisement__isnull=False)
        ).distinct()

        if title_query:
            queryset = queryset.instance_of(NoteEvent).filter(
                noteevent__note__title__icontains=title_query
            )

        return queryset
