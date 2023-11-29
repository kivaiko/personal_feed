import os
import django
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_test.settings")
django.setup()

from users.models import User
from achievements.models import Achievement, UserAchievement

ACHIEVEMENTS_IMAGES_PATH = "seed_data"


def create_users():
    user1_data = {
        "username": "user1",
        "email": "user1@example.com",
        "first_name": "User",
        "last_name": "One",
    }
    user1, created = User.objects.get_or_create(**user1_data)
    if created:
        user1.set_password("password123")
        user1.is_superuser = True
        user1.is_staff = True
        user1.save()

    user2_data = {
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "User",
        "last_name": "Two",
    }
    user2, created = User.objects.get_or_create(**user2_data)
    if created:
        user2.set_password("password123")
        user2.save()

    return [user1, user2]


def create_achievements():
    achievements_data = [
        ("Achievement 1", "Description 1", "icons8-basketball-96.png"),
        ("Achievement 2", "Description 2", "icons8-bullseye-96.png"),
        ("Achievement 3", "Description 3", "icons8-firecracker-96.png"),
    ]

    created_achievements = []
    for name, description, image_filename in achievements_data:
        with open(
            os.path.join(ACHIEVEMENTS_IMAGES_PATH, image_filename), "rb"
        ) as image_file:
            achievement, created = Achievement.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                    "icon": File(image_file, name=image_filename),
                },
            )
            created_achievements.append(achievement)
    return created_achievements


def assign_achievements_to_users(users, achievements):
    UserAchievement.objects.get_or_create(
        user=users[0], achievement=achievements[0]
    )
    UserAchievement.objects.get_or_create(
        user=users[1], achievement=achievements[1]
    )
    UserAchievement.objects.get_or_create(
        user=users[1], achievement=achievements[2]
    )


def run_seed():
    users = create_users()
    achievements = create_achievements()
    assign_achievements_to_users(users, achievements)
    print("Готово!")


if __name__ == "__main__":
    run_seed()
