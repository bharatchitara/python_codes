#PF-Exer-30

def find_average(mark_list):
    total=0
    
    for i in range(0, len(mark_list)):
        try:
            total+=mark_list1[i]
        except:
            print("error")
        finally:
            total=sum(mark_list)
            marks_avg=total/len(mark_list)
        return marks_avg
    
m_list=[1,10,67,2]

print("Average marks:", find_average(m_list))
