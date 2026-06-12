from datetime import datetime, timedelta
import data_manager

def get_current_date():
    return datetime.now().date()

# --- ADMIN FUNCTIONS ---

def add_book(title, author, collection=None):
    data = data_manager.load_data()
    
    # Calculate next sequential book ID
    if not data["books"]:
        new_id = "1"
    else:
        # Get all integer keys to find the max
        int_keys = [int(k) for k in data["books"].keys()]
        new_id = str(max(int_keys) + 1)
        
    data["books"][new_id] = {
        "id": new_id,
        "title": title,
        "author": author,
        "collection": collection
    }
    
    data_manager.save_data(data)
    return new_id

def remove_book(book_id):
    book_id = str(book_id)
    data = data_manager.load_data()
    
    if book_id not in data["books"]:
        return False, "Book not found."
        
    # Check if currently issued
    for t in data["transactions"]:
        if t["book_id"] == book_id and t["return_date"] is None:
            return False, "Cannot remove book. It is currently issued."
            
    # Remove book
    del data["books"][book_id]
    data_manager.save_data(data)
    return True, "Book removed successfully."

def clear_entry(book_id):
    """Clears all transaction history for a book and removes it completely."""
    book_id = str(book_id)
    data = data_manager.load_data()
    
    if book_id not in data["books"]:
        return False, "Book not found."
        
    # Remove transactions associated with this book
    data["transactions"] = [t for t in data["transactions"] if t["book_id"] != book_id]
    
    # Remove book
    del data["books"][book_id]
    data_manager.save_data(data)
    return True, "Book and its entries cleared successfully."

def view_borrowed_books():
    data = data_manager.load_data()
    borrowed = []
    
    for t in data["transactions"]:
        if t["return_date"] is None:
            book = data["books"].get(t["book_id"])
            user = data["users"].get(t["user_id"])
            if book and user:
                borrowed.append({
                    "book_id": t["book_id"],
                    "title": book["title"],
                    "user_name": user["name"],
                    "issue_date": t["issue_date"],
                    "due_date": t["due_date"]
                })
    return borrowed

# --- USER FUNCTIONS ---

def search_by_title(query):
    data = data_manager.load_data()
    results = []
    query = query.lower()
    for b_id, b_info in data["books"].items():
        if query in b_info["title"].lower():
            results.append(b_info)
    return results

def search_by_author(author_query):
    data = data_manager.load_data()
    results = []
    author_query = author_query.lower()
    for b_id, b_info in data["books"].items():
        if author_query in b_info["author"].lower():
            results.append(b_info)
    return results

def ensure_user(user_id, user_name, data):
    user_id = str(user_id)
    if user_id not in data["users"]:
        data["users"][user_id] = {
            "id": user_id,
            "name": user_name,
            "is_blocked": False
        }
    return data["users"][user_id]

def receive_book(user_id, user_name, book_id):
    user_id = str(user_id)
    book_id = str(book_id)
    data = data_manager.load_data()
    
    user = ensure_user(user_id, user_name, data)
    if user["is_blocked"]:
        return False, "User is blocked from receiving books due to late returns."
        
    if book_id not in data["books"]:
        return False, "Book not found."
        
    book = data["books"][book_id]
    
    # Check if book is already issued
    for t in data["transactions"]:
        if t["book_id"] == book_id and t["return_date"] is None:
            return False, "Book is already issued."
            
    # Find all books to issue (handle collections)
    books_to_issue = []
    if book["collection"]:
        collection_name = book["collection"]
        for b_id, b_info in data["books"].items():
            if b_info["collection"] == collection_name:
                # Check if any book in collection is already issued
                for t in data["transactions"]:
                    if t["book_id"] == b_id and t["return_date"] is None:
                        return False, f"Part of the collection '{collection_name}' is already issued."
                books_to_issue.append(b_id)
    else:
        books_to_issue.append(book_id)
        
    # Issue books
    issue_date = get_current_date()
    due_date = issue_date + timedelta(days=14)
    
    for b_id in books_to_issue:
        data["transactions"].append({
            "book_id": b_id,
            "user_id": user_id,
            "issue_date": issue_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "return_date": None
        })
        
    data_manager.save_data(data)
    return True, f"Successfully issued {len(books_to_issue)} book(s)."

def return_book(user_id, book_id):
    user_id = str(user_id)
    book_id = str(book_id)
    data = data_manager.load_data()
    
    if book_id not in data["books"]:
        return False, "Book not found."
        
    book = data["books"][book_id]
    
    # Find all books to return (handle collections)
    books_to_return = []
    if book["collection"]:
        collection_name = book["collection"]
        for b_id, b_info in data["books"].items():
            if b_info["collection"] == collection_name:
                books_to_return.append(b_id)
    else:
        books_to_return.append(book_id)
        
    returned_any = False
    late_return = False
    return_date = get_current_date()
    
    for b_id in books_to_return:
        # Find active transaction
        for t in data["transactions"]:
            if t["book_id"] == b_id and t["user_id"] == user_id and t["return_date"] is None:
                t["return_date"] = return_date.strftime("%Y-%m-%d")
                returned_any = True
                
                # Check if late
                due_date = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
                if return_date > due_date:
                    late_return = True
                break
                
    if not returned_any:
        return False, "No active issued record found for this book and user."
        
    if late_return:
        data["users"][user_id]["is_blocked"] = True
        data_manager.save_data(data)
        return True, "Book(s) returned late. User is now blocked."
        
    data_manager.save_data(data)
    return True, "Book(s) returned successfully."
