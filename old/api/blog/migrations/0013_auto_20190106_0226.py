# Generated by Django 2.1.3 on 2019-01-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_merge_20190106_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(help_text='Readable name to be displayed for articles.', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='articles/img/default_blog_img.png', help_text='Preview Image for the article.', upload_to='articles/img'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(help_text='Space seperated, e.g. (javascript django ).', to='blog.Tag'),
        ),
    ]