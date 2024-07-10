# Generated by Django 5.0.4 on 2024-06-06 08:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_interaktivxizmat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SecondSliderImage',
        ),
        migrations.DeleteModel(
            name='SliderImage',
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Application', 'verbose_name_plural': 'Applications'},
        ),
        migrations.AlterModelOptions(
            name='deal',
            options={'verbose_name': 'Deal', 'verbose_name_plural': 'Deals'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Regulatory Document', 'verbose_name_plural': 'Regulatory Documents'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Gallery'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RemoveField(
            model_name='deal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='title',
        ),
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.RemoveField(
            model_name='interaktivxizmat',
            name='title',
        ),
        migrations.RemoveField(
            model_name='logo',
            name='text',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='group_deal',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer_country',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_per_unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='trade_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='warranty_type',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='text',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='title',
        ),
        migrations.RemoveField(
            model_name='vazirlik',
            name='text',
        ),
        migrations.RemoveField(
            model_name='vazirlik',
            name='title',
        ),
        migrations.AddField(
            model_name='deal',
            name='description_en',
            field=models.TextField(default='Default Description', verbose_name='Description (English)'),
        ),
        migrations.AddField(
            model_name='deal',
            name='description_ru',
            field=models.TextField(default='Default Description', verbose_name='Description (Russian)'),
        ),
        migrations.AddField(
            model_name='deal',
            name='description_uz',
            field=models.TextField(default='Default Description', verbose_name='Description (Uzbek)'),
        ),
        migrations.AddField(
            model_name='deal',
            name='title_en',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (English)'),
        ),
        migrations.AddField(
            model_name='deal',
            name='title_ru',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (Russian)'),
        ),
        migrations.AddField(
            model_name='deal',
            name='title_uz',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (Uzbek)'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_en',
            field=models.CharField(default='Default Title (English)', max_length=255, verbose_name='Title (English)'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ru',
            field=models.CharField(default='Default Title (Russian)', max_length=255, verbose_name='Title (Russian)'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_uz',
            field=models.CharField(default='Default Title (Uzbek)', max_length=255, verbose_name='Title (Uzbek)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address_en',
            field=models.CharField(default='Default Address', max_length=200, verbose_name='Address (English)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address_ru',
            field=models.CharField(default='Default Address', max_length=200, verbose_name='Address (Russian)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address_uz',
            field=models.CharField(default='Default Address', max_length=200, verbose_name='Address (Uzbek)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='comment_en',
            field=models.TextField(blank=True, default='Default Comment', null=True, verbose_name='Comment (English)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='comment_ru',
            field=models.TextField(blank=True, default='Default Comment', null=True, verbose_name='Comment (Russian)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='comment_uz',
            field=models.TextField(blank=True, default='Default Comment', null=True, verbose_name='Comment (Uzbek)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name_en',
            field=models.CharField(default='Default Full Name', max_length=100, verbose_name='Full Name (English)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name_ru',
            field=models.CharField(default='Default Full Name', max_length=100, verbose_name='Full Name (Russian)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name_uz',
            field=models.CharField(default='Default Full Name', max_length=100, verbose_name='Full Name (Uzbek)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_en',
            field=models.CharField(default='Default Position', max_length=100, verbose_name='Position (English)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_ru',
            field=models.CharField(default='Default Position', max_length=100, verbose_name='Position (Russian)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_uz',
            field=models.CharField(default='Default Position', max_length=100, verbose_name='Position (Uzbek)'),
        ),
        migrations.AddField(
            model_name='image',
            name='title_en',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (English)'),
        ),
        migrations.AddField(
            model_name='image',
            name='title_ru',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (Russian)'),
        ),
        migrations.AddField(
            model_name='image',
            name='title_uz',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (Uzbek)'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='title_en',
            field=models.CharField(default='Default Name', max_length=100, verbose_name='Name (English)'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='title_ru',
            field=models.CharField(default='Default Name', max_length=100, verbose_name='Name (Russian)'),
        ),
        migrations.AddField(
            model_name='interaktivxizmat',
            name='title_uz',
            field=models.CharField(default='Default Name', max_length=100, verbose_name='Name (Uzbek)'),
        ),
        migrations.AddField(
            model_name='logo',
            name='text_en',
            field=models.TextField(default='Default Text', verbose_name='Text (English)'),
        ),
        migrations.AddField(
            model_name='logo',
            name='text_ru',
            field=models.TextField(default='Default Text', verbose_name='Text (Russian)'),
        ),
        migrations.AddField(
            model_name='logo',
            name='text_uz',
            field=models.TextField(default='Default Text', verbose_name='Text (Uzbek)'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_en',
            field=models.TextField(default='Default Text', verbose_name='Text (English)'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=models.TextField(default='Default Text', verbose_name='Text (Russian)'),
        ),
        migrations.AddField(
            model_name='news',
            name='text_uz',
            field=models.TextField(default='Default Text', verbose_name='Text (Uzbek)'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(default='Default Title', max_length=200, verbose_name='Title (English)'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(default='Default Title', max_length=200, verbose_name='Title (Russian)'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(default='Default Title', max_length=200, verbose_name='Title (Uzbek)'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(default='Default Description', verbose_name='Description (English)'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(default='Default Description', verbose_name='Description (Russian)'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(default='Default Description', verbose_name='Description (Uzbek)'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(default='Default Name', max_length=100, verbose_name='Name (English)'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(default='Default Name', max_length=100, verbose_name='Name (Russian)'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uz',
            field=models.CharField(default='Default Name', max_length=100, verbose_name='Name (Uzbek)'),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='text_en',
            field=models.TextField(default=1, verbose_name='Text (English)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='text_ru',
            field=models.TextField(default=1, verbose_name='Text (Russian)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='text_uz',
            field=models.TextField(default=1, verbose_name='Text (Uzbek)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='title_en',
            field=models.CharField(default=1, max_length=100, verbose_name='Title (English)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='title_ru',
            field=models.CharField(default=1, max_length=100, verbose_name='Title (Russian)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinfo',
            name='title_uz',
            field=models.CharField(default=1, max_length=100, verbose_name='Title (Uzbek)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='text_en',
            field=models.TextField(default='Default Text', verbose_name='Text (English)'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='text_ru',
            field=models.TextField(default='Default Text', verbose_name='Text (Russian)'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='text_uz',
            field=models.TextField(default='Default Text', verbose_name='Text (Uzbek)'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='title_en',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (English)'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='title_ru',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (Russian)'),
        ),
        migrations.AddField(
            model_name='vazirlik',
            name='title_uz',
            field=models.CharField(default='Default Title', max_length=100, verbose_name='Title (Uzbek)'),
        ),
        migrations.AlterField(
            model_name='application',
            name='first_name',
            field=models.CharField(default='Default First Name', max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_name',
            field=models.CharField(default='Default Last Name', max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(default='Default Phone Number', max_length=20, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='gmail',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='img',
            field=models.ImageField(default='tender/default.jpg', upload_to='tender/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Publish Date'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='site',
            field=models.URLField(verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='status',
            field=models.CharField(default='New', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Views'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='interaktivxizmat',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='interaktivxizmat',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Views'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='link',
            field=models.URLField(verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.URLField(default='https://www.gazeta.uz/oz/2024/04/13/yunusabad/', verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Views'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image'),
        ),
    ]
