


#kocha="Bog'bon"
#mahalla="Sag'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#print(kocha , " ko'chasi" , mahalla , " mahallasi", tuman, " tumani", viloyat, " viloyati")

#print("Iltimos, ma'lumotlarni to'liq kiriting")
#kocha=input("Ko'changizni kiriting: ")
#mahalla=input("Mahallangizni kiriting: ")
#tuman=input("Tumaningizni kiriting: ")
#viloyat=input("Viloyatingizni kiriting: ")
#print(kocha , " kochasi,\n ", mahalla , " mahallasi,\n ", tuman, " tumani,\n ", viloyat, " viloyati")

#kocha="Bog'bon"
#mahalla="Sag'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
#print(manzil.capitalize())

#a = 20
#b = 5.5
#temp =36.6
#aholi_soni = 7_564_367_986
#print("Aholi soni: " , aholi_soni)

#x, y, z = 10, 5.5, -56

#c=a*b

#d=100/2 # type float o'nlik ya'ni butun bo'lmagan sonlar

#f=100//2 # type int butun sonlar

#x = int(input("Son kiriting: "))
#print( x,"ning kvadrati",x ** 2, "ga teng" )
#print(x, "ning kubi",x ** 3, "ga teng")
#z = int(x**3)
#print(x,"ning kvadrati ",y , "ga teng ")
#print(x,"ning kubi ", z, "ga teng")

#yosh=int(input("Yoshingizni kiriting: "))
#yil=2021-yosh
#print("Siz " , yil , " yilda tug'ilgansiz")

#x = int(input("Son kiriting: "))
#y = int(input("Son kiriting: "))
#print(x,"+",y,"=", x+y,"ga teng")
#print(x,"-",y,"=",x-y,"ga teng")
#print(x,"*",y,"=",x*y,"ga teng")
#print(x,":",y,"=",x/y,"ga teng")

#ismlar = ['Jamshid', 'Mirkamol', 'Javohir']
#print(ismlar)
#print('Assalomu alaykum va rohmatullohi va barokatuh' , ismlar[2] , 'bugun choyxona bormi?')

#sonlar = [2 , 25 , 69 , -63 , 3.6 ]
#sonlar = sonlar[0] + 12
#sonlar = sonlar[3] - 63
#sonlar = sonlar[4] * 2
#sonlar = sonlar[1] / 5
#sonlar [-1] = 66
#sonlar.append(6)
#sonlar.insert(0,23)
#print(sonlar)

#t_shaxslar = ["Muhammad sollalohu alayhi vasallam" , "Amir Temur" , "Abdulhamid" ]
#z_shaxslar = ["Elon Musk" , "Bill Gates" , "Abdulloh domla"] 
#print('Men tarixiy shaxslardan ',t_shaxslar.pop(0),"bilan suhbat qilgan bo'lardim","Zamonaviy shaxslardan esa",z_shaxslar.pop(2),"bilan suhbat qilgan bo'lardim")

#friends=[]
#friends.append('Abror')
#friends.append('Jamshid')
#friends.append('Mirkamol')
#friends.append('Javohir')
#print(friends)
#friends.remove('Mirkamol')
#friends.remove('Abror')
#print(friends)
#friends.append('Ilhom')
#friends.insert(0,'Siroj')
#friends.insert(2,'Samandar')
#print(friends)

#dostlar=['siroj','jamshid','samandar','abror']
#mehmonlar= []
#mehmonlar.append(dostlar.pop(0))
#print(mehmonlar)

#cars=['bmw','audi','toyota','mazda','gm','lexus']
#cars.sort()
#print(sorted(cars))
#print(sorted(cars,reverse=True))
#cars.reverse()
#print(len(cars))

#sonlar=list(range(1,20))
#print(sonlar)
#t_sonlar = list(range(1,20,2))
#print(t_sonlar)
#j_sonlar=list(range(0,20,2))
#print(j_sonlar)
#sonlar_2=list(range(10,101,10))
#print(sonlar_2)

#narxlar = [5,3,7,9,6,4026,32598,48632]
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami_summa= sum(narxlar)
#print("Eng arzon narxdagi mahsulot:", arzon,"Eng qimmat narxdagi mahsulot:",qimmat,"Jami mahsulotlarning narxi:",jami_summa)
#kesish
#print(narxlar[0:3])
#print(narxlar[:5])#boshidan kiritilgan indexgacha
#print(narxlar[4:])#kiritilgan indexdan oxirigacha

#nusxa
#my_cars = narxlar[:]# nusxa olish belgisi
#my_cars.remove(7)
#narxlar.insert(2,6)
#print(my_cars)
#print(narxlar)

#toys = ('teddy','snake','dina','alex')
#toys = list(toys)
#toys.append('momiqvoy')
#toys = tuple(toys)
#type(toys)
#print(toys)

#davlatlar = ['Uzb', 'Rus', 'Usa', 'Albaniya', 'Turkiya']
#print(sorted(davlatlar,reverse=True))
#davlatlar.reverse()
#davlatlar.sort()
#davlatlar.sort(reverse=True)
#j_sonlar = list(range(120,1200))
#kichik = min(j_sonlar)
#katta = max(j_sonlar)
#print(katta - kichik)
#print(len(j_sonlar))
#print(j_sonlar[0:20])
#print(j_sonlar[530:550])
#print(j_sonlar[-20:])
#print(sum(j_sonlar))

#taomlar = ['sut', 'osh', 'somsa', 'bulochka', "bo'tqa"]
#nonushta = taomlar[:]
#nonushta.remove('osh')
#nonushta.remove('somsa')
#nonushta.append('kofe')
#nonushta.insert(0, 'shakolad')
#print(nonushta)
#print(taomlar)

# FOR SIKLI
#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
#for mehmon in mehmonlar:
   # print("Assalomu alaykum va rohmatulloh",mehmon)
    #print('Hayr',mehmon)
  
#mehmonlar = ['Ali','Vali','Hasan','Husan']
##for mehmon in mehmonlar:
  #   print(f"Hurmatli {mehmon} sizni tabriklaymiz")
   #  print('Hurmat bilan Ucell companiyasi')

#sonlar = list(range(1,11))
#for son in sonlar:
 #   print(f"{son} ning kvadrati {son**2} ga teng")

#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
 #   sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("5ta do'stingizni kiriting")
#for n in range(5):
 #   dostlar.append(input(f"{n+1}-nchi do'stingizni kiriting: "))
#print(dostlar)

#Homework

#ismlar = ['ali', 'vali', 'olim' ,'hasan', 'husan']
#for ism in ismlar:
 #   print('salom',ism)
#print(f"Ko'd {len(ismlar)}-marta takrorlandi")
  
#t_sonlar = list(range(11,100,2))
#for sonlar in t_sonlar:
 #   print(f"{sonlar}-nining kubi {sonlar**3}")

#kinolar = []    
#print("Sevimli kinolaringizni kiriting")   
#for n in range(5):
 #   kinolar.append(input(f"{n+1}-nchi sevimli kinoingizni kiriting: "))
#print(kinolar)    

# IF ELSE TARMOQLANISH

#avtolar = ['bmw', 'audi', 'toyota', 'lada', 'mazda']
#for avto in avtolar:
#    if avto == 'bmw':
  #      print(avto.upper())
 ##   else:
 #       print(avto.title())

#ism = 'Ali'
#ism.lower() == 'ali'

#ism = input("Ismingizni kiriting?\n>>>")
#if ism.lower() != 'ali':
#    print(f"Uzr,{ism.title()} biz Alini kutyapmiz")
#else:
    #print("Assalomu alaykum Ali")

#javob = float(input("12x6 kopaytirsa nechiga teng?"))
#if javob != 72:
 #   print('javob xato')

#yosh = int(input("Yoshingizni kiriting:\n>>>")) 
#if yosh >=18:
 #   print("Xush kelibsiz")
#else:
 #   print('Kirishingiz mumkin emas')  

#login = input("Yangi login kiriting:")
#if len(login) <=5:
 #   print("Login 5 harfdan ko'p bo'lishi kerak")

#yil = int(input("Tug'ilgan yilingizni kiriting:\n>>>"))
#if 2021-yil <18:
  #  print(f"Sizning yoshingiz {2020-yil}-da ekan")
 #   print("Sizga bu saytga kirish mumkin emas")
#else:
    #print("Xush kelibsiz bizning saytimizga")    

#yosh = int(input("Yoshingiz nechida:\n>>>"))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

#x,y = 25,50
#print("x>y") if x>y else print("x<y")

#Homework

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#cars = ['toyota', 'mazda', 'gm', 'kia', 'hundai']
#for car in cars:
 #   if car == 'gm':
  #      print(car.upper()) 
   # else:
    #    print(car.title())          
 
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.    
#cars = ['toyota', 'kia', 'mazda', 'gm', 'hundai'] 
#for car in cars:
 #  if car != 'gm':
  #     print(car.title())
   #else:
    #   print(car.upper())
     
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring. 
#login = input("Loginigizni kiriting: ")
#if login.lower() == 'admin':
 #   print("Xush kelibsiz Admin,Foydalanuvchilar ro'yxatini ko'rasizmi")
#else:
 #   print(f"Xush kelibsiz {login}")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
#x = input("Birinchi sonni kiriting: ")
#y = input("Ikkinchi sonni kiriting: ")
#if x==y:
 #   print(f"{x}={y} ikkisi teng ")
#else:
  #  print(f"{x}={y} ikkisi teng emas")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
#x = int(input("Son kiriting: "))
#if x<=0:
 #   print(f"{x}-Manfiy son")
#else:
 #   print(f"{x}-Musbat son")


# if elif else
#yosh = int(input("Yoshingizni kiriting: "))
#if yosh<=4:
   # narx = 0
#elif yosh<=12:
 #   narx = 5000    
#else:
 #   narx = 10000

#print(f"Sizga kirish {narx} so'm")    
 
# or=yoki, and=va   
#kun = input("Bugun nima kun?>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
 #   print('Bugun dam olish kuni')
#else:
 #   print('Bugun ish kuni')

#kun = input("Bugun nima kun? ")
#harorat = float(input("Havo harorati qanday? "))
#if kun.lower()=='yakshanba' and harorat>=30:
 #   print("Cho'milgani ketdik")
#elif kun.lower()=='yakshanba' and harorat<30:
 #   print("Bugun uyda dam olamiz")    

#kun = input("Bugun nima kun? ")
#harorat = float(input("Havo harorati qanday? "))
#if(kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
 #   print("Cho'milishga ketdik")
#elif(kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
 #   print('Bugun dam olamiz')

#boolean
#narx = 15000
#choy = True   
#salat = False
#if choy and salat:
 #   narx = narx + 10000
#elif choy or salat:
 #   narx = narx + 5000
#print(f"Jami {narx} so'm")    
    
#narx = 20000
#choy = 1
#non = 1
#kompot = 1
#assorti = 0
#kola = 0
#if choy:
 #   narx = narx + 2000
  #  print("Mijoz choy sotib oldi")
#if non:
 #   narx = narx + 3000
  #  print("Mijoz non sotib oldi")
#if kompot:
 #   narx = narx + 4000
  #  print("Mijoz kompot sotib oldi")
#if assorti:
 #   narx = narx + 30000
   # print("Mijoz assorti sotib oldi")
#if kola:
 #   narx = narx + 10000
  #  print("Mijoz kola sotib oldi")

#print(f"Jami {narx} so'm")

# in, not in 
#menu = ['somsa', 'manti', 'osh', 'shashlik', 'norin']
#chiq = 'osh' in menu
#print(chiq)

#menu = ['osh', 'somsa', 'norin', 'kabob']
#ovqat = input('Nima ovqat yemoqchisiz?>>>')
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi")
#else:
 #   print("Afsuski bizda bunday ovqat yo'q")

#menu = ['osh', 'somsa', 'norin', 'kabob']
#ovqat = input("Nima ovqat yeysiz?>>>")
#if ovqat.lower() not in menu:
 #   print("Afsuski bizda bunday ovqat yo'q")
#else:
#    print("Buyurtmangiz qabul qilindi")

##menu = ['osh', 'mosh', 'qozonkabob', 'shashlik', 'chuchvora', 'baliq']
#buyurtmalar = ['somsa', 'salat', 'oliviya', 'osh', 'shashlik']
#if buyurtmalar:
 # for taom in buyurtmalar:
  #  if taom in menu:
   #     print(f"Menuda {taom} bor")
    #else:
     #   print(f"Menuda {taom} yo'q")

#HOMEWORK
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
#son = int(input("Son kiriting:>>>"))
#if son%2:
 #   print("juft emas")
#else:
 #   print("raxmat")    
  

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#yosh = int(input("Yoshingizni kiriting: "))   
#if yosh<=4 or yosh >=60:
 #   narx = 0
#elif yosh < 18:
 #   narx = 5000
#else:
 #   narx = 10000
#print(f"Sizga kirish {narx} so'm")    
    
#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

#x = int(input("Birinchi sonni kiriting: "))
#y = int(input("Ikkinchi sooni kiriting: "))
#if x==y:
 #   print(f"{x}={y}")
#elif x>y:
 #   print(f"{x}>{y}")
#else:
 #   print(f"{x}<{y}")
    
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

#mahsulotlar = ['olma', 'nok', 'non', 'piyoz', 'kartoshka', 'sabzi', "o'rik", 'qaymoq' ]
#savat = []
#for n in range(5):
 #   savat.append(input(f"{n+1}-mahsulotni kiriting: "))
#for mahsulot in savat:
 #   if mahsulot in mahsulotlar:
  #      print(f"Bizning do'konimizda {mahsulot} bor")
   # else:
    #    print(f"Bizning do'konimizda {mahsulot} yo'q")
        
#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.  
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
              # 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


#savat = []
#for n in range(5):
 #   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
 #   if mahsulot in mahsulotlar:
  #      bor_mahsulotlar.append(mahsulot)
   # else:
    #    mavjud_emas.append(mahsulot)

#if mavjud_emas:
 # print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  ## print(mahsulot)
#else:
 # print("Siz so'ragan barcha mahsulotlar do'konimizda bor") 
    
 
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring
#users = ['ok', 'pass', 'odno', 'bek', 'tesla']
#login = input("Yangi login kiriting: ")
#if login in users:
 #   print("Login band yangi login tanlang")
#else:
    #print(f"Xush kelibsiz ")    

#son = int(input("Son kiriting: "))
#for n in range (2,11):
 #   if not (son%n):
  #      print(f"{son} soni {n} ga qoldiqsiz bo'linadi")










