stick_list = [3,3,3,3,34,4,4,4,4,4,2,0,0,]



def clean(stick_list):
    print stick_list
    stick_list = filter(lambda x: x != 0, stick_list)
    print len(stick_list)
    print "DONE CLEANING"
    return stick_list

def cut(stick_list):
    if len(stick_list) >  0:
        popped_number = stick_list.pop(stick_list.index(min(stick_list)))
        print "cutting number is: ", popped_number
        print "length of list", len(stick_list)
        print stick_list
        new_list = [i - popped_number for i in stick_list if i - popped_number != 0]
        cut(new_list)
    else:
        pass


stick_list = clean(stick_list)
cut(stick_list)
