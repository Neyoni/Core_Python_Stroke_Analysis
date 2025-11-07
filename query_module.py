def save_to_csv(data, filename):
    with open(filename, "w") as file:
        file.write("Category,Mean,Median,Mode\n")
        for group, values in data.items():
            if isinstance(values, dict):
                mean = str(values.get("Mean", ""))
                median = str(values.get("Median", ""))
                mode = str(values.get("Mode", ""))
                file.write(f"{group},{mean},{median},{mode}\n")
            else:
                file.write(f"{group},{values},,\n")


def save_records_to_csv(records: dict, filename: str):
    if not records:
        return

    headers = list(records[next(iter(records))].keys())
    with open(filename, "w") as file:
        file.write(",".join(headers) + "\n")
        for item in records.values():
            row = []
            for h in headers:
                row.append(str(item.get(h, "")))
            file.write(",".join(row) + "\n")


class QueryModule():

    def __init__(self, dataset):#constructor
        self.dataset = dataset

#A function for computing the average age, modal age, and median age of those who smoked and had hypertension that resulted in stroke.
    def smoke_n_hypertension(self):
        age = []
        count = 0
        for num, value in self.dataset.items():
            if value['Hypertension'] == '1' and value['Smoking Status'] == 'Formerly smoked' and value['Stroke Occurrence'] == '1':
                age.append(int(value['Age']))
                count +=1 #uses count to increment every new addition of a figure to the list
            elif value['Smoking Status'] == 'Smokes' and value['Hypertension'] == '1'and value['Stroke Occurrence'] == '1':
                age.append(int(value['Age']))
                count+=1
    #avg age
        def avg_age():
            if count > 0: #checks if the count for the list is empty/if the list is empty.
                avg_age= sum(age)/count
                return round(avg_age,2)
            else:
                return None




#median age calculation
        def median_age():
            if len(age) == 0: #checks the length of the list age
                return None

            else:
                age.sort()
                middle= len(age)//2 #dividing the length of the list age by 2 using floor division to show the answer without remainders
                
                if len(age)%2 ==0: #if length of age divided by 2 equals to 0
                    return (age[middle] + age[middle-1])/2 #Using the result obtained from middle as an index to get the 2 middle numbers and then divide by 2
                else:
                    return age[middle]
                
        
        

    #modal age calculation
        def modal_age():
            modal = {}
            maximum= []
            for _ in age:#loop through every number in age
                if _ in modal:# checks if the number exists in the modal dictionary
                    modal[_] += 1 #if yes, it increments the count
                elif _ not in modal:
                    modal[_] = 1 #if no, it adds the pair to the dictionary
                
            maxi= max(modal.values()) #checks for the largest VALUE in the dictionary (key,value pair)

            for num, value in modal.items():#iterating through the modal dictionary
                if value == maxi: #checks each value to see if the Value in the (key value pair) present in modal matches the highest value stored in maxi
                    maximum.append(num)#adds the value obtained to the maximum list

            if len(maximum) == 1:#checks length
                return maximum[0] #if length equals 1 returns the only value in the list maximum
            else: 
                return maximum #else returns the numbers that appear.

        
        result = {
            "Smokers with Hypertension that caused Stroke": {
                "Mean": avg_age(),
                "Median": median_age(),
                "Mode": modal_age()
            }
        }

    
        save_to_csv(result, "smoke_n_hypertension.csv") #result saved in csv format


        output = (
            f"Average age: {avg_age()}\n"
            f"Median age: {median_age()}\n"
            f"Mode age: {modal_age()}"
        )
        return output #output returned.
        

    #Calculating the mean, median, mode and avg glucose level ages for heart diseases that leads to stroke.

    def heart_disease_lead_to_stroke(self):
        age = []
        count=0
        glucose = []
        for num, value in self.dataset.items():
            if value['Smoking Status']== 'Formerly smoked' and value['Stroke Occurrence']== '1':
                age.append(int(value['Age']))
                glucose.append(eval(value['Average Glucose Level']))
                count+=1
            elif value['Smoking Status'] == 'Smokes' and value ['Stroke Occurrence']== '1':
                age.append(int(value['Age']))
                glucose.append(eval(value['Average Glucose Level']))
                count+=1

        def avg_age():
            if len(age) >0:
                mean = sum(age)/len(age)
            return round(mean,2)
            
        def median():
            if len(age) == 0:
                return None
            else:
                age.sort()
                middle = len(age)//2
                if len(age) % 2 == 0: 
                    return age[middle] + age[middle -1]/2
                else:
                    return age[middle]
                

        def mode():
            modal= {}
            maximum=[]
            for num in age:
                if num in modal:
                    modal[num] += 1
                else: 
                    modal[num] = 1
            maxi = max(modal.values())
            for n,v in modal.items():
                if v == maxi:
                    maximum.append(n)
            if len (maximum)==1:
                return maximum[0]
            else:
                return maximum
       
        def avg_glucose():
            if len(glucose) == 0:
                return 'The average glucose level for this request cannot be returned: There exists no record'
            else:
                mean_glucose = sum(glucose)/ len(glucose)
                return f'The average glucose level for people with heart disease that leads to stroke is {round(mean_glucose,3)}'
            


        result = {
            "Heart disease that caused Stroke": {
                "Mean": avg_age(),
                "Median": median(),
                "Mode": mode(),
                "Average glucose level": avg_glucose()
            }
        }

    
        save_to_csv(result,"Heart disease that led to Stroke.csv") #result saved in csv format

            

        output = (
            f'Average Age: {avg_age()}\n'
            f'Median Age: {median()}\n'
            f'Modal Age: {mode()}\n'
            f'Average Glucose Level: {avg_glucose()}\n'
        )
        return output
                    
                    


#Calculating the mean,median and modal age patients based on genders of those whose hypertensions resulted in stroke and of those whose hypertensions did not resultin stroke.

    def gender_hypertension(self):
        f_age_h = []
        m_age_h = []
        f_age_nh = []
        m_age_nh=[]
        count_f_h=0
        count_f_nh=0
        count_m_h=0
        count_m_nh = 0

        for num, value in self.dataset.items():
            if value['Gender'] == 'Female' and value['Hypertension'] == '1'and value['Stroke Occurrence'] == '1':
                f_age_h.append(float(value['Age']))
                count_f_h+=1
            elif value['Gender'] == 'Female' and value['Hypertension'] == '1'and value['Stroke Occurrence'] == '0':
                f_age_nh.append(float(value['Age']))
                count_f_nh+=1
            elif value['Gender'] == 'Male' and value['Hypertension'] == '1'and value['Stroke Occurrence'] == '1':
                m_age_h.append(float(value['Age']))
                count_m_h+=1
            elif value['Gender'] == 'Male' and value['Hypertension'] == '1'and value['Stroke Occurrence'] == '0':
                m_age_nh.append(float(value['Age']))
                count_m_nh+=1
                
        #avg_age
        def get_mean(data):
            return sum(data) / len(data)

        
        def get_median(data):
            data.sort()
            mid = len(data) // 2
            if len(data) % 2 == 0:
                return (data[mid - 1] + data[mid]) / 2
            else:
                return data[mid]

        def get_mode(data):
            freq = {}
            modes =[]
            for age in data:
                freq[age] = freq.get(age, 0) + 1
            max_freq = max(freq.values())
            for k, v in freq.items(): 
                if v == max_freq:
                    modes.append(k)
            return modes[0]

        result = {}
        groups = {
            "Female with Hypertension leading to Stroke": f_age_h,
            "Female with Hypertension leading to No_Stroke": f_age_nh,
            "Male with Hypertension leading to Stroke": m_age_h,
            "Male with Hypertensionleading to No_Stroke": m_age_nh,}
        
        
    
        save_to_csv(groups,"Hypertension land Gender.csv") #result saved in csv format


        for group, ages in groups.items():
            if ages:
                result[group] = {
                    "Mean": round(get_mean(ages), 2), 
                    "Median": round(get_median(ages), 2),
                    "Mode": round(get_mode(ages), 2),
                }
            else:
                result[group] = "No data"

        return result






    #A function for computing the average age, modal age, median age of those whose smoking habits result in stroke and for those whose smoking habit did not result in stroke

    def smoking_stroke_occurrence(self):
        sm_st=[]
        sm_nst=[]
        fsm_st=[]
        fsm_nst=[]
        for num, value in self.dataset.items():
            if value['Smoking Status'] =='Smokes' and value['Stroke Occurrence'] == '1':
                sm_st.append(eval(value['Age']))
            elif value['Smoking Status'] == 'Smokes' and value['Stroke Occurrence'] == '0':
                sm_nst.append(eval(value['Age']))
            elif value['Smoking Status'] == 'Formerly Smoked' and value['Stroke Occurrence'] == '1':
                fsm_st.append(eval(value['Age']))
            elif value['Smoking Status'] == 'Formerly Smoked' and value['Stroke Occurence'] == '0':
                fsm_nst.append(eval(value['Age']))

        def get_mean(data):
            return sum(data)/len(data)
            
        def get_median(data):
            data.sort()
            mid=len(data)//2
            if len(data)%2 == 0:
                return (data[mid-1] + data[mid])/2
            else:
                return data[mid]

        def get_mode(data):
            modes = []
            freq ={}
            for age in data:
                if age not in freq:
                    freq[age]=1
                else:
                    freq[age]+=1
            max_freq = max(freq.values())
            for age,value in freq.items():
                if value == max_freq:
                    modes.append(age)
            if len(modes)==1:
                return modes[0]
            else:
                return modes
                    
        result={}
        groups={
            'currently smoking habits that resulted in stroke':sm_st,
            "currently smoking habits that didn't result in stroke":sm_nst,
            'formerly smoking habits that resulted in stroke':fsm_st,
            "formerly smoking habits that didn't result in stroke":fsm_nst,
        }

       

        save_to_csv(result,"Smoking habits leading to Stroke.csv") #result saved in csv format

        for group,ages in groups.items():
            if ages:
                result[group]={
                    'Mean':round(get_mean(ages),2),
                    'Median':round(get_median(ages),2),
                    'Mode' :(get_mode(ages)),}
            else:
                result[group]= 'No result found'
        return result
           
                

#A function for computing the average age, modal age, median age of those who lived in urban areas and for those in rural areas that had stroke.

    def area_stroke(self):
        urban_age = []
        rural_age =[]
        for num, value in self.dataset.items():
            if value['Residence Type']=='Urban' and value['Stroke Occurrence'] == '1':
                urban_age.append(eval(value['Age']))
            elif value['Residence Type']=='Rural' and value['Stroke Occurrence']=='1':
                rural_age.append(eval(value['Age']))


        def get_mean(data):
            return sum(data)/len(data)


        def get_median(data):
            data=sorted(data)
            mid = len(data)//2
            if len(data)%2 ==0:
                return (data[mid-1] + data[mid])/2
            else:
                return data[mid]


        def get_mode(data):
            modes=[]
            freq= {}
            for age in data:
                if age not in freq:
                    freq[age]=1
                else:
                    freq[age]+=1
            max_freq = max(freq.values())
            for num, value in freq.items():
                if value == max_freq:
                    modes.append(num)
            if len(modes) == 1:
                return modes[0]
            else:
                return modes

        result = {}
        groups={
            'Urban Residents with stroke occurence': urban_age,
            'Rural Residents with stroke occurrence': rural_age,
        }

        

        save_to_csv(result,"Locations and their Stroke Occurrences.csv") #result saved in csv format


        for group, age in groups.items():
            if age:
                result[group]= {
                    'Mean': round(get_mean(age),2),
                    'Median': round(get_median(age),2),
                    'Mode': (get_mode(age)),
                }
            else:
                result[group]='no data'
        return result


    def Dietary_n_stroke(self):
        
        mixed_stroke = 0
        vegetarian_stroke=0
        non_vegetarian_stroke=0
        mixed_no_stroke=0
        vegetarian_no_stroke=0
        non_vegetarian_no_stroke=0
        
        for num, value in self.dataset.items():
            if value['Stroke Occurrence'] == '1' and  value['Dietary Habits']=='Mixed':
                mixed_stroke+=1
            elif value['Stroke Occurrence'] == '1' and  value['Dietary Habits']=='Vegetarian':
                vegetarian_stroke+=1
            elif value['Stroke Occurrence'] == '1' and  value['Dietary Habits']=='Non-Vegetarian':
                non_vegetarian_stroke+=1
            elif value['Stroke Occurrence'] == '0' and  value['Dietary Habits']=='Mixed':
                mixed_no_stroke+=1
            elif value['Stroke Occurrence'] == '0' and  value['Dietary Habits']=='Vegetarian':
                vegetarian_no_stroke+=1
            elif value['Stroke Occurrence'] == '0' and  value['Dietary Habits']=='Non-Vegetarian':
                non_vegetarian_no_stroke+=1
        

        result1 = {
            "Dietary Stroke Analysis - No Stroke": {
            "Mixed": mixed_no_stroke,
            "Vegetarian": vegetarian_no_stroke,
            "Non-Vegetarian": non_vegetarian_no_stroke
              },
              "Dietary Stroke Analysis - Has Stroke": {
                  "Mixed": mixed_stroke,
                "Vegetarian": vegetarian_stroke,
                "Non-Vegetarian": non_vegetarian_stroke
                }
                  }

        save_records_to_csv(result1,"Dietary Preference and their Stroke Occurrences.csv") #result saved in csv format

                
        output={
            'No_stroke': {
                'Mixed':mixed_no_stroke,
                'Vegetarian': vegetarian_no_stroke,
                'Non-Vegetarian': non_vegetarian_no_stroke
                },
            'Has_stroke':{
                'Mixed': mixed_stroke,
                'Vegetarian': vegetarian_stroke,
                'Non-Vegetarian': non_vegetarian_stroke
                }
            }
        return output
        
        
    



#A function that returns anyone whose hypertension resulted in stroke.

    def stroke_n_hypertension(self):
        hyp_stroke = {}
        for num, value in self.dataset.items():
            if value['Hypertension'] == '1' and value['Stroke Occurrence']=='1':
                hyp_stroke[num] = value

        save_records_to_csv(hyp_stroke, "stroke_n_hypertension.csv")

        return f'These people have hypertension that resulted in stroke:\n{hyp_stroke}.'



#A function to retrieve those who hypertension did not result in stroke and those whose hypertension resulted in stroke
    def hypertension_n_stroke_or_not(self):
        hyp_stroke={}
        hyp_no_stroke={}
        for num,value in self.dataset.items():
            if value['Hypertension'] == '1' and value['Stroke Occurrence']=='1':
                hyp_stroke[num]=value
            elif value['Hypertension'] == '1' and value['Stroke Occurrence']=='0':
                hyp_no_stroke[num]=value


      
        save_records_to_csv(hyp_stroke, "Hypertension and Stroke.csv")
        save_records_to_csv(hyp_stroke, "Hypertension and no stroke.csv")

        return (
            f"These people have hypertension that resulted in stroke:\n {hyp_stroke}\n\n"
            f'These people have hypertension that did not result in stroke:\n {hyp_no_stroke}'
        )


#A function that returns everyone with heart disease with a stroke.

    def heart_disease_n_stroke(self):
        heart={}
        for num,value in self.dataset.items():
            if value['Heart Disease'] =='1' and value['Stroke Occurrence'] == '1':
                heart[num]=value
                
        save_records_to_csv(heart,"Heart Disease and Stroke.csv")
        return f'These people have heart disease that resulted in stroke:\n{heart}'

#A function to retrieve the average sleep hours of those who had stroke and those who did not have stroke
    
    def avg_sleep(self):
        sleep=[]
        sleep2=[]
        for num,value in self.dataset.items():
            if value['Stroke Occurrence']=='1':
                sleep.append(eval(value['Sleep Hours']))
            elif value['Stroke Occurrence']=='0':
                sleep2.append(eval(value['Sleep Hours']))

        def mean(data):
            return sum(data)/len(data)

        result1 = {
            "Average Sleep": {
                "Mean for those who had stroke": mean(sleep),
                "Mean for those who did not have stroke":mean(sleep2),
               
            }
        }

        save_to_csv(result1,"Average Sleep.csv") #result saved in csv format



        output = (
            f'The average sleep for those with stroke is {round(mean(sleep),2)}\n'
            f'The average sleep for those who do not have stroke is {round(mean(sleep2),2)}'
        )
        return output

#A function that returns the descriptive statistics of any of the features of the dataset.This function should ask for which feature to analyse and then return the statistics. The descriptive statistics are mean, standard deviation, minimum, maximum, 25%, 50%, and 75%.

    def stats(self):
        feature_map = {
            'A': 'Age',
            'B': 'Gender',
            'C': 'Hypertension',
            'D': 'Heart Disease',
            'E': 'Ever Married',
            'F': 'Work Type',
            'G': 'Residence Type',
            'H': 'Average Glucose Level',
            'I': 'BMI',
            'J': 'Smoking Status',
            'K': 'Physical Activity',
            'L': 'Dietary Habits',
            'M': 'Alcohol Consumption',
            'N': 'Chronic Stress',
            'O': 'Sleep Hours',
            'P': 'Family History',
            'Q': 'Education Level',
            'R': 'Income Level',
            'S': 'Stroke Risk Score',
            'U': 'Region',
            'V': 'Stroke Occurrence'
        }

        print('''list of available features in the dataset include:
              A : Age
        B : Gender
        C : Hypertension
        D : Heart Disease
        E : Ever Married
        F : Work Type
        G : Residence Type
        H : Average Glucose Level
        I : BMI
        J : Smoking Status
        K : Physical Activity
        L : Dietary Habits
        M : Alcohol Consumption
        N : Chronic Stress
        O : Sleep Hours
        P : Family History
        Q : Education Level
        R : Income Level
        S : Stroke Risk Score
        U : Region
        V : Stroke Occurrence''')

        request = input('Enter a feature you would like to see the statistics of from the above list A-V: ').strip().upper()

        while request not in feature_map:
            print('Wrong input, enter a valid letter from A to V.')
            request = input('Enter a feature again: ').strip().upper()

        request1 = feature_map[request]

        data = []
        for num, value in self.dataset.items():
            if request1 in value and value[request1] != '':
                data.append(value[request1])

        num_data = []
        non_num_data = []

        for i in data:
            try:
                val = eval(i)
                if isinstance(val, (int, float)):
                    num_data.append(val)
                else:
                    non_num_data.append(i)
            except:
                non_num_data.append(i)

        if num_data:
            num_data.sort()

            def mean(data):
                if len(data) != 0:
                    return sum(data) / len(data)
                return 'No data'

            def standard_dev(data):
                if len(data) != 0:
                    mean_val = sum(data) / len(data)
                    var = 0
                    for num in data:
                        var += (num - mean_val) ** 2
                    return (var / len(data)) ** 0.5
                return 'No data'

            def min_value(data):
                if len(data) != 0:
                    return min(data)
                return 'No data'

            def max_value(data):
                if len(data) != 0:
                    return max(data)
                return 'No data'

            def percentile(data, p):
                n = len(data)
                index = (n - 1) * p
                lower = int(index)
                upper = lower + 1
                if upper >= n:
                    return data[lower]
                return data[lower] + (data[upper] - data[lower]) * (index - lower)

            result1 = {
                "Descriptive Stats": {
                    "Mean": mean(num_data),
                    "Standard Deviation": standard_dev(num_data),
                    "Minimum Value": min_value(num_data),
                    "Maximum Value": max_value(num_data),
                    "25th Percentile": percentile(num_data, 0.25),
                    "50th Percentile": percentile(num_data, 0.50),
                    "75th Percentile": percentile(num_data, 0.75),
                }
            }

            save_to_csv(result1, f"{request1}_descriptive_statistics.csv")

            return f'''Below are the results for "{request1}":
            Mean: {round(mean(num_data),2)}
            Standard Deviation: {round(standard_dev(num_data),2)}
            Minimum: {min_value(num_data)}
            Maximum: {max_value(num_data)}
            25th Percentile: {percentile(num_data,0.25)}
            50th Percentile: {percentile(num_data,0.50)}
            75th Percentile: {percentile(num_data,0.75)}
            '''
        else:
            counter = {}
            for item in non_num_data:
                if item in counter:
                    counter[item] += 1
                else:
                    counter[item] = 1

            max_category = None
            max_count = 0
            for category, count in counter.items():
                if count > max_count:
                    max_category = category
                    max_count = count

            results = {
                "Most Common Category": max_category,
                "Frequency": max_count,
                "All Category Counts": counter
            }

            save_to_csv(results, f"{request1}_category_statistics.csv")

            return (f"\nBelow are the category statistics for '{request1}':\n"
                    f"Most Common: {max_category} ({max_count} times)\n"
                    f"All counts: {counter}")
