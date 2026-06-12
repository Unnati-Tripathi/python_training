from datetime import datetime, timedelta

# Data storage variables
book_inventory = {}
member_records = {}
issue_history = []

def get_today_date():
    return datetime.now().date()

def register_new_book(title, author_name, series_name=""):
    if len(book_inventory) == 0:
        next_book_id = "1"
    else:
        max_id = 0
        for b_id in book_inventory.keys():
            if int(b_id) > max_id:
                max_id = int(b_id)
        next_book_id = str(max_id + 1)
        
    book_inventory[next_book_id] = {
        "id": next_book_id,
        "book_title": title,
        "author": author_name,
        "series": series_name if series_name else None
    }
    return next_book_id

def delete_book_record(b_id):
    b_id = str(b_id)
    if b_id not in book_inventory:
        return False, "This book does not exist in our records."
        
    for rec in issue_history:
        if rec["b_id"] == b_id and rec["date_returned"] is None:
            return False, "You can't delete a book that is currently checked out."
            
    del book_inventory[b_id]
    return True, "Book deleted."

def wipe_book_data(b_id):
    b_id = str(b_id)
    if b_id not in book_inventory:
        return False, "This book does not exist."
        
    global issue_history
    updated_history = []
    for rec in issue_history:
        if rec["b_id"] != b_id:
            updated_history.append(rec)
    issue_history = updated_history
    
    del book_inventory[b_id]
    return True, "Book and all its history wiped out."

def list_issued_books():
    active_loans = []
    for rec in issue_history:
        if rec["date_returned"] is None:
            bk = book_inventory.get(rec["b_id"])
            mem = member_records.get(rec["m_id"])
            if bk and mem:
                active_loans.append({
                    "book_id": rec["b_id"],
                    "title": bk["book_title"],
                    "member": mem["member_name"],
                    "issued": rec["date_issued"],
                    "due": rec["date_due"]
                })
    return active_loans

def search_title(text):
    found = []
    text = text.lower()
    for b_id, info in book_inventory.items():
        if text in info["book_title"].lower():
            found.append(info)
    return found

def search_author(author_text):
    found = []
    author_text = author_text.lower()
    for b_id, info in book_inventory.items():
        if author_text in info["author"].lower():
            found.append(info)
    return found

def check_member_exists(m_id, m_name):
    m_id = str(m_id)
    if m_id not in member_records:
        member_records[m_id] = {
            "id": m_id,
            "member_name": m_name,
            "blocked": False
        }
    return member_records[m_id]

def checkout_book(m_id, m_name, b_id):
    m_id = str(m_id)
    b_id = str(b_id)
    
    mem = check_member_exists(m_id, m_name)
    if mem["blocked"] == True:
        return False, "Error: Member is blocked because of late returns."
        
    if b_id not in book_inventory:
        return False, "Invalid book ID."
        
    target_book = book_inventory[b_id]
    
    # Check if already issued
    for rec in issue_history:
        if rec["b_id"] == b_id and rec["date_returned"] is None:
            return False, "Book is currently unavailable."
            
    # Handle series logic
    checkout_list = []
    if target_book["series"]:
        s_name = target_book["series"]
        for current_id, info in book_inventory.items():
            if info["series"] == s_name:
                for rec in issue_history:
                    if rec["b_id"] == current_id and rec["date_returned"] is None:
                        return False, f"A book from the {s_name} series is already issued out."
                checkout_list.append(current_id)
    else:
        checkout_list.append(b_id)
        
    today = get_today_date()
    deadline = today + timedelta(days=14)
    
    for issue_id in checkout_list:
        issue_history.append({
            "b_id": issue_id,
            "m_id": m_id,
            "date_issued": today.strftime("%Y-%m-%d"),
            "date_due": deadline.strftime("%Y-%m-%d"),
            "date_returned": None
        })
        
    return True, f"Checkout successful. {len(checkout_list)} item(s) issued."

def bring_book_back(m_id, b_id):
    m_id = str(m_id)
    b_id = str(b_id)
    
    if b_id not in book_inventory:
        return False, "Invalid book ID."
        
    target_book = book_inventory[b_id]
    
    return_list = []
    if target_book["series"]:
        s_name = target_book["series"]
        for current_id, info in book_inventory.items():
            if info["series"] == s_name:
                return_list.append(current_id)
    else:
        return_list.append(b_id)
        
    found_record = False
    is_late = False
    now = get_today_date()
    
    for r_id in return_list:
        for rec in issue_history:
            if rec["b_id"] == r_id and rec["m_id"] == m_id and rec["date_returned"] is None:
                rec["date_returned"] = now.strftime("%Y-%m-%d")
                found_record = True
                
                due_val = datetime.strptime(rec["date_due"], "%Y-%m-%d").date()
                if now > due_val:
                    is_late = True
                break
                
    if found_record == False:
        return False, "Could not find an active checkout for this user and book."
        
    if is_late == True:
        member_records[m_id]["blocked"] = True
        return True, "Items returned after due date. Member status set to blocked."
        
    return True, "Items returned successfully."


# Start of program interface
if __name__ == "__main__":
    while True:
        print("\n--- Library System Menu ---")
        print("1. Admin Access")
        print("2. Member Access")
        print("3. Quit System")
        
        main_choice = input("Enter your option (1-3): ")
        
        if main_choice == '1':
            while True:
                print("\n[Admin Menu]")
                print("1. Add a Book to Inventory")
                print("2. Delete a Book")
                print("3. Wipe Book History")
                print("4. Check Active Loans")
                print("5. Go Back")
                
                admin_opt = input("Select: ")
                
                if admin_opt == '1':
                    b_name = input("Book Title: ")
                    a_name = input("Author Name: ")
                    s_name = input("Series Name (leave blank if none): ")
                    new_val = register_new_book(b_name, a_name, s_name)
                    print(f"Book added. Assigned ID is {new_val}")
                    
                elif admin_opt == '2':
                    del_id = input("Enter Book ID to delete: ")
                    status, message = delete_book_record(del_id)
                    print(message)
                    
                elif admin_opt == '3':
                    wipe_id = input("Enter Book ID to completely wipe: ")
                    status, message = wipe_book_data(wipe_id)
                    print(message)
                    
                elif admin_opt == '4':
                    loans = list_issued_books()
                    if len(loans) == 0:
                        print("No books are currently checked out.")
                    else:
                        print("ID   | Title                | Member       | Issued       | Due Date")
                        print("----------------------------------------------------------------------")
                        for loan in loans:
                            t_str = loan['title'][:20]
                            m_str = loan['member'][:12]
                            print(f"{loan['book_id']:<4} | {t_str:<20} | {m_str:<12} | {loan['issued']:<12} | {loan['due']}")
                            
                elif admin_opt == '5':
                    break
                else:
                    print("Invalid option. Try again.")
                    
        elif main_choice == '2':
            print("\n[Member Verification]")
            u_name = input("Enter your full name: ")
            u_id = input("Enter your member ID: ")
            
            while True:
                print("\n[Member Menu - " + u_name + "]")
                print("1. Find Book by Title")
                print("2. Find Book by Author")
                print("3. Checkout a Book")
                print("4. Return a Book")
                print("5. Go Back")
                
                mem_opt = input("Select: ")
                
                if mem_opt == '1':
                    search_text = input("Enter title keyword: ")
                    res = search_title(search_text)
                    if len(res) == 0:
                        print("No matches found.")
                    else:
                        for b in res:
                            ser = b['series'] if b['series'] else 'None'
                            print(f"[{b['id']}] {b['book_title']} by {b['author']} (Series: {ser})")
                            
                elif mem_opt == '2':
                    search_text = input("Enter author keyword: ")
                    res = search_author(search_text)
                    if len(res) == 0:
                        print("No matches found.")
                    else:
                        for b in res:
                            ser = b['series'] if b['series'] else 'None'
                            print(f"[{b['id']}] {b['book_title']} by {b['author']} (Series: {ser})")
                            
                elif mem_opt == '3':
                    target_id = input("Enter the Book ID you want to checkout: ")
                    status, message = checkout_book(u_id, u_name, target_id)
                    print(message)
                    
                elif mem_opt == '4':
                    target_id = input("Enter the Book ID you are returning: ")
                    status, message = bring_book_back(u_id, target_id)
                    print(message)
                    
                elif mem_opt == '5':
                    break
                else:
                    print("Invalid option. Try again.")
                    
        elif main_choice == '3':
            print("System shutting down...")
            break
        else:
            print("Please enter a valid option.")
