def Get_Victim_Count(p_value):
  
  l_count = 0
  try:
    p_input = str(p_value)
    print(p_input)
    l_count = str(p_input).count('Victim')

    
    #s = gpc.get_participant_count(p_type,'Suspect')
  except Exception as e:
    print(e)
    q = l_count

  return l_count