# упражнение 1
import unicodedata
mystery = '\U0001f4a9'
print(mystery)
print( unicodedata.name(mystery) )
# упражнение 2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
# упражнение 3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
# упражнение 4
poets = 'My kitty cat likes %s,\n'      % ('roast beef') + \
        'My kitty cat likes %s,\n'      % ('ham') + \
        'My kitty cat fell on his %s\n' % ('head') + \
        'And now thinks he\'s a %s.'  % ('clam')
print(poets)
# упражнение 5
letter = 'Dear {salutation} {name},\n' + \
         'Thank you for your letter. We are sorry that our {product} {verbed} in your\n' + \
         '{room}. Please note that it should never be used in a {room}, especially\n' + \
         'near any {animals}.\n' + \
         'Send us your receipt and {amount} for shipping and handling. We will send\n' + \
         'you another {product} that, in our tests, is {percent} less likely to\n' + \
         'have {verbed}.\n' + \
         'Thank you for your support.\n' + \
         'Sincerely,\n' + \
         '{spokesman}\n' + \
         '{job_title}\n'
print(letter)
# упражнение 6
response = {
    'salutation': '1',
    'name': '2',
    'product': '3',
    'verbed': '4',
    'room': '5',
    'animals': '6',
    'amount': '7',
    'percent': '8',
    'spokesman': '9',
    'job_title': '10',
}
print(letter.format(**response))
# упражнение 7
mammoth = 'We have seen thee, queen of cheese,\n' + \
          'Lying quietly at your ease,\n' + \
          'Gently fanned by evening breeze,\n' + \
          'Thy fair form no flies dare seize.\n' + \
          'All gaily dressed soon you\'ll go\n' + \
          'To the great Provincial show,\n' + \
          'To be admired by many a beau\n' + \
          'In the city of Toronto.\n' + \
          'Cows numerous as a swarm of bees,\n' + \
          'Or as the leaves upon the trees,\n' + \
          'It did require to make thee please,\n' + \
          'And stand unrivalled, queen of cheese.\n' + \
          'May you not receive a scar as\n' + \
          'We have heard that Mr. Harris\n' + \
          'Intends to send you off as far as\n' + \
          'The great world\'s show at Paris.\n' + \
          'Of the youth beware of these,\n' + \
          'For some of them might rudely squeeze\n' + \
          'And bite your cheek, then songs or glees\n' + \
          'We could not sing, oh! queen of cheese.\n' + \
          'We\'rt thou suspended from balloon,\n' + \
          'You\'d cast a shade even at noon,\n' + \
          'Folks would think it was the moon\n' + \
          'About to fall and crush them soon.\n'
# упражнение 8
import re
print( re.findall(r'\bc\w*', mammoth) )
# упражнение 9
print( re.findall(r'\bc\w{3}\b', mammoth) )
# упражнение 10
print( re.findall(r'\b[\w\']*r\b', mammoth) )
# упражнение 11
print( re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth) )
# упражнение 12
import binascii
before_gif = '47494638396101000100800000000000ffffff21f9' + \
             '0401000000002c000000000100010000020144003b'
print( binascii.unhexlify(before_gif) )
# упражнение 13
# gif[:6] == b'GIF89a'

