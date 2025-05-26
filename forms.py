from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, file_allowed, FileAllowed, file_size, FileSize
from wtforms.fields import StringField,IntegerField,SubmitField,PasswordField,RadioField,DateField,SelectField
from wtforms.validators import  DataRequired,length,equal_to

class AddProductforms(FlaskForm):
     name= StringField("ჩაწერეთ დასამატებელი პროდუქტის  სახელი",validators=[DataRequired()])
     price= IntegerField("ჩაწერეთ პროდუქტის ფასი",validators=[DataRequired()])
     img=FileField("აირჩიეთ ფაილი",validators=[DataRequired(),
                                                    FileAllowed(["png","jpg","jpeg"], message="მისაღებია სურათები მხოლოდ შემდეგი ფორმატით:JPG,PNG,JPEG"),
                                                    FileSize(1024 * 1024 * 5,message="ფაილი უნდა იყოს მაქსიმუმ 5 მეგაბაიტი")
                                                   ])
     submit=SubmitField("დამატება")


class Registration(FlaskForm):
    username=StringField("ჩაწერეთ თქვენი სახელი",validators=[DataRequired()])
    password=PasswordField("შეიყვანეთ პაროლი",validators=[length(min=8,max=65,message="პაროლი მინიმუმ უნდა შედგებოდეს 8 სიმბოლოსგან")])
    repeat_password=PasswordField("გაიმეორეთ პაროლი",validators=[
                                                               DataRequired(),
                                                               equal_to("password",message="პაროლები ერთმანეთს არ ემთხვევა")])
    gender=RadioField("აირჩიეთ სქესი",choices=["მამაკაცი", "მანდილოსანი"],validators=[DataRequired()])
    birthday= DateField("შეიყვანეთ დაბადების თარიღი",validators=[DataRequired()])
    country=SelectField("მონიშნეთ ქვეყანა: ",choices=["საქართველო","გერმანია","სომხეთი","აზერბაიჯანი","ჩინეთი","თურქეთი","ესპანეთი"],validators=[DataRequired()])
    submit=SubmitField("რეგისტრაცია")

class New_Password(FlaskForm):
      username=StringField("ჩაწერეთ მომხმარებლის სახელი",validators=[DataRequired()])
      new_password=PasswordField("შეიყვანეთ ახალი პაროლი",validators=[DataRequired(),length(min=8,max=32,message="პაროლი უნდა შეიცავდეს მინიმუმ 8 სიმბოლოს")])
      submit = SubmitField("დადასტურება")
class Loginform(FlaskForm):
    username=StringField("ჩაწერეთ მომხმარებლის სახელი",validators=[DataRequired()])
    password=PasswordField("შეიყვანეთ პაროლი",validators=[
                                                     DataRequired(),
                                                     length(min=8,max=32,message="პაროლი არასწორია")])
    submit=SubmitField("ავტორიზაცია")