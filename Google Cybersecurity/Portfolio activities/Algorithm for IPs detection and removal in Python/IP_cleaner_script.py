# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Create a function called `remove_id_from_file` that takes in a file and an array as parameters.
#  The function should read the file, remove any lines that match the IP addresses in the array, 
# and then write the updated content back to the file.

def remove_ip_from_file(allowed_ip_file, array):

    # Open the file in read mode and read its content.

    with open(allowed_ip_file, 'r')as file:

        # Store the content of the file in a variable called `file_content`.

        file_content = file.read()
        # Split the content of the file into a list of IDs and store it in a variable called `list_of_ids`.

    list_of_ips = file_content.split()

    
    # Loop through each IP address in the array.

    for ip in array:

        # Check if the IP address is in the list of IDs.

        if ip in list_of_ips:

            # If it is, remove it from the list.
            print("unauthorized IP address found in the allowed list: " + ip)

            list_of_ips.remove(ip)
        else:
            print("IP address not found in the allowed list: " + ip)

    list_of_ips = "\n".join(list_of_ips)
  
    # Open the file in write mode and write the updated list of IPs back to the file.

    with open(allowed_ip_file, 'w')as file:
        file.write(list_of_ips)


def is_ip_in_file(allowed_ip_file, array):
    counter = 0
    with open(allowed_ip_file, 'r')as file:
        file_content = file.read()
    list_of_ips = file_content.split()
    for ip in array:
        if ip in list_of_ips:
            counter += 1
        else:
            counter = counter
    print("number of unauthorized IP addresses found in the allowed list: " + str(counter))
            
            
# check if not allowed ids exist in the allowed list

is_ip_in_file("allow_list.txt", remove_list)

# Call the `remove_ip_from_file` function, passing in the file name and the `remove_list` as arguments if the IP addresses in the `remove_list` are still present in the allowed list file.

remove_ip_from_file("allow_list.txt", remove_list)

# check if not allowed ips still exist in the allowed list

is_ip_in_file("allow_list.txt", remove_list)

