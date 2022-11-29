from django import template

register = template.Library()

@register.filter()
def censor(value):
   forbidden_words = ['богатый', 'историю,', 'арбуз', 'мира', 'сборных', "переработка"]
   if not isinstance(value, str):
      raise TypeError(f"unresolved type '{type(value)}' expected type 'str' ")
   for word in value.split():
      if word.lower() in forbidden_words:
         value = value.replace(word, f"{word[0]}{'*' * (len(word)-1)}")
   return value
