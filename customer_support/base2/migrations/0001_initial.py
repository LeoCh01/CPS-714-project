# Generated by Django 5.1.3 on 2024-11-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticationlogs',
            fields=[
                ('log_id', models.IntegerField(db_column='log_ID', primary_key=True, serialize=False)),
                ('login_time_timestamp', models.CharField(max_length=255, unique=True)),
                ('success', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'authenticationlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chatlogs',
            fields=[
                ('chatid', models.IntegerField(db_column='ChatID', primary_key=True, serialize=False)),
                ('message', models.TextField(db_column='Message')),
                ('created_at', models.DateField(db_column='Created_AT')),
            ],
            options={
                'db_table': 'chatlogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Educationalresources',
            fields=[
                ('resourceid', models.IntegerField(db_column='ResourceID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=100, unique=True)),
                ('content', models.TextField(db_column='Content')),
                ('resourcetype', models.CharField(db_column='ResourceType', max_length=255, unique=True)),
                ('dateadded', models.CharField(db_column='DateAdded', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'educationalresources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loyaltypoints',
            fields=[
                ('pointsid', models.IntegerField(db_column='PointsID', primary_key=True, serialize=False)),
                ('action', models.CharField(db_column='Action', max_length=300)),
            ],
            options={
                'db_table': 'loyaltypoints',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loyaltyrewards',
            fields=[
                ('rewardid', models.IntegerField(db_column='RewardID', primary_key=True, serialize=False)),
                ('rewarddescription', models.CharField(db_column='RewardDescription', max_length=255, unique=True)),
                ('pointsrequired', models.CharField(db_column='PointsRequired', max_length=255, unique=True)),
                ('redemptiondate', models.DateField(db_column='RedemptionDate', unique=True)),
            ],
            options={
                'db_table': 'loyaltyrewards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multiplechoiceoption',
            fields=[
                ('optionposition', models.IntegerField(db_column='OptionPosition', primary_key=True, serialize=False)),
                ('optiontext', models.CharField(db_column='OptionText', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'multiplechoiceoption',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multiplechoicequestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxselectionnumber', models.IntegerField(db_column='MaxSelectionNumber', unique=True)),
            ],
            options={
                'db_table': 'multiplechoicequestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multiplechoiceresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectedoption', models.IntegerField(db_column='SelectedOption', unique=True)),
            ],
            options={
                'db_table': 'multiplechoiceresponse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productid', models.IntegerField(db_column='ProductID', primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='ProductName', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchasehistory',
            fields=[
                ('purchaseid', models.IntegerField(db_column='PurchaseID', primary_key=True, serialize=False)),
                ('purchasedate', models.DateField(db_column='PurchaseDate', unique=True)),
                ('pointsearned', models.CharField(db_column='PointsEarned', max_length=45, unique=True)),
                ('pointsredeemed', models.CharField(db_column='PointsRedeemed', max_length=45, unique=True)),
                ('totalspent', models.DecimalField(db_column='TotalSpent', decimal_places=0, max_digits=65, unique=True)),
            ],
            options={
                'db_table': 'purchasehistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('surveyposition', models.IntegerField(db_column='SurveyPosition', primary_key=True, serialize=False)),
                ('questiontext', models.CharField(db_column='QuestionText', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rewardredemption',
            fields=[
                ('redemptionid', models.IntegerField(db_column='RedemptionID', primary_key=True, serialize=False)),
                ('redemptiondate', models.DateField(db_column='RedemptionDate')),
            ],
            options={
                'db_table': 'rewardredemption',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('reward_id', models.IntegerField(db_column='reward_ID', primary_key=True, serialize=False)),
                ('points', models.IntegerField(db_column='Points', unique=True)),
                ('reward_date_timestamp', models.CharField(db_column='reward_Date_timestamp', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'rewards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.PositiveIntegerField(db_column='Role_ID', primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('survey_response_id', models.IntegerField(db_column='Survey_Response_ID', primary_key=True, serialize=False)),
                ('survery_id', models.CharField(db_column='Survery_ID', max_length=255, unique=True)),
                ('user_id', models.CharField(db_column='User_ID', max_length=255, unique=True)),
                ('response_text', models.CharField(db_column='Response_text', max_length=1000)),
            ],
            options={
                'db_table': 'survey_response',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('survey_id', models.IntegerField(db_column='Survey_ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'surveys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Textualquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charlimit', models.IntegerField(db_column='CharLimit')),
            ],
            options={
                'db_table': 'textualquestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Textualresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsetext', models.CharField(db_column='ResponseText', max_length=1000, unique=True)),
            ],
            options={
                'db_table': 'textualresponse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TicketResponse',
            fields=[
                ('ticket_response_id', models.IntegerField(db_column='Ticket_Response_ID', primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, db_column='User_ID', max_length=255, null=True)),
                ('response_text', models.CharField(blank=True, db_column='Response_text', max_length=255, null=True)),
                ('responded_at', models.CharField(blank=True, db_column='Responded_at', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ticket_response',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.IntegerField(db_column='Ticket_ID', primary_key=True, serialize=False)),
                ('ticket_status', models.CharField(db_column='Ticket_status', max_length=255, unique=True)),
                ('priority', models.CharField(db_column='Priority', max_length=255, unique=True)),
                ('created_at', models.CharField(db_column='Created_at', max_length=255)),
                ('ticket_text', models.CharField(db_column='Ticket_text', max_length=1000)),
            ],
            options={
                'db_table': 'tickets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transactionid', models.IntegerField(db_column='TransactionID', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
            ],
            options={
                'db_table': 'transactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(db_column='User_ID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=255, unique=True)),
                ('user_password', models.CharField(db_column='User_Password', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userresourceaccess',
            fields=[
                ('accessid', models.IntegerField(db_column='AccessID', primary_key=True, serialize=False)),
                ('accessdate', models.CharField(db_column='AccessDate', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'userresourceaccess',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('user_role_id', models.IntegerField(db_column='User_role_ID', primary_key=True, serialize=False)),
                ('user_id', models.CharField(db_column='User_ID', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'user_roles',
                'managed': False,
            },
        ),
    ]
