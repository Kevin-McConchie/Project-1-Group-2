from ast import Return
import pandas as pd


def process_data(p_incident, p_types, p_genders,p_status,p_age_groups,p_file_name,p_debug):

    print("p_file_name started")

    df_type         = pd.DataFrame(columns=['incident_number', 'participant_number','data_value'])
    df_gender       = pd.DataFrame(columns=['incident_number', 'participant_number','data_value'])
    df_status       = pd.DataFrame(columns=['incident_number', 'participant_number','data_value'])
    df_age_groups   = pd.DataFrame(columns=['incident_number', 'participant_number','data_value'])

    # ********************************************************** *#

    incident_series = pd.Series(p_incident)
    type_series     = pd.Series(p_types)
    gender_series   = pd.Series(p_genders)
    status_series   = pd.Series(p_status)
    age_series      = pd.Series(p_age_groups)


    frame = { 'Incident': incident_series, 'Participant Types': type_series, 'Gender':gender_series, 'Status' : status_series, 'AgeGrpup' :age_series }
    merged_df = pd.DataFrame(frame)

    # ********************************************************** *#
    # ************ PARTICIPANT TYPE START *********************** 
    

    for ind in merged_df.index:

        # Looping through each merged df row
        # Print each element
        if p_debug == True:
            print("***********************************************************")
            print("")
            print("")
            print("Index   : " + str(ind))
            print("Incident ID   : " + str(merged_df['Incident'][ind]))
            print("Participant Type   : " + merged_df['Participant Types'][ind])
            print("Participant Type   : " + merged_df['Participant Types'][ind])
            print("Participant Status : " + merged_df['Status'][ind])
            print("Participant Age Grp : " + merged_df['AgeGrpup'][ind])
            print("")
        
        # ################################################################# #
        # Start of PARTICIPANT TYPE process
        # ################################################################# #

        p_types =  merged_df['Participant Types'][ind]

        if str(p_types).count('||') != 0:
            d_list = str(p_types).split('||')    

            try:
                for x in range(len(d_list)):    #for each participant type sub list
                
                    if str(d_list[x]).count('::') != 0:
                        d_sublist = str(d_list[x]).split('::')   
                    elif str(d_list[x]).count(':') != 0:     
                        d_sublist = str(d_list[x]).split(':')   
                    else:
                        print("Error 100: Exception with string parse type. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_number = str(d_sublist[0])
                    d_value = str(d_sublist[1])    
                    
                    df_type = df_type.append({'incident_number': merged_df['Incident'][ind],  
                                              'participant_number':d_participant_number, 
                                              'data_value':d_value}, ignore_index=True)
            
            except Exception as a:
                print("Error 200: Exception with Participant Types. Incident number: "+str( merged_df['Incident'][ind]))    



        elif str(p_types).count('|') != 0:  

            d_list = str(p_types).split('|')    
                     

            try:
                for x in range(len(d_list)):    #for each participant type sub list
                
                    if str(d_list[x]).count('::') != 0:
                        d_sublist = str(d_list[x]).split('::')   
                    elif str(d_list[x]).count(':') != 0:     
                        d_sublist = str(d_list[x]).split(':')   
                    else:
                        print("Error 100: Exception with string parse type. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_number = str(d_sublist[0])
                    d_value = str(d_sublist[1])    
                    
                    df_type = df_type.append({'incident_number': merged_df['Incident'][ind],  
                                              'participant_number':d_participant_number, 
                                              'data_value':d_value}, ignore_index=True)
            
            except Exception as a:
                print("Error 200: Exception with Participant Types. Incident number: "+str( merged_df['Incident'][ind]))    
        
        else: #If the input has only one element, the first split doesnt work and the list is not created. 

            d_list = str(p_types)  

            if str(d_list).count('::') != 0:
                str2 = "::"  
            
            elif str(d_list).count(':') != 0:     
                str2 = ":"  

            try:
                l_separator = d_list.find(str2)+1

                d_participant_number    = d_list[:1]
                d_value                 = d_list[l_separator+1:len(d_list)-l_separator+2]
        
                df_type                 = df_type.append({'incident_number': merged_df['Incident'][ind],  
                                                          'participant_number':d_participant_number, 
                                                          'data_value':d_value}, ignore_index=True)

            except Exception as a:
                print("Error 300: Exception with Participant Types. Incident number: "+str( merged_df['Incident'][ind]))    

       

        # ################################################################# #
        # End of PARTICIPANT TYPE process
        # ################################################################# #

# *********************************************************************************************************** #

        # ################################################################# #
        # Start of STATUS process
        # ################################################################# #

        
        p_status =  merged_df['Status'][ind] 

        if str(p_status).count('||') != 0:
            d_status = str(p_status).split('||')   


            try:
                for x in range(len(d_status)):    #for each participant type sub list
                    

                    if str(d_status[x]).count('::') != 0:
                        d_sublist_status = str(d_status[x]).split('::')    
                    elif str(d_status[x]).count(':') != 0:     
                        d_sublist_status = str(d_status[x]).split(':')    
                    else:
                        print("ERROR 400: Exception with string parse status. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_status = str(d_sublist_status[0])
                    d_value_status = str(d_sublist_status[1])
                        
                    
                    df_status = df_status.append({'incident_number': merged_df['Incident'][ind],  
                                                  'participant_number':d_participant_status, 
                                                  'data_value':d_value_status}, ignore_index=True)

            except Exception as a:
                print("ERROR 500: Exception with Status. Incident number: "+str( merged_df['Incident'][ind]))    
        


        elif str(p_status).count('|') != 0:     
            d_status = str(p_status).split('|')    

            try:
                for x in range(len(d_status)):    #for each participant type sub list
                    

                    if str(d_status[x]).count('::') != 0:
                        d_sublist_status = str(d_status[x]).split('::')    
                    elif str(d_status[x]).count(':') != 0:     
                        d_sublist_status = str(d_status[x]).split(':')    
                    else:
                        print("ERROR 400: Exception with string parse status. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_status = str(d_sublist_status[0])
                    d_value_status = str(d_sublist_status[1])
                        
                    
                    df_status = df_status.append({'incident_number': merged_df['Incident'][ind],  
                                                  'participant_number':d_participant_status, 
                                                  'data_value':d_value_status}, ignore_index=True)

            except Exception as a:
                print("ERROR 500: Exception with Status. Incident number: "+str( merged_df['Incident'][ind]))    
       
        
        else:
            d_status = str(p_status)


            if str(d_status).count('::') != 0:
                str2 = "::"  
            
            elif str(d_status).count(':') != 0:     
                str2 = ":"  

            try:
                l_separator = d_status.find(str2)+1

                d_participant_status    = d_status[:1]
                d_value_status          = d_status[l_separator+1:len(d_status)-l_separator+2]
        
                df_status = df_status.append({'incident_number': merged_df['Incident'][ind],  
                                                  'participant_number':d_participant_status, 
                                                  'data_value':d_value_status}, ignore_index=True)

            except Exception as a:
                print("Error 600: Exception with Participant Status. Incident number: "+str( merged_df['Incident'][ind]))    

       
        # ################################################################# #
        # End of of STATUS process
        # ################################################################# #

# *********************************************************************************************************** #

        # ################################################################# #
        # Start of AGE GROUP process
        # ################################################################# #


        p_age_group =  merged_df['AgeGrpup'][ind]
        
        if str(p_age_group).count('||') != 0:
            d_age_group = str(p_age_group).split('||')    


            try:
                for x in range(len(d_age_group)):    #for each participant type sub list
                        

                    if str(d_age_group[x]).count('::') != 0:
                        d_sublist_age = str(d_age_group[x]).split('::')    
                    elif str(d_age_group[x]).count(':') != 0:     
                        d_sublist_age = str(d_age_group[x]).split(':')    
                    else:
                        print("Error 700: Exception with string parse age group. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_age = str(d_sublist_age[0])
                    d_value_age = str(d_sublist_age[1])
                        
                    
                    df_age_groups = df_age_groups.append({'incident_number': merged_df['Incident'][ind],  'participant_number':d_participant_age, 'data_value':d_value_age}, ignore_index=True)
            except Exception as a:
                print("Error 800: Exception with Age Group. Incident number: "+str( merged_df['Incident'][ind]))    




        elif str(p_age_group).count('|') != 0:     
            d_age_group = str(p_age_group).split('|')    
                
            try:
                for x in range(len(d_age_group)):    #for each participant type sub list
                        

                    if str(d_age_group[x]).count('::') != 0:
                        d_sublist_age = str(d_age_group[x]).split('::')    
                    elif str(d_age_group[x]).count(':') != 0:     
                        d_sublist_age = str(d_age_group[x]).split(':')    
                    else:
                        print("Error 700: Exception with string parse age group. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_age = str(d_sublist_age[0])
                    d_value_age = str(d_sublist_age[1])
                        
                    
                    df_age_groups = df_age_groups.append({'incident_number': merged_df['Incident'][ind],  'participant_number':d_participant_age, 'data_value':d_value_age}, ignore_index=True)
            except Exception as a:
                print("Error 800: Exception with Age Group. Incident number: "+str( merged_df['Incident'][ind]))    

        else:
            d_age_group = str(p_age_group)  

            if str(d_age_group).count('::') != 0:
                str2 = "::"  
            
            elif str(d_age_group).count(':') != 0:     
                str2 = ":"  

            try:
                l_separator = d_age_group.find(str2)+1

                d_participant_age = d_age_group[:1]
                d_value_age       = d_age_group[l_separator+1:len(d_age_group)-l_separator+2]
        
                df_age_groups = df_age_groups.append({'incident_number': merged_df['Incident'][ind],  'participant_number':d_participant_age, 'data_value':d_value_age}, ignore_index=True)
            except Exception as a:
                print("Error 900: Exception with Age Group parse for single value. Incident number: "+str( merged_df['Incident'][ind]))    



        # ################################################################# #
        # End of of AGE GROUP process
        # ################################################################# #

# *********************************************************************************************************** #

        # ################################################################# #
        # Start of GENDER process
        # ################################################################# #



        p_gender =  merged_df['Gender'][ind]
        
        if str(p_gender).count('||') != 0:
            d_gender = str(p_gender).split('||')    

            try:
                for x in range(len(d_gender)):    #for each participant type sub list
                        

                    if str(d_gender[x]).count('::') != 0:
                        d_sublist_gender = str(d_gender[x]).split('::')    
                    elif str(d_gender[x]).count(':') != 0:     
                        d_sublist_gender = str(d_gender[x]).split(':')    
                    else:
                        print("Error 1000: Exception with string parse age group. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_gender = str(d_sublist_gender[0])
                    d_value_gender = str(d_sublist_gender[1])
                        
                    
                    df_gender = df_gender.append({'incident_number': merged_df['Incident'][ind],  
                                                  'participant_number':d_participant_gender, 
                                                  'data_value':d_value_gender}, ignore_index=True)
            except Exception as a:
                print("Error 1100: Exception with GENDER. Incident number: "+str( merged_df['Incident'][ind]))    



        elif str(p_gender).count('|') != 0:     
            d_gender = str(p_gender).split('|')    
                
            try:
                for x in range(len(d_gender)):    #for each participant type sub list
                        

                    if str(d_gender[x]).count('::') != 0:
                        d_sublist_gender = str(d_gender[x]).split('::')    
                    elif str(d_gender[x]).count(':') != 0:     
                        d_sublist_gender = str(d_gender[x]).split(':')    
                    else:
                        print("Error 1000: Exception with string parse age group. Incident number: "+str( merged_df['Incident'][ind]))    
                        pass   

                    d_participant_gender = str(d_sublist_gender[0])
                    d_value_gender = str(d_sublist_gender[1])
                        
                    
                    df_gender = df_gender.append({'incident_number': merged_df['Incident'][ind],  
                                                  'participant_number':d_participant_gender, 
                                                  'data_value':d_value_gender}, ignore_index=True)
            except Exception as a:
                print("Error 1100: Exception with GENDER. Incident number: "+str( merged_df['Incident'][ind]))    

        else:
            d_gender = str(p_gender)  

            if str(d_gender).count('::') != 0:
                str2 = "::"  
            
            elif str(d_gender).count(':') != 0:     
                str2 = ":"  

            try:
                l_separator = d_gender.find(str2)+1

                d_participant_gender = d_gender[:1]
                d_value_gender       = d_gender[l_separator+1:len(d_gender)-l_separator+2]
        
                df_gender = df_gender.append({'incident_number': merged_df['Incident'][ind],  
                                                  'participant_number':d_participant_gender, 
                                                  'data_value':d_value_gender}, ignore_index=True)


            except Exception as a:
                print("Error 1200: Exception with Age Group parse for single value. Incident number: "+str( merged_df['Incident'][ind]))    


# *********************************************************************************************************** #

        # ################################################################# #
        # FINAL PROCESS MERGING, INDEXING ETC
        # ################################################################# #

    df_type.reset_index
    df_status.reset_index
    df_age_groups.reset_index
    df_gender.reset_index

    if p_debug == True:
        print("df_type")
        print(df_type.head())

        print("df_status")
        print(df_status.head())

        print("df_age_groups")
        print(df_age_groups.head())

        print("df_gender")
        print(df_gender.head())

    df2 = pd.merge(df_type, df_status, on=['incident_number','participant_number'], how = "outer",suffixes=('_x', '_y'))
    df2_1 = pd.merge(df2, df_age_groups, on=['incident_number','participant_number'], how = "outer", suffixes=('z', 'q'))
    df2_2 = pd.merge(df2_1, df_gender, on=['incident_number','participant_number'], how = "outer",suffixes=('a', 'b'))


    
    column_names = ['incident_id','No','Type','Status','Age Group','Gender']
    df2_2.columns = column_names
    
    file_location = f"resource/{p_file_name}.csv"
    print("file_location : "+file_location)
    #df2_2.to_csv("resource/processed_data.csv", index=False, header=True)  
    df2_2.to_csv(file_location, index=False, header=True)        
    print("*********************************************")
    return 1
    