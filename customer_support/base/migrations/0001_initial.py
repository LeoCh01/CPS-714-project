# Generated by Django 5.1.3 on 2024-11-12 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            },
        ),
        migrations.CreateModel(
            name='Loyaltypoints',
            fields=[
                ('pointsid', models.IntegerField(db_column='PointsID', primary_key=True, serialize=False)),
                ('action', models.CharField(db_column='Action', max_length=300)),
                ('loyaltyrewards_rewardid', models.ForeignKey(db_column='LoyaltyRewards_RewardID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.loyaltyrewards')),
            ],
            options={
                'db_table': 'loyaltypoints',
            },
        ),
        migrations.CreateModel(
            name='Multiplechoiceoption',
            fields=[
                ('optionposition', models.IntegerField(db_column='OptionPosition', primary_key=True, serialize=False)),
                ('optiontext', models.CharField(db_column='OptionText', max_length=255, unique=True)),
                ('question_surveyposition', models.ForeignKey(db_column='Question_SurveyPosition', on_delete=django.db.models.deletion.DO_NOTHING, to='base.question')),
            ],
            options={
                'db_table': 'multiplechoiceoption',
            },
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('survey_id', models.IntegerField(db_column='Survey_ID', primary_key=True, serialize=False)),
                ('survey_response_survey_response', models.ForeignKey(db_column='Survey_Response_Survey_Response_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveyresponse')),
            ],
            options={
                'db_table': 'surveys',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='surveys_survey',
            field=models.ForeignKey(db_column='Surveys_Survey_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveys'),
        ),
        migrations.CreateModel(
            name='Multiplechoicequestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxselectionnumber', models.IntegerField(db_column='MaxSelectionNumber', unique=True)),
                ('question_surveyposition', models.ForeignKey(db_column='Question_SurveyPosition', on_delete=django.db.models.deletion.DO_NOTHING, to='base.question')),
                ('surveys_survey', models.ForeignKey(db_column='Surveys_Survey_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveys')),
            ],
            options={
                'db_table': 'multiplechoicequestion',
            },
        ),
        migrations.CreateModel(
            name='Textualquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charlimit', models.IntegerField(db_column='CharLimit')),
                ('question_surveyposition', models.ForeignKey(db_column='Question_SurveyPosition', on_delete=django.db.models.deletion.DO_NOTHING, to='base.question')),
                ('surveys_survey', models.ForeignKey(db_column='Surveys_Survey_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveys')),
            ],
            options={
                'db_table': 'textualquestion',
            },
        ),
        migrations.CreateModel(
            name='TicketResponse',
            fields=[
                ('ticket_response_id', models.IntegerField(db_column='Ticket_Response_ID', primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, db_column='User_ID', max_length=255, null=True)),
                ('response_text', models.CharField(blank=True, db_column='Response_text', max_length=255, null=True)),
                ('responded_at', models.CharField(blank=True, db_column='Responded_at', max_length=255, null=True)),
                ('tickets_ticket', models.ForeignKey(db_column='Tickets_Ticket_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.tickets')),
            ],
            options={
                'db_table': 'ticket_response',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(db_column='User_ID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=255, unique=True)),
                ('user_password', models.CharField(db_column='User_Password', max_length=255, unique=True)),
                ('survey_response_survey_response', models.ForeignKey(db_column='Survey_Response_Survey_Response_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveyresponse')),
                ('ticket_response_ticket_response', models.ForeignKey(db_column='Ticket_response_Ticket_Response_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.ticketresponse')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transactionid', models.IntegerField(db_column='TransactionID', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('loyaltypoints_pointsid', models.ForeignKey(db_column='LoyaltyPoints_PointsID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.loyaltypoints')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.AddField(
            model_name='tickets',
            name='user_user',
            field=models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user'),
        ),
        migrations.CreateModel(
            name='Textualresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsetext', models.CharField(db_column='ResponseText', max_length=1000, unique=True)),
                ('question_surveyposition', models.ForeignKey(db_column='Question_SurveyPosition', on_delete=django.db.models.deletion.DO_NOTHING, to='base.question')),
                ('surveys_survey', models.ForeignKey(db_column='Surveys_Survey_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveys')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'textualresponse',
            },
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('reward_id', models.IntegerField(db_column='reward_ID', primary_key=True, serialize=False)),
                ('points', models.IntegerField(db_column='Points', unique=True)),
                ('reward_date_timestamp', models.CharField(db_column='reward_Date_timestamp', max_length=255, unique=True)),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'rewards',
            },
        ),
        migrations.CreateModel(
            name='Rewardredemption',
            fields=[
                ('redemptionid', models.IntegerField(db_column='RedemptionID', primary_key=True, serialize=False)),
                ('redemptiondate', models.DateField(db_column='RedemptionDate')),
                ('loyaltyrewards_rewardid', models.ForeignKey(db_column='LoyaltyRewards_RewardID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.loyaltyrewards')),
                ('rewards_reward', models.ForeignKey(db_column='Rewards_reward_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.rewards')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'rewardredemption',
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
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'purchasehistory',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productid', models.IntegerField(db_column='ProductID', primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='ProductName', max_length=255, unique=True)),
                ('tickets_ticket', models.ForeignKey(db_column='Tickets_Ticket_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.tickets')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Multiplechoiceresponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectedoption', models.IntegerField(db_column='SelectedOption', unique=True)),
                ('question_surveyposition', models.ForeignKey(db_column='Question_SurveyPosition', on_delete=django.db.models.deletion.DO_NOTHING, to='base.question')),
                ('surveys_survey', models.ForeignKey(db_column='Surveys_Survey_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.surveys')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'multiplechoiceresponse',
            },
        ),
        migrations.AddField(
            model_name='loyaltyrewards',
            name='user_user',
            field=models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user'),
        ),
        migrations.CreateModel(
            name='Chatlogs',
            fields=[
                ('chatid', models.IntegerField(db_column='ChatID', primary_key=True, serialize=False)),
                ('message', models.TextField(db_column='Message')),
                ('created_at', models.DateField(db_column='Created_AT')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'chatlogs',
            },
        ),
        migrations.CreateModel(
            name='Authenticationlogs',
            fields=[
                ('log_id', models.IntegerField(db_column='log_ID', primary_key=True, serialize=False)),
                ('login_time_timestamp', models.CharField(max_length=255, unique=True)),
                ('success', models.IntegerField(unique=True)),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'authenticationlogs',
            },
        ),
        migrations.CreateModel(
            name='Userresourceaccess',
            fields=[
                ('accessid', models.IntegerField(db_column='AccessID', primary_key=True, serialize=False)),
                ('accessdate', models.CharField(db_column='AccessDate', max_length=255, unique=True)),
                ('educationalresources_resourceid', models.ForeignKey(db_column='EducationalResources_ResourceID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.educationalresources')),
                ('user_user', models.ForeignKey(db_column='User_User_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.user')),
            ],
            options={
                'db_table': 'userresourceaccess',
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('user_role_id', models.IntegerField(db_column='User_role_ID', primary_key=True, serialize=False)),
                ('user_id', models.CharField(db_column='User_ID', max_length=255, unique=True)),
                ('role_role', models.ForeignKey(db_column='Role_Role_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.role')),
            ],
            options={
                'db_table': 'user_roles',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='user_roles_user_role',
            field=models.ForeignKey(db_column='User_Roles_User_role_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='base.userroles'),
        ),
    ]