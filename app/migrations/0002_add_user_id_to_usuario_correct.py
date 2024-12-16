from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_add_user_id_to_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.RunSQL(
            sql="ALTER TABLE app_usuario ADD CONSTRAINT user_id_refs_id FOREIGN KEY (user_id) REFERENCES auth_user(id);",
            reverse_sql="ALTER TABLE app_usuario DROP CONSTRAINT user_id_refs_id;"
        ),
    ]