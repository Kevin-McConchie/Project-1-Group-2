def get_participant_count(participant_types, p_function_type):
  l_victim_count  = 0    
  l_suspect_count = 0
 
  try:
    l_range = str(participant_types).count(',')+1
    print(f"l_range : {l_range}")
    print(f"participant_types : {participant_types}")
    
    for z in range(l_range):
        val1 = participant_types[z]          

        if 'Victim' in val1:
          l_victim_count +=1
        else:
          l_suspect_count +=1  

    if p_function_type == 'Victim':
      return l_victim_count
    else:
      return l_suspect_count 
  except Exception as e:    
    print(f"get_participant_count {e}")