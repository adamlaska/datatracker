# Generated by Django 2.2.28 on 2022-06-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_remove_docs2_m2m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchrule',
            name='rule_type',
            field=models.CharField(choices=[('group', 'All I-Ds associated with a particular group'), ('area', 'All I-Ds associated with all groups in a particular Area'), ('group_rfc', 'All RFCs associated with a particular group'), ('area_rfc', 'All RFCs associated with all groups in a particular Area'), ('group_exp', 'All expired I-Ds of a particular group'), ('state_iab', 'All I-Ds that are in a particular IAB state'), ('state_iana', 'All I-Ds that are in a particular IANA state'), ('state_iesg', 'All I-Ds that are in a particular IESG state'), ('state_irtf', 'All I-Ds that are in a particular IRTF state'), ('state_ise', 'All I-Ds that are in a particular ISE state'), ('state_rfceditor', 'All I-Ds that are in a particular RFC Editor state'), ('state_ietf', 'All I-Ds that are in a particular Working Group state'), ('author', 'All I-Ds with a particular author'), ('author_rfc', 'All RFCs with a particular author'), ('ad', 'All I-Ds with a particular responsible AD'), ('shepherd', 'All I-Ds with a particular document shepherd'), ('name_contains', 'All I-Ds with particular text/regular expression in the name')], max_length=30),
        ),
    ]