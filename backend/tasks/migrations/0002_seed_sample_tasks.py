from django.db import migrations


def seed_sample_tasks(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')

    replacements = [
        {
            'old_description': 'I want to built an ap',
            'title': 'App',
            'description': 'I want to build an app',
            'priority': 'High',
            'completed': True,
        },
        {
            'old_description': 'I wanna watch the movie',
            'title': 'Movie',
            'description': 'I want to watch a movie',
            'priority': 'Medium',
            'completed': True,
        },
    ]

    existing_count = Task.objects.count()

    for item in replacements:
        Task.objects.filter(description=item['old_description']).update(
            title=item['title'],
            description=item['description'],
            priority=item['priority'],
            completed=item['completed'],
        )

    if existing_count == 0:
        for item in replacements:
            Task.objects.create(
                title=item['title'],
                description=item['description'],
                priority=item['priority'],
                completed=item['completed'],
            )


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_sample_tasks, migrations.RunPython.noop),
    ]