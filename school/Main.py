from school import School,classroom,Subject
from person import student,Teacher

def main():
    print('_________main is runnding_____')

    school= School('Rasullabad U.A khan High School','Arif college')

    #add classRooms

    eight =classroom('eight')
    school.add_classroom(eight)

    nine =classroom('nine')
    school.add_classroom(nine)

    ten =classroom('ten')
    school.add_classroom(ten)
    
    #add students

    abul = student('amir khan',eight)
    school.student_admission(abul)
    
    babul = student('babul khan',eight)
    school.student_admission(babul)
    
    kabul = student('kabul khan',eight)
    school.student_admission(kabul)

    #ADD SUBJECTS
    chemistry_teachers= Teacher('Jahangir sir,mohosin sir,Delware sir')
    physics = Subject('chemistry',chemistry_teachers)
    eight.add_subject(physics)

    Physics_teachers= Teacher('Jahangir sir,mohosin sir,Delware sir')
    physics = Subject('physics',Physics_teachers)
    eight.add_subject(physics)

    biology_teachers= Teacher('Jahangir sir,mohosin sir,Delware sir')
    physics = Subject('biology',biology_teachers)
    eight.add_subject(physics)


    eight.semister_final()

    print(school)
    

 
if __name__ == '__main__':
    main()