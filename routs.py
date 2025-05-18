from itertools import product
from flask_login import login_user,logout_user,login_required,current_user
from extentions import  app,db
from flask import render_template, redirect
from os import path
from forms import AddProductforms,Registration,Loginform
from models import Product,User







@app.route("/login",methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        if current_user.role !="admin":
          return redirect("/")

    form=Loginform()
    if form.validate_on_submit():
        user=User.query.filter(User.username==form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            return redirect("registration")
    return render_template("login.html",form=form,)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/category/<int:category_id>")
def category(category_id):
    products=Product.query.filter(Product.category_id ==category_id).all()
    return render_template("index.html",product=products)

@app.route("/products/<int:index>",methods=["POST","GET"])

def produt(index):
    prod=Product.query.get(index)
    return render_template("products.html",product=prod)

@app.route("/search/<string:name>",methods=["GET","POST"])
def search(name):
    products=Product.query.filter(Product.name.ilike(f"%{name}%")).all()
    return render_template("search.html",product=products)



@app.route("/")
def home():
    products=Product.query.all()

    return render_template("index.html",product=products)

@app.route("/addproducts",methods=["GET","POST"])
@login_required
def addProductforms():
    if current_user.role != "admin":
        return redirect("/")
    form=AddProductforms()
    if form.validate_on_submit():
        new_product=Product(name=form.name.data,price=form.price.data,img=form.img.data.filename)
        db.session.add(new_product)
        db.session.commit()

        file_dir=path.join(app.root_path,"static",form.img.data.filename)
        form.img.data.save=(file_dir)

        return redirect("/")
    print(form.errors)
    return render_template("addproductforms.html",forms=form)



@app.route("/delete/<int:index>")
@login_required
def delt(index):
    if current_user.role != "admin":
        return redirect("/")
    product=Product.query.get(index)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")
@app.route("/edit_product/<int:index>",methods=["GET","POST"])
@login_required
def edit(index):
    if current_user.role != "admin":
        return redirect("/")
    product=Product.query.get(index)
    form=AddProductforms(name=product.name,price=product.price,img=product.img)
    if form.validate_on_submit():
        product.name=form.name.data
        product.price=form.price.data
        product.img=form.img.filename
        db.session.commit()


        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save = (file_dir)
        return redirect("/")
    print(form.errors)
    return  render_template("editfile.html",forms=form)


@app.route("/registration",methods=["GET","POST"])
def reg():
    regi=Registration()
    if regi.validate_on_submit():
        user = User(username=regi.username.data, password=regi.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    print(regi.errors)
    return render_template("registration_forms.html",regist=regi)

@app.route("/about_us")
def about():
    return render_template("about_us.html")