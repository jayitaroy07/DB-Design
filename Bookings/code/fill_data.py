
def func():
    from management.models import *

    f = open('/Users/jayitaroy/Downloads/Contacts.csv')
    l = f.readlines()[1:]

    for line in l:
        list_line = line.strip().split()
        cid = int(list_line[0])
        fname = list_line[1]
        mname = list_line[2]
        lname = list_line[3]
        new_contact = contact(contact_id=cid, fname=fname, mname=mname, lname=lname)
        new_contact.save()
        home_phone = list_line[4]
        cell_phone = list_line[5]
        work_phone = list_line[10]
        if home_phone:
            new_phone = phone(contact_id=cid, phone_type='home', area_code='+1', number=home_phone)
            new_phone.save()
        if work_phone:
            new_phone = phone(contact_id=cid, phone_type='work', area_code='+1', number=work_phone)
            new_phone.save()
        if cell_phone:
            new_phone = phone(contact_id=cid, phone_type='cell', area_code='+1', number=cell_phone)
            new_phone.save()

        home_address = list_line[6]
        home_city = list_line[7]
        home_state = list_line[8]
        home_zip = list_line[9]

        if home_address or home_city or home_state or home_zip:
            new_address = address(contact_id=cid, address_type='home', address=home_address, city=home_city, state=home_state, zip=home_zip)
            new_address.save()
        
        work_address = list_line[11]
        work_city = list_line[12]
        work_state = list_line[13]
        work_zip = list_line[14]

        if work_address or work_city or work_state or work_zip:
            new_address = address(contact_id=cid, address_type='work', address=work_address, city=work_city, state=work_state, zip=work_zip)
            new_address.save()

        date = list_line[15]

        if date:
            new_date = date(contact_id=cid, date_type='birthdate', date=date)
            new_date.save()
        


