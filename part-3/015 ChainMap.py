d1, d2, d3
d = {**d1, **d2, **d3} # if collision, the last key will override

d = {}
d.update(d1)
d.update(d2)
d.update(d3)

# it is wasteful, duplicating a lot of data to a new dictionary
# chainmap
# chainmap is not a subclass of dictionary !!!!!
# chainmap order is not guaranteed in iteration !!!!
# if collision, first in first out, when found first one, it stops iteration

# chainmap can handle insert, update and delete
# insert goes to first dictionary
# mutation only goes to the first dictionary, otherwise create a new key in the first dict
# delete only goes to the first dictionary, otherwise KeyError


# when change the original dictionary, for example d3['x']=500
d['x'] ->500 # d is chainmap, chainmap get can the new one
# like the views, all the references to the dictionary, when dictionary changes, the views reflect that change.

# order matters in chainmap
d = ChainMap(d1,d2) # same as below
d = d.new_child(d3) # d3 is the first dict
d.parents -> # return d2 and d3 in chainmap

#
type(d.maps), d.maps -> list, [d3,d1,d2]
d.maps.append(d3) -> # d3 goes to the end
del d.maps[0] # d will also change, so can use this to change the chainmap instead of using approaches above

********************************************************************************************************************************************************
# application case: change dictioanry but want to restore the original dict later. we can use chainmap
# configuration setting
# idea: always mutate the first dict, so it is safe saved as the 2nd dict. will never be modified.
config = {
          'host': 'xxx',
          'port': 5432,
          'database':'deep',
          'user_id':'xxx',
          'user_pwd':'xxx'
}

local_config = ChainMap({},config)
list(local_config.items())
local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'
list(local_config.items())
local_config -> will see new settings goes to the first dict
config -> still have the original settings, no change



