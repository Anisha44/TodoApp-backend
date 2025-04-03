from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo


class SystemViewTest(TestCase):
    def test_full_system(self):
        print("1. register start")
        # mock user
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, 201)  # 201 created
        # get user instance
        self.user = User.objects.get(username='newuser')

        # check if user is created
        self.assertTrue(User.objects.filter(username='newuser').exists())
        print("1. register testing finish username:" + self.user.username)

        print("2. login testing start")

        response = self.client.post('/api/auth/login/', {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)

        self.token = response.json()['access']
        self.assertIsNotNone(self.token)
        print("2. login testing finish, token:" + self.token)
        # delete user clean up
        self.user.delete()


class TodoModelTest(TestCase):
    def test_add_task(self):
        print("3. create task testing start")
        user = User.objects.create_user(username='newuser', password='newpassword')
        task = Todo.objects.create(task_title="Test Task", task_description="desc", priority='low',comments='Todo Comment', status="pending", user=user)
        # self.assertEqual(task.title, "Test Task")

        print("3. create task testing finish")


        print("4. update task testing start")

        task.task_title="Test now Title"
        task.save()

        print("4. update task testing finish")


        print("5. delete task testing start")

        task.delete()
        # self.assertEqual(task.title, "Test Task")
        print("5. create task testing finish")


