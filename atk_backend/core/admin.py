from django.contrib import admin
from .models import TraineeProfile

@admin.register(TraineeProfile)
class TraineeProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'belt_rank', 'phone_number', 'level']
    list_filter = ['age', 'belt_rank', 'level']
    search_fields = ["user", "age"]
    ordering = ['level', 'belt_rank']
