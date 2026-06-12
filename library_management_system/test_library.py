import os
import time

# Use a separate file for testing
os.environ["LIBRARY_DATA_FILE"] = "test_data.json"

import data_manager
data_manager.DATA_FILE = "test_data.json"
import library

def run_tests():
    print("Running Tests...")
    
    # Clean up old test data if exists
    if os.path.exists(data_manager.DATA_FILE):
        os.remove(data_manager.DATA_FILE)
    
    data_manager.initialize_data()
    
    # 1. Admin Add Book (Sequential Check)
    print("Test 1: Admin Add Book & Sequential ID")
    id1 = library.add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Harry Potter")
    assert id1 == "1", f"Expected ID 1, got {id1}"
    
    id2 = library.add_book("Clean Code", "Robert C. Martin", None)
    assert id2 == "2", f"Expected ID 2, got {id2}"
    
    id3 = library.add_book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Harry Potter")
    assert id3 == "3", f"Expected ID 3, got {id3}"
    print("Passed.")
    
    # 2. Search by Title
    print("Test 2: Search by Title")
    res = library.search_by_title("harry")
    assert len(res) == 2, f"Expected 2 results, got {len(res)}"
    print("Passed.")
    
    # 3. User Receive Book (Collection)
    print("Test 3: Receive Book (Collection)")
    success, msg = library.receive_book("U1", "Alice", "1")
    assert success, msg
    
    # Verify that both HP books were issued
    data = data_manager.load_data()
    hp_issued = [t for t in data["transactions"] if t["book_id"] in ["1", "3"]]
    assert len(hp_issued) == 2, "Expected both books in the collection to be issued"
    print("Passed.")
    
    # 4. View Borrowed Books
    print("Test 4: View Borrowed Books")
    borrowed = library.view_borrowed_books()
    assert len(borrowed) == 2, "Expected 2 borrowed books"
    print("Passed.")
    
    # 5. User Return Book (Late)
    print("Test 5: Return Book (Late)")
    
    # Manually make the issue late by modifying due date
    data = data_manager.load_data()
    for t in data["transactions"]:
        t["due_date"] = "2020-01-01"  # Set due date in the past
    data_manager.save_data(data)
    
    success, msg = library.return_book("U1", "1")
    assert success, "Return should succeed"
    
    # Check if user blocked
    data = data_manager.load_data()
    assert data["users"]["U1"]["is_blocked"] == True, "User should be blocked due to late return"
    print("Passed.")
    
    # Clean up test data
    if os.path.exists(data_manager.DATA_FILE):
        os.remove(data_manager.DATA_FILE)
        
    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
