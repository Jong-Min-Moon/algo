def pldr(sent):
    forward_idx = 0
    backward_idx = len(sent) - 1

    while forward_idx <= backward_idx:
        while not sent[forward_idx].isalpha():
            forward_idx += 1
        forward_char = sent[forward_idx].lower()
        print(forward_char)

        while not sent[backward_idx].isalpha():
            backward_idx -= 1
        backward_char = sent[backward_idx].lower()
        print(backward_char)
        if forward_char != backward_char:
            return False

        forward_idx +=1
        backward_idx -=1
    return True

print(pldr('Wow'))
print(pldr("Madam, I'm Adam."))
print(pldr('madam, I am Adam.'))