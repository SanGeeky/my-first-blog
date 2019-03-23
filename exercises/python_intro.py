# name = 'Sasdasdas'
# if name == 'Ola':
#     print('Hey Ola!')
# elif name == 'Sonja':
#     print('Hey Sonja!')
# else:
#     print('Hey anonymous!')

# Cambiar el volumen si esta muy alto o muy bajo
# volume = 57
# if volume < 20:
#     print("It's kinda quiet.")
# elif 20 <= volume < 40:
#     print("It's nice for background music")
# elif 40 <= volume < 60:
#     print("Perfect, I can hear all the details")
# elif 60 <= volume < 80:
#     print("Nice for parties")
# elif 80 <= volume < 100:
#     print("A bit loud!")
# else:
#     print("Me duelen las orejas! :(")


# def hi(name):
#     if name == 'Ola':
#         print('Hi Ola!')
#     elif name == 'Sonja':
#         print('Hi Sonja!')
#     else:
#         print('Hi anonymous!')
#
# hi('Feo')
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')


for i in range(1, 6):
    print(i)
