from django.db import models
from django.db.models import CharField, Case, When, Value, Avg
from django.db.models.functions import (
    ExtractSecond,
    ExtractMinute,
    ExtractHour,
    ExtractDay,
    ExtractMonth,
    ExtractYear,
)
from django.utils.timezone import now


class Data(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField("date published", default=now)

    def __str__(self):
        return f"ID: {self.id}, temperature: {self.temperature}, humidity: {self.humidity} recorded on {self.timestamp}"

    class Meta:
        verbose_name_plural = "data"

    def clean_db(self, aggr_minutes=5):
        """Remove obsolete data in database. Aggregate data by minute, hours, days."""

    @staticmethod
    def get_data_grouped_by_seconds():
        cases = [
            When(
                second__gte=x * 5,
                second__lt=(x + 1) * 5,
                then=Value(f"{x * 5}-{(x + 1) * 5}"),
            )
            for x in range(12)
        ]
        data = (
            Data.objects.annotate(
                year=ExtractYear("timestamp"),
                month=ExtractMonth("timestamp"),
                day=ExtractDay("timestamp"),
                hour=ExtractHour("timestamp"),
                minute=ExtractMinute("timestamp"),
                second=ExtractSecond("timestamp"),
            )
            .annotate(closest_part_of_minute=Case(*cases, output_field=CharField()))
            .values("year", "month", "day", "hour", "minute", "second", "closest_part_of_minute")
            .annotate(
                average_temperature=Avg("temperature"),
                average_humidity=Avg("humidity"),
            )
        )
        return data[:12]

    @staticmethod
    def get_data_grouped_by_minutes():
        cases = [
            When(
                minute__gte=x * 5,
                minute__lt=(x + 1) * 5,
                then=Value(f"{x * 5}-{(x + 1) * 5}"),
            )
            for x in range(12)
        ]
        data = (
            Data.objects.annotate(
                year=ExtractYear("timestamp"),
                month=ExtractMonth("timestamp"),
                day=ExtractDay("timestamp"),
                hour=ExtractHour("timestamp"),
                minute=ExtractMinute("timestamp"),
            )
            .annotate(closest_part_of_hour=Case(*cases, output_field=CharField()))
            .values("year", "month", "day", "hour", "minute", "closest_part_of_hour")
            .annotate(
                average_temperature=Avg("temperature"), average_humidity=Avg("humidity")
            )
        )
        return data[:12]

    @staticmethod
    def get_data_grouped_by_hour():
        cases = [
            When(hour__gte=x, hour__lt=x + 1, then=Value(f"{x}-{x + 1}"))
            for x in range(24)
        ]
        data = (
            Data.objects.annotate(
                year=ExtractYear("timestamp"),
                month=ExtractMonth("timestamp"),
                day=ExtractDay("timestamp"),
                hour=ExtractHour("timestamp"),
            )
            .annotate(closest_part_of_day=Case(*cases, output_field=CharField()))
            .values("year", "month", "day", "hour", "closest_part_of_day")
            .annotate(
                average_temperature=Avg("temperature"), average_humidity=Avg("humidity")
            )
        )
        return data[:24]
