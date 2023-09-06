import books_operations as bo
#-------------main--------------
while True :
     print("===========================================")
     print ("press A to add a book")
     print ("press L to list all books")
     print ("press F to find a book")
     print ("press D to delete a book")
     print ("press Q to quit application")
     print("========================================")
     choice = input("enter your choice: ").upper()
     if choice == "A":
       bo.add_book()
     elif choice =="L" :
       bo.list_books()
     elif choice =="F" :
       bo.find_book()  
     elif choice == "D" :
      bo.delete_book()  
     elif choice == "Q" :
      break
     else :
        print("erong choice")