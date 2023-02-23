mail= input('Enter mail: ').strip().lower()

name= mail[:mail.find('@')]
provider= mail[mail.find('@')+1:mail.find('.')]
domain= mail[mail.find('.')+1:]

print(f'"Your name is {name}"')
print(f'"Your provider is {provider}"')
print(f'"Your domain is {domain}"')