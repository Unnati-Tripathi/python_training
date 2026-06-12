import library
import data_manager
import sys

def print_header(title):
    print("\n" + "="*40)
    print(f"  {title}")
    print("="*40)

def admin_menu():
    while True:
        print_header("Admin Menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Clear Entry for Book")
        print("4. View Borrowed Books")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            collection = input("Enter Collection Name (or press Enter to skip): ")
            if not collection.strip():
                collection = None
            book_id = library.add_book(title, author, collection)
            print(f"Success! Book added with ID: {book_id}")
            
        elif choice == '2':
            book_id = input("Enter Book ID to remove: ")
            success, msg = library.remove_book(book_id)
            print(msg)
            
        elif choice == '3':
            book_id = input("Enter Book ID to clear entry: ")
            success, msg = library.clear_entry(book_id)
            print(msg)
            
        elif choice == '4':
            borrowed = library.view_borrowed_books()
            if not borrowed:
                print("No books are currently borrowed.")
            else:
                print(f"{'Book ID':<10} {'Title':<20} {'User':<15} {'Issue Date':<15} {'Due Date'}")
                print("-" * 75)
                for b in borrowed:
                    print(f"{b['book_id']:<10} {b['title'][:18]:<20} {b['user_name'][:13]:<15} {b['issue_date']:<15} {b['due_date']}")
                    
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def user_menu():
    user_name = input("Enter your Name: ")
    user_id = input("Enter your User ID: ")
    
    while True:
        print_header(f"User Menu - Welcome {user_name}")
        print("1. Search Book by Title")
        print("2. Search Book by Author")
        print("3. Receive (Issue) Book")
        print("4. Return Book")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            query = input("Enter title or substring to search: ")
            results = library.search_by_title(query)
            display_search_results(results)
            
        elif choice == '2':
            query = input("Enter author name to search: ")
            results = library.search_by_author(query)
            display_search_results(results)
            
        elif choice == '3':
            book_id = input("Enter Book ID to receive: ")
            success, msg = library.receive_book(user_id, user_name, book_id)
            print(msg)
            
        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            success, msg = library.return_book(user_id, book_id)
            print(msg)
            
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def display_search_results(results):
    if not results:
        print("No books found.")
        return
    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Collection'}")
    print("-" * 70)
    for b in results:
        coll = b['collection'] if b['collection'] else "N/A"
        print(f"{b['id']:<5} {b['title'][:28]:<30} {b['author'][:18]:<20} {coll}")

def main():
    data_manager.initialize_data()
    while True:
        print_header("Library Management System")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
