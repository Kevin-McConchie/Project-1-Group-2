import get_participant_count as gpc

def get_participant_count(p_value):
  

  try:
    p_input = str(p_value)
    p_type = p_input.split("||")

    q = gpc.get_participant_count(p_type,'Victim')

    
    #s = gpc.get_participant_count(p_type,'Suspect')
  except Exception as e:
    print(e)
    q = 0

  return q