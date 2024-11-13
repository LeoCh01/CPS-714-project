# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authenticationlogs(models.Model):
    log_id = models.IntegerField(db_column='log_ID', primary_key=True)  # Field name made lowercase.
    login_time_timestamp = models.CharField(unique=True, max_length=255)
    success = models.IntegerField(unique=True)
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'authenticationlogs'


class Chatlogs(models.Model):
    chatid = models.IntegerField(db_column='ChatID', primary_key=True)  # Field name made lowercase.
    message = models.TextField(db_column='Message')  # Field name made lowercase.
    created_at = models.DateField(db_column='Created_AT')  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'chatlogs'


class Educationalresources(models.Model):
    resourceid = models.IntegerField(db_column='ResourceID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', unique=True, max_length=100)  # Field name made lowercase.
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    resourcetype = models.CharField(db_column='ResourceType', unique=True, max_length=255)  # Field name made lowercase.
    dateadded = models.CharField(db_column='DateAdded', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'educationalresources'


class Loyaltypoints(models.Model):
    pointsid = models.IntegerField(db_column='PointsID', primary_key=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=300)  # Field name made lowercase.
    #loyaltyrewards_rewardid = models.ForeignKey('Loyaltyrewards', models.DO_NOTHING, db_column='LoyaltyRewards_RewardID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'loyaltypoints'


class Loyaltyrewards(models.Model):
    rewardid = models.IntegerField(db_column='RewardID', primary_key=True)  # Field name made lowercase.
    rewarddescription = models.CharField(db_column='RewardDescription', unique=True, max_length=255)  # Field name made lowercase.
    pointsrequired = models.CharField(db_column='PointsRequired', unique=True, max_length=255)  # Field name made lowercase.
    redemptiondate = models.DateField(db_column='RedemptionDate', unique=True)  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'loyaltyrewards'


class Multiplechoiceoption(models.Model):
    optionposition = models.IntegerField(db_column='OptionPosition', primary_key=True)  # Field name made lowercase.
    optiontext = models.CharField(db_column='OptionText', unique=True, max_length=255)  # Field name made lowercase.
    #question_surveyposition = models.ForeignKey('Question', models.DO_NOTHING, db_column='Question_SurveyPosition')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'multiplechoiceoption'


class Multiplechoicequestion(models.Model):
    maxselectionnumber = models.IntegerField(db_column='MaxSelectionNumber', unique=True)  # Field name made lowercase.
    #question_surveyposition = models.ForeignKey('Question', models.DO_NOTHING, db_column='Question_SurveyPosition')  # Field name made lowercase.
    #surveys_survey = models.ForeignKey('Surveys', models.DO_NOTHING, db_column='Surveys_Survey_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'multiplechoicequestion'


class Multiplechoiceresponse(models.Model):
    selectedoption = models.IntegerField(db_column='SelectedOption', unique=True)  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.
    #surveys_survey = models.ForeignKey('Surveys', models.DO_NOTHING, db_column='Surveys_Survey_ID')  # Field name made lowercase.
    #question_surveyposition = models.ForeignKey('Question', models.DO_NOTHING, db_column='Question_SurveyPosition')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'multiplechoiceresponse'


class Products(models.Model):
    productid = models.IntegerField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', unique=True, max_length=255)  # Field name made lowercase.
    #tickets_ticket = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='Tickets_Ticket_ID')  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'products'


class Purchasehistory(models.Model):
    purchaseid = models.IntegerField(db_column='PurchaseID', primary_key=True)  # Field name made lowercase.
    purchasedate = models.DateField(db_column='PurchaseDate', unique=True)  # Field name made lowercase.
    pointsearned = models.CharField(db_column='PointsEarned', unique=True, max_length=45)  # Field name made lowercase.
    pointsredeemed = models.CharField(db_column='PointsRedeemed', unique=True, max_length=45)  # Field name made lowercase.
    totalspent = models.DecimalField(db_column='TotalSpent', unique=True, max_digits=65, decimal_places=0)  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'purchasehistory'


class Question(models.Model):
    surveyposition = models.IntegerField(db_column='SurveyPosition', primary_key=True)  # Field name made lowercase.
    questiontext = models.CharField(db_column='QuestionText', unique=True, max_length=255)  # Field name made lowercase.
    #surveys_survey = models.ForeignKey('Surveys', models.DO_NOTHING, db_column='Surveys_Survey_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'question'


class Rewardredemption(models.Model):
    redemptionid = models.IntegerField(db_column='RedemptionID', primary_key=True)  # Field name made lowercase.
    redemptiondate = models.DateField(db_column='RedemptionDate')  # Field name made lowercase.
    #rewards_reward = models.ForeignKey('Rewards', models.DO_NOTHING, db_column='Rewards_reward_ID')  # Field name made lowercase.
    #loyaltyrewards_rewardid = models.ForeignKey(Loyaltyrewards, models.DO_NOTHING, db_column='LoyaltyRewards_RewardID')  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'rewardredemption'


class Rewards(models.Model):
    reward_id = models.IntegerField(db_column='reward_ID', primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', unique=True)  # Field name made lowercase.
    reward_date_timestamp = models.CharField(db_column='reward_Date_timestamp', unique=True, max_length=255)  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'rewards'


class Role(models.Model):
    role_id = models.PositiveIntegerField(db_column='Role_ID', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(unique=True, max_length=45)

    class Meta:
        # managed = False
        db_table = 'role'


class SurveyResponse(models.Model):
    survey_response_id = models.IntegerField(db_column='Survey_Response_ID', primary_key=True)  # Field name made lowercase.
    survery_id = models.CharField(db_column='Survery_ID', unique=True, max_length=255)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', unique=True, max_length=255)  # Field name made lowercase.
    response_text = models.CharField(db_column='Response_text', max_length=1000)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'survey_response'


class Surveys(models.Model):
    survey_id = models.IntegerField(db_column='Survey_ID', primary_key=True)  # Field name made lowercase.
    #survey_response_survey_response = models.ForeignKey(SurveyResponse, models.DO_NOTHING, db_column='Survey_Response_Survey_Response_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'surveys'


class Textualquestion(models.Model):
    charlimit = models.IntegerField(db_column='CharLimit')  # Field name made lowercase.
    #question_surveyposition = models.ForeignKey(Question, models.DO_NOTHING, db_column='Question_SurveyPosition')  # Field name made lowercase.
    #surveys_survey = models.ForeignKey(Surveys, models.DO_NOTHING, db_column='Surveys_Survey_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'textualquestion'


class Textualresponse(models.Model):
    responsetext = models.CharField(db_column='ResponseText', unique=True, max_length=1000)  # Field name made lowercase.
    #question_surveyposition = models.ForeignKey(Question, models.DO_NOTHING, db_column='Question_SurveyPosition')  # Field name made lowercase.
    #surveys_survey = models.ForeignKey(Surveys, models.DO_NOTHING, db_column='Surveys_Survey_ID')  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'textualresponse'


class TicketResponse(models.Model):
    ticket_response_id = models.IntegerField(db_column='Ticket_Response_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    response_text = models.CharField(db_column='Response_text', max_length=255, blank=True, null=True)  # Field name made lowercase.
    responded_at = models.CharField(db_column='Responded_at', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #tickets_ticket = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='Tickets_Ticket_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'ticket_response'


class Tickets(models.Model):
    ticket_id = models.IntegerField(db_column='Ticket_ID', primary_key=True)  # Field name made lowercase.
    ticket_status = models.CharField(db_column='Ticket_status', unique=True, max_length=255)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', unique=True, max_length=255)  # Field name made lowercase.
    created_at = models.CharField(db_column='Created_at', max_length=255)  # Field name made lowercase.
    ticket_text = models.CharField(db_column='Ticket_text', max_length=1000)  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tickets'


class Transactions(models.Model):
    transactionid = models.IntegerField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    #user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.
    #loyaltypoints_pointsid = models.ForeignKey(Loyaltypoints, models.DO_NOTHING, db_column='LoyaltyPoints_PointsID')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'transactions'


class User(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_Password', unique=True, max_length=255)  # Field name made lowercase.
    #ticket_response_ticket_response = models.ForeignKey(TicketResponse, models.DO_NOTHING, db_column='Ticket_response_Ticket_Response_ID')  # Field name made lowercase.
    #user_roles_user_role = models.ForeignKey('UserRoles', models.DO_NOTHING, db_column='User_Roles_User_role_ID')  # Field name made lowercase.
    #survey_response_survey_response = models.ForeignKey(SurveyResponse, models.DO_NOTHING, db_column='Survey_Response_Survey_Response_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'user'


class UserRoles(models.Model):
    user_role_id = models.IntegerField(db_column='User_role_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', unique=True, max_length=255)  # Field name made lowercase.
    #role_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='Role_Role_ID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'user_roles'


class Userresourceaccess(models.Model):
    accessid = models.IntegerField(db_column='AccessID', primary_key=True)  # Field name made lowercase.
    accessdate = models.CharField(db_column='AccessDate', unique=True, max_length=255)  # Field name made lowercase.
    #user_user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.
    #educationalresources_resourceid = models.ForeignKey(Educationalresources, models.DO_NOTHING, db_column='EducationalResources_ResourceID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'userresourceaccess'
