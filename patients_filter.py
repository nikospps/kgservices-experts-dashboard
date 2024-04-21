import patients_lists

def patients_filter(list1, list2):
    for dictionary in list2:
        if str(dictionary['email']).lower() == str(list1[0]['email']).lower():
            print("The dictionary from random_list exists in list")
            value = True
            break
        else:
            print("The dictionary from random_list does not exist in list.")
            value = False
    return value
##########################################################################
# random_list = [
#     {
#     'email': 'atRYpONi.alameda@gmail.com',
#     'organization': 'NKUA'
#     },
# ]
#
# nkua = patients_lists.list_nkua
# fism = patients_lists.list_fism
# suub = patients_lists.list_suub
#
# result = patients_filter(random_list,nkua)
###########################################################################
# meaa = get_fbdaily(access_token)
# message = []
# for n in meaa:
#     result = patients_filter([n], list_fism)
#     if (result == True):
#         message.append(n)