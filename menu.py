# -*- coding: utf-8 -*-

from datetime import datetime


def date():
    return "%s/%s/%s" % (now.day, now.month, now.year)



with open("menu.txt", "w+") as menu_file:
    now = datetime.now()
    print "%s\nThe daily menu:  " % date()
    menu_file.write("%s\nThe daily menu:  " % date())
    dish = raw_input("Enter the dish please:\n>> ")
    print "The dish for today is \" %s \" " % dish
    price = int(raw_input("Enter the price of the %s:\n>>" % dish))
    print "%s costs %s" % (dish, price)
    menu_file.write("\n\n%s:  %s,-" % (dish, price))

