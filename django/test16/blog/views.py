#coding:utf8
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from blog.models import Customer,Types,Foods,LineItem
from blog.form import CustomerForm
import hashlib

def index_view(req,id):
    dict_return = {}
    types_list = Types.objects.all()
    dict_return['types'] = types_list
    foods = []
    if id == "":
        dict_return['pagename'] = '首页'
        for each in types_list:
            foods.append(each.foods_set.all()[0])
    else:
        thetype = Types.objects.get(id=id)
        foods = thetype.foods_set.all()
        dict_return['pagename'] = thetype.foodtype
    dict_return['foods'] = foods
    req.session['id'] = id
    if req.session.has_key('user'):
        user = req.session['user']
        dict_return['user'] = user
        return render(req,'index_view.html',dict_return)
    else:
        return render(req,'index.html',dict_return)


def regist_view(req):
    if req.method == "POST":
        cf = CustomerForm(req.POST)
        if cf.is_valid():
            try:
                Customer.objects.get(username = cf.instance.username)
                cf = CustomerForm()
                return render(req,'regist_view.html',{'cf':cf})
            except:
                cf.instance.password = hashlib.sha1(cf.cleaned_data['password']).hexdigest()
                cf.save()
                return HttpResponseRedirect('/login/')
    else:
        cf = CustomerForm()
        return render(req,'regist_view.html',{'cf':cf})


def login_view(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        try:
            user = Customer.objects.get(username ="cuiyanan",password=hashlib.sha1(password).hexdigest())
            req.session['user'] = user
        except:
            pass
    return HttpResponseRedirect('/index/')



def logout_view(req):
    del req.session['user']
    return HttpResponseRedirect('/index/')

class Cart(object):
    def __init__(self,*args,**kwargs):
        self.items = []
        self.total_price = 0
    def add_food(self,food):
        self.total_price += food.foodprice
        for item in self.items:
            if item.food.id == food.id:
                item.quantity += 1
                return
        self.items.append(LineItem(food = food,quantity=1))
def choose(req,id):
    food = Foods.objects.get(id=id)
    cart = req.session.get('cart',None)
    if not cart:
        cart = Cart()
    cart.add_food(food)
    req.session['cart'] = cart
#    for item in cart.items:
#        print item.food
    return HttpResponseRedirect('/index/%s'%req.session['id'])

def clearing(req):
    cart = req.session.get('cart',None)
    user = req.session.get('user',None)
    if not cart:
        cart = Cart()
    types_list = Types.objects.all()
    if not user:
        return HttpResponseRedirect('/index/')
    return render(req,'clearing.html',{'user':user,'cart':cart,'types':types_list})


def confirm(req):
    pass

def cleancart(req):
    cart = req.session.get('cart',None)
    if cart:
        del req.session['cart']
        cart = None
    user = req.session.get('user',None)
    types_list = Types.objects.all()
    return render_to_response('clearing.html',{'cart':cart,'user':user,'types':types_list})
    cart = None
