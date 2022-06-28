
from email.quoprimime import quote
#add apostrophes when using quotes

first_name="Friedrich"
last_name="Nietzche"
full_name=f"{first_name} {last_name}"
quote=f'{full_name.title()} once said, "That which does not kill us makes us stronger."'
print(quote)