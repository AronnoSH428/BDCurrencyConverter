import pyttsx3
friend = pyttsx3.init()
friend.setProperty("rate", 120)
friend.setProperty('volume', 100)
friend.say("Welcome sir,This is a python programme created by Bangladeshi young programmer Shahriar,"
           "   It will help you to convert any Bangladeshi money Amount in Taka to any  other currency,"
            "Please Enter your amount in Taka")
friend.runAndWait()



#You can add many values here .but don't forget to keep them in this dictoionary
currenDict = {
'Pound':  '0.0088',
'Euro':  '0.0097',
'Swiss':  '0.0104',
'Dollar':  '0.0118',
'AusDollar': '0.0156',
'Yuan' : '0.077',
'Ruble' : '0.865',
'Rupee':  '0.866',
'Yen':  '1.22 ',
"Iranian rial":"0.002",
"Indonesian rupiah":"0.006",
"Korean won":"0.0775",
"Chilean peso":"0.1154",
"Nigerian naira":"0.2225",
"Hungarian forint":"0.291",
"Sri Lanka rupee":"0.4536",
"Pakistan rupee":"0.5285",
"Algerian dinar":"0.6432",
"Iceland krona":"0.6648",
"Japanese yen":"0.8194",
"Serbian dinar":"0.8797",
"Argentine peso":"1.027",
"Russian ruble":"1.152",
"Philippine peso":"1.765",
"Thai baht": "2.826",
"Taiwan dollar":"3.016",
"Ukraine hryvnia":"3.049",
"Czech koruna":"3.948",
"Mexican peso":"4.249",
"Egyptian pound":"5.399",
"South african rand":"5.701",
"Norwegian krone":"9.767",
"Swedish krona":"10.16",
"Turkish lira":"10.85",
"Hong kong dollar":"10.94",
"Chinese yuan renminbi":"12.98",
"Brazilian real":"16.59",
"Malaysian ringgit":"20.92",
"Saudi riyal":"22.61",
"Un. arab emirates dirham":"23.09",
"Qatari rial":"23.3",
"Israeli new shekel":"26.09",
"Singapore dollar":"63.8"
}
#print(type(currenDict['Pound']))
friend.runAndWait()


#main function

try:
  #main function
 amount = abs(int(input('Please Enter Your amount in taka : \n')))
 print('available options are : \n')
 [print(item) for item in currenDict.keys()]
 friend.say("Enter one of these currencies in which you want to convert your amount : ")
 friend.runAndWait()
 currency = str(input('Enter one of these currencies in which you want to convert your amount : \n'))
 friend.say(f"{amount} taka is equal to {amount*float(currenDict[currency])} {currency}")
 print(f"{amount} taka is equal to {amount*float(currenDict[currency])} {currency}")
 friend.say("Thank u sir ,WE Hope that you Have Enjoyed this programme Have a nice day sir!!!!!")
 friend.runAndWait()

except:
   friend.say("Sorry sir Plesae check your submitted value again Otherwise,This might me a technical fault or "
              "Your desired tool is not available right now "
              "We are Extremely sorry for your inconvience"
              " Have a nice day sir ")
   friend.runAndWait()

finally:
    print("Have a nice day sir !!!!")


