from dataset_module import load_dataset 
from query_module import QueryModule, save_to_csv, save_records_to_csv

def user_interface():
    
    #loads the data
    dataset = load_dataset("data.csv")
    qm = QueryModule(dataset)

    #Asks for user name
    u_name = input("Please input your name: ")

    #if name is not an alphabet, keep asking
    while not u_name.isalpha():
        print("Wrong input")
        u_name =input("Please input your name: ").strip()


    print(f'''\nWelcome {u_name} to the Stroke Analytics Application\n
          Please find below the various options for the subgroup analytics.\n
          A Smokers with Hypertension resulting in stroke.\n
          B Heart diseases that leads to stroke.\n
          C Hypertension resulting in stroke and those not resulting in stroke based on genders.\n
          D Smoking habits that resulted in stroke an smoking habits that did not result in stroke.\n
          E Areas and their resulting stroke analysis.\n
          F Stroke and Dietary analysis.\n
          G Hypertension resulting in stroke.\n
          H Details of people whose hypertension did and did not result in stroke.\n
          I Details of people whose heart dieases resulted in stroke.\n
          J Descriptive statistics of each features.\n
          K Average sleep hours of people with stroke and those without.\n
          L Exit.\n''')
    maps ={
            'A': ("Smokers with Hypertension resulting in stroke.", qm.smoke_n_hypertension), 
            'B':("Heart diseases that leads to stroke.", qm.heart_disease_lead_to_stroke),
            'C': ("Hypertension resulting in stroke and those not resulting in stroke based on genders.",qm.gender_hypertension),
            'D':("Smoking habits that resulted in stroke an smoking habits that did not result in stroke.",qm.smoking_stroke_occurrence),
            'E':("Areas and their resulting stroke analysis.",qm.area_stroke),
            'F':("Stroke and Dietary analysis.",qm.Dietary_n_stroke),
            'G':("Hypertension resulting in stroke",qm.stroke_n_hypertension),
            'H': ("Details of people whose hypertension did and did not result in stroke.",qm.hypertension_n_stroke_or_not),
            'I':("Details of people whose heart dieases resulted in stroke.",qm.heart_disease_n_stroke),
            'J': ("Descriptive statistics of each features",qm.stats),
            'K': ("Average sleep hours of people with stroke and those without",qm.avg_sleep),
            'L':("Exit.", None)
                  }
    
    
    while True:
        option= input ('Enter a letter from the list above (A-L) to find more information about the analytics of the groups: ').strip().upper()

        if option not in maps:
            print('Wrong input. Please type in the correct letter A-L.')
            continue


        desc, func = maps[option]
        print(f'You selected option {option}: {desc}\n')


        if option == 'L':
            print('Thank you for using the Stroke Analytics program. We hope to see you soon.\n Goodbye!')
            break
            
        
        result = func()
        print('Below are the results:\n', result)

        cont = input('\nWould you like to perform another analysis? Respond with Y for Yes or N for No: ').strip().upper()

        while cont not in ['Y','N']:
            print('Please enter the correct correct letters Y for Yes or N for No.')
            cont = input('\nWould you like to perform another analysis? Respond with Y for Yes or N for No: ').strip().upper()
            
        if cont =='Y':
                
            print(f'''\n Please find below the various options for the subgroup analytics.\n
                  A Smokers with Hypertension resulting in stroke.\n
                  B Heart diseases that leads to stroke.\n
                  C Hypertension resulting in stroke and those not resulting in stroke based on genders.\n
                  D Smoking habits that resulted in stroke an smoking habits that did not result in stroke.\n
                  E Areas and their resulting stroke analysis.\n
                  F Stroke and Dietary analysis.\n
                  G Hypertension resulting in stroke.\n
                  H Details of people whose hypertension did and did not result in stroke.\n
                  I Details of people whose heart dieases resulted in stroke.\n
                  J Descriptive statistics of each features.\n
                  K Average sleep hours of people with stroke and those without.\n
                  L Exit.\n''')
                
                
        elif cont=='N':
            print('Thank you for using the Stroke Analytics program. We hope to see you soon.\n Goodbye!')
            break
            

if __name__=="__main__":
    user_interface()

