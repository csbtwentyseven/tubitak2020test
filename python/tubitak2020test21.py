from firebase import firebase

firebase = firebase.FirebaseApplication('https://tubitak2020test3.firebaseio.com/', None)

veri = input("İsim girniz:")
firebase.put('/message','message',veri)
print('Record Updated')
