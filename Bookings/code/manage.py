#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def func():

    f = open('/Users/jayitaroy/Downloads/Contacts.csv')
    l = f.readlines()[1:]

    for line in l:
        list_line = line.strip().split(',')
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
            new_phone = phone(contact_id=new_contact, phone_type='home', area_code='+1', number=home_phone)
            new_phone.save()
        if work_phone:
            new_phone = phone(contact_id=new_contact, phone_type='work', area_code='+1', number=work_phone)
            new_phone.save()
        if cell_phone:
            new_phone = phone(contact_id=new_contact, phone_type='cell', area_code='+1', number=cell_phone)
            new_phone.save()

        home_address = list_line[6]
        home_city = list_line[7]
        home_state = list_line[8]
        home_zip = list_line[9]

        if home_address or home_city or home_state or home_zip:
            new_address = address(contact_id=new_contact, address_type='home', address=home_address, city=home_city, state=home_state, zip=home_zip)
            new_address.save()
        
        work_address = list_line[11]
        work_city = list_line[12]
        work_state = list_line[13]
        work_zip = list_line[14]

        if work_address or work_city or work_state or work_zip:
            new_address = address(contact_id=new_contact, address_type='work', address=work_address, city=work_city, state=work_state, zip=work_zip)
            new_address.save()

        date_birth = list_line[15]

        if date_birth:
            new_date = date(contact_id=new_contact, date_type='birthdate', date=date_birth)
            new_date.save()
        




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bookings.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    # from management.models import *
    # func()
