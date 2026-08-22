def checker(card_num):
    
    if "-" in card_num:
        card = card_num.replace("-", "")
    elif " " in card_num:
        card = card_num.replace(" ", "")
    else:
        card = card_num

    length = len(card)
    test_1 = card[::-1]
    
    num_sum = 0
    isSecond = False
    
    for i in range(0, length):
        d = ord(test_1[i]) - ord('0')
        
        if isSecond:
            d = d*2
        
        num_sum += d // 10
        num_sum += d % 10
    
        isSecond = not isSecond
    
    if num_sum % 10 == 0:
        return "The card is valid"
    else:
        return "card is invalid"

a = checker('453914889')
print(a)
    
