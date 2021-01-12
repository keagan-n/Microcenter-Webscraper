def handlerHigh(dict,itemName,itemPrice):
    if dict[itemName] < itemPrice:
        dict[itemName]=itemPrice + " (highest price for duplicates)"
    else:
        dict[itemName] = dict[itemName] + " (highest price for duplicates)"


def handlerLow(dict,itemName,itemPrice):
    if dict[itemName] > itemPrice:
        dict[itemName] = itemPrice + " (lowest price for duplicates)"
    else:
        dict[itemName] = dict[itemName] + " (lowest price for duplicates)"