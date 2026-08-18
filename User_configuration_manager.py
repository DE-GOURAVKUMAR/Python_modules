test_settings = {'theme': 'light', 'notifications': 'enabled', 'volume': 'high'}
new_settings = ('theme', 'dark')

def add_setting(dict_of_settings, setting_tuple):
    
    # Convert the key and value to lowercase.
    k, v = setting_tuple
    k_low = str(k).lower()
    v_low = str(v).lower()
    
    if k_low in dict_of_settings:
        return f"Setting '{k_low}' already exists! Cannot add a new setting with this name."
    
    if k_low not in dict_of_settings:
        dict_of_settings[k_low] = v_low
            
    return f"Setting '{k_low}' added with value '{v_low}' successfully!"


def update_setting(dict_of_settings, setting_tuple):
    k, v = setting_tuple
    ku_low = str(k).lower()
    vu_low = str(v).lower()

    if ku_low in dict_of_settings:
        dict_of_settings.update({ku_low: vu_low})
        return f"Setting '{ku_low}' updated to '{vu_low}' successfully!"

    if ku_low not in dict_of_settings:
        return f"Setting '{ku_low}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_of_settings, key):
    
    key_low = str(key).lower()

    if key_low in dict_of_settings:
        dict_of_settings.pop(key_low, None)
        return f"Setting '{key_low}' deleted successfully!"
    if key_low not in dict_of_settings:
        return "Setting not found!"

def view_settings(dict_of_settings):
    if not dict_of_settings:
        return "No settings available."

    if dict_of_settings:
        new_text = "\n".join([f"{k.capitalize()}: {v}" for k, v in dict_of_settings.items()])
        return f"Current User Settings:\n{new_text}\n" 
            

update_setting(test_settings, new_settings)
print(test_settings)