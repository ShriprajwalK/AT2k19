from django.shortcuts import render, redirect
from .models import Company
from users.models import Profile
from .forms import BuyForm, SellForm
from django.core.exceptions import ValidationError


#views.home
def home(request):
    context = {
    'details': Company.objects.all()  #Sending data so that the html template can use it.
    }
    with open('/home/the_daemon_lord/Share_Market/current.txt','w') as f:
        s = ""
        for i in Company.objects.all():
            l=i
            s+=str(l.name)+" "+str(l.current_price)+" "+str(l.percentage_change)+"\n"
        f.writelines(s)


    #This particular file structure is required in django, although it may seem weird.
    return render(request,'stock_price/home.html',context)#go to stock_price/templates/stock_price/home.html.


def graph(request):
    context = {
    'detail' : Company.objects.all()
    }
    return render(request,'stock_price/graph.html',context)


def about(request):
    return render(request,'stock_price/about.html')


def buy(request):
    form = BuyForm(request.POST or None)

    if request.method == "POST":
        #form = BuyForm(request.POST)

        username = None
        if request.user.is_authenticated:
            username = request.user.username

        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            ct = 0

            for i in Company.objects.all():
                l = i
                if name ==l.name:
                    ct+=1
                    k = i
            b = Profile.objects.get(user__username=username)
            if ct==0:
                raise ValidationError('Invalid Name')

            elif k.current_price*amount > Profile.objects.get(user__username=username).money_possesed:
                raise ValidationError('Not enough money')



            else:
                if name == "Tesla(Phase2)":
                    b.Tesla_stock += amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "TataMotors":
                    b.TataMotors_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "Nissan":
                    b.Nissan_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "JPMorganChase":
                    b.JPMorgan_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "SunPharma":
                    b.SunPharma_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "GSK-Pfizer":
                    b.GSKPfizer_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "Nestle":
                    b.Nestle_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()

                elif name == "BHEL":
                    b.BHEL_stock+=amount
                    b.money_possesed -= k.current_price*amount
                    b.save()


            return redirect('stockhome')


    return render(request,'stock_price/buy.html',{'form':form})


def sell(request):

    form = SellForm(request.POST or None)

    if request.method == "POST":

        username = None
        if request.user.is_authenticated:
            username = request.user.username

        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            ct = 0

            for i in Company.objects.all():
                l = i
                if name ==l.name:
                    ct+=1
                    k = i
            b = Profile.objects.get(user__username=username)

            if ct==0:
                raise ValidationError(('Invalid Name'))



            elif name == "Tesla(Phase2)":
                if b.Tesla_stock< amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Tesla_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            elif name == "TataMotors":
                if b.TataMotors_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.TataMotors_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            elif name == "Nissan":
                if b.Nissan_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Nissan_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()



            elif name == "JPMorganChase":
                if b.JPMorgan_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.JPMorgan_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            elif name == "SunPharma":
                if b.SunPharma_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.SunPharma_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "GSK-Pfizer":
                if b.GSKPfizer_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.GSKPfizer_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "Nestle":
                if b.Nestle_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.Nestle_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()

            elif name == "BHEL":
                if b.BHEL_stock<amount:
                    raise ValidationError(("You don't have that many stocks"))
                else:
                    b.BHEL_stock -= amount
                    b.money_possesed += k.current_price*amount
                    b.save()


            return redirect('stockhome')

    return render(request,'stock_price/sell.html',{'form':form})
