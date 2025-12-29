from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='Test', points=5)
        self.assertEqual(lb.points, 5)
    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test', workout='Pushup', reps=20)
        self.assertEqual(workout.reps, 20)
