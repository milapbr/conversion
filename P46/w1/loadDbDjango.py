def change_phone(username, new_phone, phone_ext):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    if not user:
        raise Exception("User not found")
    profile = user.get_profile()
    if not profile:
        raise Exception("Profile not found")
    print "User ID: ", user.id
    print "Username: ", user.username
    print "Email: ", user.email
    print "Name:", user.first_name, user.last_name
    print "Profile ID: ", profile.id
    print "Old phone: ", profile.phone
    profile.phone = new_phone
    profile.extension = phone_ext
    profile.save()
 
change_phone("kmorgan", '1-800-727-7672', '3917')
change_phone("cheryl", '1-800-727-7672', '3918')
change_phone("rochelle", '1-800-727-7672', '3919')
change_phone("stephanie", '1-800-727-7672', '3920')


'''
User ID:  90
Username:  kmorgan
Email:  kmorgan@rmsa.com
Name: Kristina Morgan
Profile ID:  90
Old phone:  951-878-5136
User ID:  10
Username:  cheryl
Email:  cpowell@rmsa.com
Name: Cheryl Powell
Profile ID:  10
Old phone:  951-878-0969
User ID:  16
Username:  rochelle
Email:  rtoledo@rmsa.com
Name: Rochelle Toledo
Profile ID:  16
Old phone:  949-522-5153
User ID:  64
Username:  stephanie
Email:  slewis@rmsa.com
Name: Stephanie Lewis
Profile ID:  64
Old phone:  800-727-7672
'''