#Name: Jennifer Henriquez
#Assigment: 1.8 Perfomance Assesment
#CLass: SDC435
#Date: 12/18/2025


import redis

# Connecting to Redis server
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def query_set():
    keyName = input("\nEnter the key you wish to query:\n")
    memb = r.smembers(keyName)
    if memb:
        print(f"\nMember set '{keyName}':")
        for m in memb:
            print(m)
    else:
        print(f"\nSet '{keyName}' is empty..")

# Create a new set in the Redis Database
def add_set():
    keyName = input("\nEnter the key you want to add:\n")
    count = int(input("\nEnter how many members will this set have:\n"))
    for i in range(count):
        member = input("\nEnter the next member value:\n")
        r.sadd(keyName, member)
    print(f"\nSet '{keyName}' created with {count} member(s).")

# Update the members of a specific set
def update_set_members():
    keyName = input("\nEnter the key of the set you wish to update:\n")
    while True:
        print("\nPlease type in a number and press enter to execute the menu option")
        print("1. Add new member")
        print("2. Remove member")
        print("3. Remove all members")
        print("4. Exit update Menu")
        choice = input()
        if choice == "1":
            member = input("\nEnter the new member to add:\n")
            r.sadd(keyName, member)
            print(f"\nAdded member '{member}' to set '{keyName}'.")
        elif choice == "2":
            member = input("\nEnter member to remove:\n")
            r.srem(keyName, member)
            print(f"\nRemoved member '{member}' from set '{keyName}'.")
        elif choice == "3":
            print("\nRemoving all set members")
            for m in r.smembers(keyName):
                print(f"Removing member: {m}.")
                r.srem(keyName, m)
            print("\nThe cardinality of the set is now:")
            print(r.scard(keyName))
        elif choice == "4":
            break
        else:
            print("\nInvalid option")

# Deleting a specific set from the Redis database
def delete_set():
    keyName = input("\nEnter the key of the set you wish to delete:\n")
    r.delete(keyName)
    print(f"\nSet '{keyName}' has been deleted.")

# Delete all data from Redis database
def delete_all():
    confirm = input("\nAre you sure you want to delete all data? Type 'yes' to confirm:\n")
    if confirm.lower() == "yes":
        r.flushdb()
        print("\nAll data has been deleted from the database.")
    else:
        print("\nOperation cancelled.")

# Main menu
while True:
    print("\nType a number and press enter to execute the menu option")
    print("1. Query for set members")
    print("2. Add new set")
    print("3. Update members of a set")
    print("4. Delete a set")
    print("5. Delete all data from the database")
    print("6. Exit the program")
    choice = input()

    if choice == "1":
        query_set()
    elif choice == "2":
        add_set()
    elif choice == "3":
        update_set_members()
    elif choice == "4":
        delete_set()
    elif choice == "5":
        delete_all()
    elif choice == "6":
        print("\nExiting program.")
        break
    else:
        print("\nInvalid input. Please try again.")


    
