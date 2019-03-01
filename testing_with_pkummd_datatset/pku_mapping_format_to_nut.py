import os

pku_label_directory = '../../../hien_data/PKUMMD/label/Train_Label_PKU_final/test/'
pku_data_directory = '../../../hien_data/PKUMMD/data/PKU_Skeleton_Renew/test/'

# list all text file in the folder
label_file_list = os.listdir(pku_label_directory)
data_file_list = os.listdir(pku_data_directory)
print(label_file_list)
print(data_file_list)

number_of_joint = 25
number_of_dimension = 3

# read a label file
def read_label_data(label_filename):
    # with open(pku_label_directory + label_filename , 'r') as f:
    #     lines = f.readline()
    #     print(lines)

    # This way works more efficient in big data to avoid MemoryError
    with open(pku_label_directory + label_filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
        # tesing with frist line only
        print(lines[0])
        values = lines[0].split(',')
        for value in values:
            print(value)

        # pass start_frame, end_frame, and action_number in this order to data file
        read_data_and_split_action(label_filename, values)




# read a data file and slip actions
def read_data_and_split_action(data_filename, values):
    with open(pku_data_directory + data_filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]

        # Assume that start_frame and end_frame in the label file starts from 1 as the author counts the action_class from 1
        start_frame = int(values[1]) - 1
        end_frame = int(values[2]) - 1
        action_number = values[0]

        data = lines[start_frame:end_frame+1]
        #print(data)
        split_action_from_video(data_filename, data, values)

# write skeleton info for one person for one frame in the ntu format
def write_one_skeleton_info_for_one_person(data_per_person):
    skeleton_per_one_person = ''
    i = 0
    while i < len(data_per_person) - 2:
        x = data_per_person[i]
        y = data_per_person[i + 1]
        z = data_per_person[i + 2]

        temp_info = 8 * '0.0 ' + '2'
        joint_first_person = x + ' ' + y + ' ' + z + ' ' + temp_info + '\n'
        skeleton_per_one_person += joint_first_person
        # print('temp_info: ', joint_first_person)
        i = i + 3
    #print(skeleton_per_one_person)
    return skeleton_per_one_person

def split_action_from_video (file_name, data, values):
    # this function slips actions from video based on the start_frame and end_frame and action_number in label file to
    # ensure that each label has one action only (that is the same format of nut dataset)
    data_filename_new = file_name.split('.')[0] + '_new.txt'
    with open(pku_data_directory + data_filename_new, 'w') as f_data_new:
        f_data_new.writelines('%s\n' % i for i in data)

    # write data in the nut format
    # Assume that start_frame and end_frame in the label file starts from 1 as the author counts the action_class from 1
    action_number = values[0]

    number_of_frame = len(data)
    print('number of frame: ', number_of_frame)

    # number of people
    for i in range(number_of_frame):
        temp = data[i].split()

        data_first_person = temp[0:number_of_dimension*number_of_joint]

        print('First person:')
        print(data_first_person)

        data_second_person = temp[number_of_dimension*number_of_joint:len(temp)]
        #print(data_second_person)
        float_data_second_person = list(map(float, data_second_person))
        number_of_people = 1 if sum(float_data_second_person) == 0 else 2
        #number_of_people = 2

        body_info = '72057594037931101 0 1 1 1 1 0 0.02764709 0.05745083 2'


        # split joint info
        skeleton_first_person = write_one_skeleton_info_for_one_person(data_first_person)
        print(skeleton_first_person)


        # write joint information in the format of ntu
        data_filename_ntu_format = file_name.split('.')[0] + '_ntu_format.txt'
        file_exist = os.path.isfile(pku_data_directory + data_filename_ntu_format)
        #mode = 'w' if file_exist == False else 'a'
        # print('file exist: ', file_exist)

        with open(pku_data_directory + data_filename_ntu_format, 'a') as f_data_ntu:
            if file_exist == False:
                f_data_ntu.writelines('%s\n' % number_of_frame)
            f_data_ntu.writelines('%s\n' % number_of_people)
            f_data_ntu.writelines('%s\n' % body_info)
            f_data_ntu.writelines('%s\n' % number_of_joint)
            f_data_ntu.writelines(skeleton_first_person)
            # if there are 2 people, write the skeleton info for the second person
            if number_of_people == 2:
                f_data_ntu.writelines('%s\n' % number_of_joint)
                skeleton_second_person = write_one_skeleton_info_for_one_person(data_second_person)
                f_data_ntu.writelines(skeleton_second_person)


# read all label files
read_label_data(label_file_list[0])

#def change_pku_format_to_ntu_format():
#change_pku_format_to_ntu_format()
