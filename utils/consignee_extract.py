import re
from typing import Optional, Dict, Union

def parse_string_to_dict(input_string: str) -> Optional[Dict[str, Union[Dict[str, str], str]]]:
    """
    Parse a string to extract information and return it as a dictionary.

    Parameters:
    - input_string (str): The input string containing information in a specific format.

    Returns:
    - Optional[Dict[str, Union[Dict[str, str], str]]]: A dictionary containing the extracted information,
      with keys 'cleaned_address_breakdown' and 'id'. If extraction fails, returns None.

    Example:
    >>> input_str = "cleaned_address_breakdown={'key': 'value'}, id=123"
    >>> parse_string_to_dict(input_str)
    {'cleaned_address_breakdown': {'key': 'value'}, 'id': '123'}
    """

    # Extract cleaned_address_break_down and id using regular expressions
    
    name_match = re.search(r'name=(.*?),', input_string)
    cleaned_address_breakdown_match = re.search(r'cleaned_address_breakdown=({.*?})', input_string)
    id_match = re.search(r'id=([a-z0-9]+)', input_string)

    if cleaned_address_breakdown_match:
        # Extracted matches
        cleaned_address_breakdown_str = cleaned_address_breakdown_match.group(1)
        
         # Convert cleaned_address_breakdown to a dictionary
        cleaned_address_breakdown_dict = dict(item.strip().split('=') for item in cleaned_address_breakdown_str.strip('{}').split(','))
    else: 
         cleaned_address_breakdown_dict = None
        
    if id_match:
        id_value = id_match.group(1)
    else:
        id_value = None
    
    if name_match:
        name_value = name_match.group(1)
        

       
        # Create the final result dictionary
        result_dict = {
            'name': name_value,
            'cleaned_address_breakdown': cleaned_address_breakdown_dict,
            'id': id_value
        }

        return result_dict
    else:
        print("Error: Unable to extract the required information from the input string.")
        return None
