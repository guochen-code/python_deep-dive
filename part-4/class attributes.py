# retrieve attribute value from objects
# getattr function
# getattr(object_symbol, attribute_name, optional_default)
getattr(MyClass, 'language')
getattr(MyClass, 'x') -> AttributeError exception
getattr(MyClass, 'x', 'N/A') -> 'N/A'

# dot notation (shorthand)
MyClass.language # no default option here

# set attribute values in objects
# setattr(object_symbol, attribute_name, attribute_value)
setattr(MyClass, 'version', '3.7')
MyClass.version = '3.7'

# what happens if we call setattr for an attribute we did not define in our class?
python is a dynamic language -> can modify our classes at runtime

# where is the state store? -> in a dictionary (also called class namespace, it is read-only)
MyClass.__dict__ -> mappingproxy (not dict type, but still dictionary, a hash map, read-only hash map)
# python ensure all the keys in the class are strings
# that's why all our attribute names are considered strings
# modify the content of the namespace indirectly by using the setattr()

# delete attributes
delattr(obj_symbol, attribute_name)
del <keyword>
delattr(MyClass, 'version')
del MyClass.version

# caveat
MyClass.language
getattr(MyClass,'language')
MyClass.__dict__['language'] # not always, some attributes not stored in this dict !!!!!!




