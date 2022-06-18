from numpy import dtype


def get_participant_count(participant_types, p_function_type):
  l_victim_count  = 0    
  l_suspect_count = 0
  l_return = []
 
  try:
    l_range = len(participant_types)
    
    for z in range(l_range):

            
      try:
          if p_function_type == 'Victim':            
            l_return.append(str(participant_types[z]).count('Victim') )  
          elif 'Suspect' in p_function_type:
            l_return.append(str(participant_types[z]).count('Suspect') )  
      
    
      except Exception as e:    
          print(f"get_participant_count exception1 {e}")
          


  except Exception as e:    
    print(f"get_participant_count exception2 {e}")
    l_return.append(0)
 
  return l_return 