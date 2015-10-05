#!/usr/bin/env python
# http://codegolf.stackexchange.com/questions/49671/do-you-want-to-code-a-snowman

# Input string: HNLRXYTB
# H is for Hat
# N is for Nose/Mouth
# L is for Left Eye
# R is for Right Eye
# X is for Left Arm
# Y is for Right Arm
# T is for Torso
# B is for Base

#  HHHHH
#  HHHHH
# X(LNR)Y
# X(TTT)Y
#  (BBB)


def print_snowman(pattern):
    # Hats
    hats = [
        ' _===_ ',
        '  ___  \n'
        ' ..... ',
        '   _   \n'
        '  /_\  ',
        '  ___  \n'
        ' (_*_) ']

    # Noses
    noses = [
        ',',
        '.',
        '_',
        ' ']

    # Left and Right Eyes
    eyes = [
        '.',
        'o',
        'O',
        '-'
    ]

    # Left Arms
    left_arms = [
        '<',
        '\\',
        '/',
        ' ']

    # Right Arms
    right_arms = [
        '>',
        '/',
        '\\',
        ' ']

    # Torsos
    torsos = [
        ' : ',
        '] [',
        '> <',
        '   ']

    # Bases
    bases = [
        ' : ',
        '" "',
        '___',
        '   ']


    hat = int(pattern[0]) - 1
    nose = int(pattern[1]) - 1
    left_eye = int(pattern[2]) - 1
    right_eye = int(pattern[3]) - 1
    left_arm = int(pattern[4]) - 1
    right_arm = int(pattern[5]) - 1
    torso = int(pattern[6]) - 1
    base = int(pattern[7]) - 1

    # Hat
    snowman = hats[hat] + '\n';

    # Top Section
    if left_arm == 1:
        snowman += left_arms[1]
    else:
        snowman += ' '
    snowman += '('
    snowman += eyes[left_eye]
    snowman += noses[nose]
    snowman += eyes[right_eye]
    snowman += ')'
    if right_arm == 1:
        snowman += right_arms[1]
    else:
        snowman += ' '
    snowman += '\n';

    # Middle Section
    if left_arm != 1:
        snowman += left_arms[left_arm]
    else:
        snowman += ' '
    snowman += '('
    snowman += torsos[torso]
    snowman += ')'
    if right_arm != 1:
        snowman += right_arms[right_arm]
    else:
        snowman += ' '
    snowman += '\n';

    # Bottom Section
    snowman += ' ('
    snowman += bases[base]
    snowman += ')'

    print snowman + "\n***********\n"


# Test with different patterns
print_snowman("11114411")
print_snowman("33232124")
print_snowman("14441133")
print_snowman("22323242")
print_snowman("11111343")