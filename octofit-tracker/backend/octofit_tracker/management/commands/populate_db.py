from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from pymongo import MongoClient
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Limpa as coleções
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Cria índice único para email
        db.users.create_index([('email', 1)], unique=True)

        # Times
        teams = [
            {'name': 'Marvel'},
            {'name': 'DC'}
        ]
        db.teams.insert_many(teams)

        # Usuários
        users = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'}
        ]
        db.users.insert_many(users)

        # Atividades
        activities = [
            {'user': 'Superman', 'activity': 'Flight', 'duration': 60},
            {'user': 'Batman', 'activity': 'Martial Arts', 'duration': 45},
            {'user': 'Iron Man', 'activity': 'Suit Training', 'duration': 30},
            {'user': 'Spider-Man', 'activity': 'Web Swing', 'duration': 50}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'user': 'Superman', 'points': 100},
            {'user': 'Iron Man', 'points': 90},
            {'user': 'Batman', 'points': 80}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user': 'Wonder Woman', 'workout': 'Strength', 'reps': 100},
            {'user': 'Captain America', 'workout': 'Shield Throw', 'reps': 50}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populado com dados de teste!'))
