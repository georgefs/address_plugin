#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george 
#
# Distributed under terms of the MIT license.
import data

def form_str(value):
    try: 
        value = value.encode('utf-8')
    except:
        pass
    return value


def get_city(address):
    address = form_str(address)

    for city in data.cityList:
        if address.find(city['name']):
            return city


def get_town(address):
    address = form_str(address)

    city = get_city(address)
    import pdb;pdb.set_trace()
    
    for town in data.townList[int(city['id'])]:
        if address.find(town['name']):
            return {"city":city, "town":town}


    return city

